impl Solution {
    pub fn is_valid(word: String) -> bool {
        if word.len() < 3 {
            return false;
        }

        if !word
            .chars()
            .all(|c| c.is_ascii_digit() || c.is_ascii_alphabetic())
        {
            return false;
        }

        let has_vowel = word.chars().any(|c| Self::is_vowel(c));
        if !has_vowel {
            return false;
        }

        let has_consonant = word.chars().any(|c| Self::is_consonant(c));
        if !has_consonant {
            return false;
        }

        true
    }

    fn is_vowel(c: char) -> bool {
        matches!(c, 'a' | 'e' | 'i' | 'o' | 'u' | 'A' | 'E' | 'I' | 'O' | 'U')
    }

    fn is_consonant(c: char) -> bool {
        c.is_ascii_alphabetic() && !Self::is_vowel(c)
    }
}