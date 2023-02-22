'''
Created on 22 févr. 2023

@author: pascal
'''

from pattern.romanExpression import RomanExpression

class HundredExpression(RomanExpression):
    '''
    classdocs
    '''
    HUNDRED = 100

    def one(self):
        return 'C'

    def four(self):
        return 'CD'

    def five(self):
        return 'D'

    def nine(self):
        return 'CM'

    def multiplier(self):
        return self.HUNDRED