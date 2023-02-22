'''
Created on 22 févr. 2023

@author: pascal
'''
from pattern.romanExpression import RomanExpression

class TenExpression(RomanExpression):
    '''
    classdocs
    '''
    TEN = 10

    def one(self):
        return "X"

    def four(self):
        return "XL"

    def five(self):
        return "L"

    def nine(self):
        return "XC"

    def multiplier(self):
        return self.TEN
