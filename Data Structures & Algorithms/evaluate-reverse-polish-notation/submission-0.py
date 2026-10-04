class Solution:
   

    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for token in tokens:
            if token not in {"+","-","*","/"}:
                stack.append(int(token))
                continue
            b=stack.pop()
            a=stack.pop()
            if token=="+":
                result=a+b
            elif token == "-":
                result = a - b
            elif token == "*":
                result = a * b
            else:
                # int(a / b) truncates toward zero
                result = int(a / b)
            
            stack.append(result)
        return stack[0]