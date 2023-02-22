'''
Created on 22 févr. 2023

@author: pascal
'''

import logging
from pattern.romanContext import RomanContext
from pattern.oneExpression import OneExpression
from pattern.tenExpression import TenExpression
from pattern.hundredExpression import HundredExpression
from pattern.thousandExpression import ThousandExpression

class RomanInterpreter(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.result = 0

    def compute(self, roman_number):
        context = RomanContext(roman_number)

        roman_tree = [
            ThousandExpression(),
            HundredExpression(),
            TenExpression(),
            OneExpression()
        ]

        # Interpret
        for expression in roman_tree:
            expression.interpret(context)

        logging.info(f"{roman_number} = {context.get_output()}")
        self.set_result(context.get_output())

    def get_result(self):
        return self.result

    def set_result(self, result):
        self.result = result
