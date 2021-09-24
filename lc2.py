#https://leetcode.com/problems/valid-parentheses/submissions/

# constraint questions (INPUT / OUTPUT)
# what types of chars?
# empty string?
# how long string?
# empty spaces?
# return type?

class Solution:
    def isValid(self, s: str) -> bool:            
        # initialise new stack
        stack = []
        
        # if the char is one of the values in this list, push it onto the stack
        for c in s:
            if c in '({[': 
                stack.append(c)
            # if the stack is empty and the char is a closing bracket, that means we should return false    
            elif len(stack) == 0:
                return False
            else: 
                opening = stack.pop()
                # if it's a closing bracket, pop the stack to see if it's matching bracket is there. 
                # If it is not, return False
                # if it is, keep going, until the list is empty
                closing = c
                if opening == '(' and closing == ")":
                    continue 
                elif opening == "{" and closing == "}":
                    continue
                elif opening == "[" and closing == "]":
                    continue
                else:
                    return False 
        
        # return True if the stack is empty (that means the string was balanced)
        return not stack
