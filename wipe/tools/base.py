class Node:
    def __init__(self, name, api_key, **kwargs):
        self.name = name
        self.api_key = api_key

    def run (self, input, **kwargs):
        raise NotImplementedError