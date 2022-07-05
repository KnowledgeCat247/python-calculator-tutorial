class basicMath:
    def __init__(self, name):
        self.name = name
    
    def add(self, a, b):
        #What if I input a float instead of an integer?
        return (int(a) + int(b))
    
    def subtract(self,a, b):
        #What if I input a float instead of an integer?
        return (int(a) - int(b))
    
    def divide(self, a, b):
        first = (float(a) / float(b))
        number = []
        string = str(first)
        for i in string:
            number.append(i)
        
        if number[0] == '0':
            return first
        elif number[0] != '0':
            if number[1] == '0' or number[1] == '.' or number[1] != '0':
                if number[2] == '.':
                   if number[3] == '0':
                      return int(first)
                   elif number[3] != '0':
                    return first
                elif number[2] == '0':
                    return int(first)
                elif number[2] != '0':
                    return first

        
    
    def multiply(self,a,b):
        return (float(a) * float(b))

#What would a Square Root Look Like?
class advancedMath:
    def _init_(self, name):
        self.name = name