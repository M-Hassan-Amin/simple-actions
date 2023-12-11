class BaseAction:
    def run(self, **params):
        raise NotImplementedError("Subclasses must implement this method")
