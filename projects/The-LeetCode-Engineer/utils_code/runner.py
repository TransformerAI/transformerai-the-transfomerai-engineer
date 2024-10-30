
import os
class Runner:
    def __init__(self):
        pass
    
    # Find files in directories above that are leetcode problems
    def findLeets(self):
        # go up a directory
        dir = os.path.dirname(os.path.dirname(__file__))
        # go up another directory
        dir = os.path.dirname(dir)
    
    def run(self):
        print("Running the runner!")

if __name__ == "__main__":
    runner = Runner()
    runner.run()