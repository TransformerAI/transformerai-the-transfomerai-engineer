
import os
class Runner:
    
    def __init__(self):
        pass
    
    # Find files in directories above that are leetcode problems
    def findLeets(self):
        # go up a directory
        dir = os.path.dirname(os.path.dirname(__file__) + "/../")
        for root, dirs, files in os.walk(dir):
            for file in files:
                if file.endswith(".py"):
                    p = os.path.join(root, file)
                    ap = os.path.abspath(p)
                    filename = os.path.split(ap)[1]
                    filename_noext = os.path.splitext(filename)[0]
                    leet_filename = filename_noext.split('_')
                
                    if len(leet_filename) == 2:
                        if leet_filename[0].isnumeric() and leet_filename[1].isalpha():
                            print(f"Leet-Path: {filename_noext}")
                            print(f"\t{ap}")
            
    def run(self):
        self.findLeets()

if __name__ == "__main__":
    runner = Runner()
    runner.run()