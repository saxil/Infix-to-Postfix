##def inFixToPostFix():
##    inFix = '3*(x+1)-2/2'
##    postFix = ''
##    s = Stack()
##    for c in inFix:
##        # if elif chain for anything that c can be
##        if c in "0123456789x":
##            postFix += c
##        elif c in "+-":
##            if s.isEmpty():
##                s.push(c)
##            elif s.top() =='(':
##                s.push(c)
##        elif c in "*/":
##            if s.isEmpty():
##                s.push(c)
##            elif s.top() in "+-(":
##                s.push(c)
##        elif c == "(":
##            s.push(c)
##        elif c == ")":
##            while s.top() is not '(':
##                postFix += s.pop()
##            s.pop()
##        else:
##            print("Error")
##    print(postFix)
##    return postFix
##inFixToPostFix()
def toPostfix(infix):
    stack = []
    postfix = ''

    for c in infix:
        if isOperand(c):
            postfix += c
        else:
            if isLeftParenthesis(c):
                stack.append(c)
            elif isRightParenthesis(c):
                operator = stack.pop()
                while not isLeftParenthesis(operator):
                    postfix += operator
                    operator = stack.pop()              
            else:
                while (not isEmpty(stack)) and hasLessOrEqualPriority(c,peek(stack)):
                    postfix += stack.pop()
                stack.append(c)

    while (not isEmpty(stack)):
        postfix += stack.pop()
    return postfix
toPostfix()
