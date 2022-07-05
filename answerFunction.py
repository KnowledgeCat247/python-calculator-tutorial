from mathClasses import basicMath

operations = basicMath("operations")

#How would we input a square root? Ex: v(x) or sqrt(x)?
def answerLoop(n1, op, n2):
    if op == "+":
       return operations.add(n1, n2)
    elif op == "-":
        return operations.sub(n1, n2)
    elif op == "*":
         return operations.multiply(n1, n2)
    elif op == "/":
       return  operations.divide(n1, n2)

    
    
