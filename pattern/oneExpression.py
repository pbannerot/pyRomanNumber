'''
Created on 22 févr. 2023

@author: pascal
'''

from pattern.romanExpression import RomanExpression

class OneExpression(RomanExpression):
    ONE = 1

    def one(self):
        return "I"

    def four(self):
        return "IV"

    def five(self):
        return "V"

    def nine(self):
        return "IX"

    def multiplier(self):
        return self.ONE