'''
Created on 22 févr. 2023

@author: pascal
'''

from pattern.romanExpression import RomanExpression

class ThousandExpression(RomanExpression):
    '''
    classdocs
    '''
    THOUSAND = 1000

    def one(self):
        return "M"

    def four(self):
        return " "

    def five(self):
        return " "

    def nine(self):
        return " "

    def multiplier(self):
        return self.THOUSAND