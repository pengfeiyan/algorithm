# coding=utf-8
import math
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        if not tokens:
            return None
        else:
            for i in tokens:
                if i == '+' and len(stack)>=2:
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(num1+num2)
                elif i == '-' and len(stack)>=2:
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(num2 - num1)
                elif i == '*' and len(stack)>=2:
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(num1 * num2)
                elif i == '/' and len(stack)>=2:
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(int(float(num2)/num1))
                else:
                    stack.append(int(i))
            return stack.pop()
sol = Solution()
arr = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(sol.evalRPN(arr))
