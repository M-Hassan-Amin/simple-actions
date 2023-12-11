from base_action import BaseAction

class AddNumbersAction(BaseAction):
    def run(self, num1, num2):
        return num1 + num2
