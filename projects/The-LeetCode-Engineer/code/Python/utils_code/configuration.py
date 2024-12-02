

import json


class Configuration():
    DEFAULT_HANDLE_CONSTRAINTS = False

    def __init__(self):
        self.handle_constraints = None 

    def to_dict(self) -> dict:
        d = {
            "handle_constraints": self.handle_constraints
        }
    
    @staticmethod
    def from_dict(d: dict) -> 'Configuration':
        c = Configuration()
        c.handle_constraints = d["handle_constraints"]
        return c
        
    def to_json(self) -> str:
        d = self.to_dict()
        json_str = json.dumps(d, indent=4)
        return json_str
    
    @staticmethod
    def from_json(json_str: str) -> 'Configuration':
        d = json.loads(json_str)
        c = Configuration.from_dict(d)
        return c
    
    @staticmethod
    def inst() -> 'Configuration':
        inst = Configuration.read_constraints()
        if inst is None:
            inst = Configuration.default_constraints()
        return inst
        
    @staticmethod
    def read_constraints() -> 'Configuration':
        # read from file configuration....
        with open("_leetcode_configuration_py.json") as f:
            json_contents = f.read()
            c = Configuration.from_json(json_contents)
            return c

    @staticmethod
    def default_constraints() -> 'Configuration':
        c = Configuration()
        c.handle_constraints = Configuration.DEFAULT_HANDLE_CONSTRAINTS
        return c