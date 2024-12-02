from typing import Callable
from utils_code.configuration import Configuration

def predicate(code: Callable[[], bool] = None, positive_condition: str = None, negative_condition: str = None):
    if code == None:
        return
    if not Configuration.inst().handle_constraints:
        return
    results = code()
    if not results:
        raise Exception(negative_condition)
    if positive_condition != None and results:
        raise Exception(positive_condition)
