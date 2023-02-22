'''
Created on 22 févr. 2023

@author: pascal
'''

class RomanContext(object):
    '''
    classdocs
    '''

    def __init__(self, input_str):
        '''
        Constructor
        '''
        self.input = input_str
        self.output = 0


    def get_input(self):
        return self.input

    def set_input(self, input_str):
        self.input = input_str

    def get_output(self):
        return self.output

    def set_output(self, output):
        self.output = output
