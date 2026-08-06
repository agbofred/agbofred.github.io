"""Token program for processing expressions."""
class Token:
    
    UNKNOWN = 0 # Unknown
    INT     = 4 #Integer
    MINUS   = 5 # minus operator
    PLUS    = 6 # Plus Operator
    MUL     = 7 # Multiply operator
    DIV     = 8 #divid operator
    EXPO    = 9 # Exponent operator
    LPAR    = 10 # Left Par operator
    RPAR    = 11 # Right Par operator
    FIRST_OP = 5 # First operator code
    
    # Contrcutor
    def __init__(self, value):
        if type(value) == int:
            self.type = Token.INT
        else:
            self.type = self.makeType(value)
        self.value = value
            
            
    def makeType(self, ch):
        if ch == "*": return Token.MUL
        elif ch == "/": return Token.DIV
        elif ch == '+': return Token.PLUS
        elif ch == '-': return Token.MINUS
        elif ch == '^': return Token.EXPO
        elif ch == '(': return Token.LPAR
        elif ch == ')': return Token.RPAR
        else:           return Token.UNKNOWN
    
    def isOperator(self):
        return self.type >=Token.FIRST_OP
    
    def __str__(self):
        return str(self.value)
    
    def getType(self):
        return self.type
    
    def getValue(self):
        return self.value
    
    def getPrecedence(self):
        """returns the precedence level"""
        myType = self.type
        if myType ==Token.EXPO: return 3
        if myType in (Token.MUL, Token.DIV) : return 2
        if myType in (Token.PLUS, Token.MINUS) : return 1
        else: return 0
        
def main():
    # Run some testers here 
    plus = Token("+")
    minus = Token("-")
    mul = Token("*")
    div = Token("/")
    expo = Token("^")
    unknown = Token("#")
    anint = Token(34)
    
    print(plus, minus, mul, div, expo, unknown, anint)
    

if __name__ == '__main__':
    main()        