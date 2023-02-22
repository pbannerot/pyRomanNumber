'''
Created on 22 févr. 2023

@author: pascal
'''

class RomanExpression(object):
    '''
    classdocs
    '''

    def interpret(self, context):
        if len(context.get_input()) == 0:
            return

        if context.get_input().startswith(self.nine()):
            context.set_output(context.get_output() + (9 * self.multiplier()))
            context.set_input(context.get_input()[2:])
        elif context.get_input().startswith(self.four()):
            context.set_output(context.get_output() + (4 * self.multiplier()))
            context.set_input(context.get_input()[2:])
        elif context.get_input().startswith(self.five()):
            context.set_output(context.get_output() + (5 * self.multiplier()))
            context.set_input(context.get_input()[1:])

        while context.get_input().startswith(self.one()):
            context.set_output(context.get_output() + (1 * self.multiplier()))
            context.set_input(context.get_input()[1:])

    def one(self):
        pass

    def four(self):
        pass

    def five(self):
        pass

    def nine(self):
        pass

    def multiplier(self):
        pass
