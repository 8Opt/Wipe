class Node:
    def __init__(self, name, **kwargs):
        self.name = name

    def run (self, input, **kwargs):
        raise NotImplementedError