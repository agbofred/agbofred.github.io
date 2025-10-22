""" This model will create evaluator class and also display the PFevaluator values or error messages"""
from mytoken import Token
from scanner import Scanner
from arraystack import ArrayStack

class PFEvaluatorModel(object):
    def evaluate(self, sourceStr):
        self.evaluator = PFEvaluator(Scanner(sourceStr))
        value = self.evaluator.evaluate()
        return value
        
    def format(self, sourceStr):
        normalizeStr = ""
        scanner = Scanner(sourceStr)
        while scanner.hasNext():
            normalizeStr += str(scanner.next()) + " "
        return normalizeStr
        
    
    def evaluationStatus(self):
        return str(self.evaluator)
    
    
class PFEvaluator(object):
    def __init__(self, scanner):
        self.expressionSoFar = ""
        self.operatorStack = ArrayStack()
        self.scanner = scanner
    
    def evaluate(self):
        while self.scanner.hasNext():
            currentToken = self.scanner.next()
            self.expressionSoFar= str(currentToken)+ " "
            if currentToken.getType()== Token.INT:
                self.operatorStack.push(currentToken)
            elif currentToken.isOperator():
                if len(self.operatorStack)<2:
                    raise AttributeError("Too few operands are in the stack")
                t2 = self.operatorStack.pop()
                t1 = self.operatorStack.pop()
                result = Token(self.computeValue(currentToken, t1.getValue(), t2.getValue()))
                self.operatorStack.push(result)
            else:
                raise AttributeError("Unknown Token type")
        if len(self.operatorStack)> 1:
            raise AttributeError("Too many operands on the stack")
        result = self.operatorStack.pop()
        return result.getValue()
                
    def computeValue(self, op, val1, val2):
        result = 0
        theType = op.getType() 
        if theType == Token.PLUS:
            result = val1 + val2
        elif theType == Token.MINUS:
            result = val1 - val2
        elif theType == Token.MUL:
            result = val1 * val2
        elif theType == Token.DIV:
            result = val1 // val2
        elif theType == Token.EXPO:
            result = val1 ** val2
        else:
            raise Exception("Unkown Operator")
        return result
    def __str__(self):
        result = "\n"
        if self.expressionSoFar == "":
            result += "Portion of the expression: none\n"
        else:
            result += "Portion of the expression:" + self.expressionSoFar + "\n"
        if self.operatorStack.isEmpty():
            result += "The stack is empty"
        else:
            result += "Operands on ths stack: "+ str(self.operatorStack)
            
pf = PFEvaluatorModel()
def main():
    while True:
        sourceStr = input("Enter a Postfix Expression:  ")
        if sourceStr.strip() == "":
            break
        fm = pf.format(sourceStr)
        print(fm)
        eval = pf.evaluate(fm)
        print(eval)
        
if __name__ == '__main__':
    main()