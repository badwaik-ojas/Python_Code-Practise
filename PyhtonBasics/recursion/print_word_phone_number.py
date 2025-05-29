'''
Print Words from a Phone Number

Given a string of digits (e.g., "23"), you need to return all possible letter combinations that the number could represent, based on the old mobile phone keypad layout.

Example Input: "23"
Example Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

📱 Old Mobile Keypad Mapping
plaintext
Copy
Edit
2 -> a b c  
3 -> d e f  
4 -> g h i  
5 -> j k l  
6 -> m n o  
7 -> p q r s  
8 -> t u v  
9 -> w x y z  
1 -> (empty / ignored)
🔑 Note: You won't get 1 or 0 in the input in most coding problems. But if it does come up, ask the interviewer how to handle it.
'''

def return_all_words(digits: str) -> list[str]:
    if not digits:
        return []
    
    # Mapping of digits to letters
    keys = {
        "2": "abc", "3": "def", "4": "ghi",
        "5": "jkl", "6": "mno", "7": "pqrs",
        "8": "tuv", "9": "wxyz"
    }

    small_input = digits[1:]
    small_words = return_all_words(small_input)

    letters = keys[digits[0]]
    result = []

    if not small_words:
        for ch in letters:
            result.append(ch)
    else:
        for i in letters:
            for j in small_words:
                result.append(i +j)

    return result

digits = '234'
print(return_all_words(digits))


