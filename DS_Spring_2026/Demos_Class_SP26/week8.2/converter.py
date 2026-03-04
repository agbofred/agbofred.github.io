"""This module converts from infix to postfix"""

from scanner import Scanner
from arraystack import ArrayStack
from mytoken import Token

class IFToPTConverter(object):
    
    #. contrsutor 
    def __init__(self, scanner):
        self.scanner = scanner
        self.expressionSoFar = ""
        self.stack = ArrayStack()
        
    def convert(self):
        postfix =[]
        while self.scanner.hasNext():
            currentToken = self.scanner.next()
            self.expressionSoFar = str(currentToken)+ " "
            if currentToken.getType() == Token.UNKNOWN:
                raise AttributeError("Unrecognized symbol")
            if currentToken.getType() ==Token.INT:
                postfix.append(currentToken)
            elif currentToken.getType() == Token.LPAR:
                self.stack.push(currentToken)
            elif currentToken.getType() == Token.RPAR:
                topOperator = self.stack.pop()
                while topOperator.getType() != Token.LPAR:
                    postfix.append(topOperator)
                    topOperator = self.stack.pop()
            else:
                while not self.stack.isEmpty() and \
                    currentToken.getType() != Token.EXPO and self.stack.peek().getPrecedence() >= currentToken.getPrecedence():
                    postfix.append(self.stack.pop())
                self.stack.push(currentToken)
        while not self.stack.isEmpty():
            postfix.append(self.stack.pop())
        return postfix
    
    def __str__(self):
        result = "\n"
        if self.expressionSoFar == "":
            result += "Portion of expression processed: none\n"
        else: 
            result += "Portion of expression processed: " + \
                    self.expressionSoFar + "\n"
        if self.stack.isEmpty():
            result += "The stack is empty"
        else:
            result += "Operators on the stack          : " + \
                        str(self.stack)
        return result
        pass

    def conversionStatus(self):
        return str(self)
        
def main():
    while True:
        sourceStr = input("Enter an infix expression:   ")
        if sourceStr.strip() =="":
            break
        else:
            try:
                converter = IFToPTConverter(Scanner(sourceStr))
                postfix = converter.convert()
                print("Postfix: ", end = " ")
                for token in postfix:
                    print(token, end =" ")
                print()
            except Exception as e:
                print(e)
                
if __name__ == '__main__':
    main()