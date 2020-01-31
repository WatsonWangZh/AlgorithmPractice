# Validate if a given string can be interpreted as a decimal number.

# Some examples:
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
# " -90e3   " => true
# " 1e" => false
# "e3" => false
# " 6e-1" => true
# " 99e2.5 " => false
# "53.5e93" => true
# " --6 " => false
# "-+3" => false
# "95a54e53" => false

# Note: It is intended for the problem statement to be ambiguous. 
# You should gather all requirements up front before implementing one. 
# However, here is a list of characters that can be in a valid decimal number:
# Numbers 0-9
# Exponent - "e"
# Positive/negative sign - "+"/"-"
# Decimal point - "."
# Of course, the context of these characters also matters in the input.

# Update (2015-02-10):
# The signature of the C++ function had been updated. 
# If you still see your function signature accepts a const char * argument, 
# please click the reload button to reset your code definition.

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # M1. 正则表达式
        import re
        p = re.compile(r'^[+-]?(\d+[.]?|\d*[.]\d+)(e[+-]?\d+)?$')
        if len(s.strip()) == 0:
            return False
        m = p.match(s.strip())
        return m != None

        # M2. 模拟 Case by Case
        if not s:
            return False
        s = s.strip() # strip the heading and tailing spaces of the string
        res = signs = eE = dot = False
        for c in s:
            if '0' <= c <= '9': # current is number
                print('f')
                res = True # seen number
                signs = True # no more signs 
            elif c == '.' and not dot: # current is dot and not seen dot before
                print('u')
                dot = True # no more dots
                sign = True # no more signs
            elif (c == 'e' or c == 'E') and (not eE) and res: 
                print('c')
                # current is e and not seen e before, seen number before 
                res = False # have to see number after e
                signs = False # can see more signs
                dot = True # no more dot
                eE = True # no more e
            elif (c == '+' or c == '-') and not res and not signs and ((not dot) or eE):
                print('k')
                # current is sign and not seen number before, not seen sign before
                signs = True # no more signs
            else:
                return False
        return res