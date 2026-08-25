class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # We do top down approach
        # we will create a recursive function call, lets say the function called min_coin
        # in those function we need to check
        # 1. if target == 0, return 0 (we reach the end & could sum up the amount)
        # 2. if target < 0, return inf (impossible)
        # and then, we need to recursively solve min_coin(amount - coin)
        # if those sub result is not returning inf, we update the best_score by compare it & find the minimum with min_coin(1 + sub result)
        # overall min_coin(amount) is given the amount, return the minimum value we could sum the amount
        memo = [-1]*(amount + 1)
        def min_coin(target):
            if target == 0:
                return 0
            if target < 0:
                return inf
            if memo[target] != -1:
                return memo[target]
            
            best_result = inf

            for coin in coins:
                sub_result = min_coin(target - coin)
                if sub_result != inf:
                    best_result = min(best_result, sub_result + 1)
            memo[target] = best_result
            return memo[target]
        
        result = min_coin(amount)
        if result != inf:
            return result
        else:
            return -1