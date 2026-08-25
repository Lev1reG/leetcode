class Solution:
    def simplifyPath(self, path: str) -> str:
        # split path based on /
        # result (its a stack!) initialize with / since all of the path will start with /
        # iterate through split
        # if item == "..": result.pop
        # else: result.append
        splittedPath = path.strip("/").split("/")
        stack = []

        for item in splittedPath:
            if item == "." or item == "":
                continue

            if item == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(item)

        return "/" + "/".join(stack)