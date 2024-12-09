

def assertEq(input = None, expectedOut = None, actualOut = None):
    try:
        assert expectedOut == actualOut
        print(f"expected: {expectedOut} == actual: {actualOut}")
    except AssertionError:
        print(f"Assertion failed for input {input or "n/a"}: expected {expectedOut or "n/a"}, got {actualOut or "n/a"}")
