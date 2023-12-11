from base_action import BaseAction

class ConcatenateStringsAction(BaseAction):
    def run(self, string1, string2):
        return string1 + string2
