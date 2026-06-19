class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        
        # map closing → opening
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for char in s:
            if char in pairs:  # closing bracket
                if not stack:
                    return False
                top = stack.pop()
                if top != pairs[char]:
                    return False
            else:  # opening bracket
                stack.append(char)
        
        return len(stack) == 0
