# Two moving pointers, regardless of directions, moving dependently or independently;
# A function that utilizes the entries referenced by the two pointers, which relates to the answer in a way;
# An easy way of deciding which pointer to move;
# A way to process the array when the pointers are moved.
#
# 
# Two Pointers Technique - From Google
# A "two pointers same direction" technique is particularly useful for 
# problems where you need to analyze a "sliding window" or sub-array within 
# a larger data structure, like an array, where both pointers move from the 
# same starting point and progress through the data in the same direction, 
# allowing you to efficiently track and update the window based on specific
# conditions; this is often seen in problems like finding the maximum 
# subarray sum or merging sorted arrays. [1, 2, 3]  
# Key points about using two pointers in the same direction: [1, 4, 5]  
#
# • Sliding window concept: This is the most common application, where the window 
# size can dynamically adjust based on the problem's requirements while both pointers 
# move forward. [1, 4, 5]  
# • Maintaining relative positions: By keeping both pointers moving in the same 
# direction, you can easily compare elements within the current window and make 
# decisions based on their relative positions. [1, 2, 3]  
# • Optimized time complexity: Compared to nested loops, using two pointers in the 
# same direction often leads to a linear time complexity, making it very efficient 
# for large datasets. [1, 2, 6]  
#
# Example scenarios where "two pointers same direction" might be used: [1, 2, 3] 
# • Find the longest substring with at most k distinct characters: Both pointers move through the string, updating the window size as needed to maintain the constraint on distinct characters. [1, 2, 3]  
# • Merge two sorted arrays: One pointer iterates through each sorted array, comparing elements and adding them to the result in sorted order. [1, 5, 7]  
# • Find the maximum subarray sum: A sliding window is used to track the current sum as both pointers move through the array. [1, 4, 5]  



# [1] https://dev.to/charlesamakoye/dissecting-the-two-pointer-technique-2lb4
# [2] https://hyperskill.org/learn/step/41495
# [3] https://medium.com/@johnnyJK/data-structures-and-algorithms-907a63d691c1
# [4] https://algo.monster/problems/two_pointers_intro
# [5] https://www.codecademy.com/article/the-two-pointer-technique-in-a-linked-list-swift
# [6] https://medium.com/@elfrmkr98/mastering-problem-solving-two-pointers-technique-23dafb17e90b
# [7] https://medium.com/@Prachi-Jamdade/two-pointers-algorithm-most-efficient-technique-to-optimize-runtime-fbbbf24a3891


from typing import Callable, Any, List

### 
# Problems to Solve with TwoPointers
# finding the maximum subarray sum 
# merging sorted arrays
# 
# find palindrome
# find pair-num sum to target-num --- Given a sorted array of unique integers and a target 
#   integer, return true if there exists a pair of numbers that sum to target, false otherwise. 
#   This problem is similar to Two Sum.
# fast pointer, slow pointer, detect cycle in linked list
# Extended: 
#    - Alternate movement
#    - Multiple pointers

def twoSum(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        if arr[left] + arr[right] == target:
            return [left, right]
        left += 1
        right -= 1
arr = [1, 3, 6, 7, 9]
goal = 9
results = twoSum(arr, goal)
print(results)
class TwoPointers():     
    def __init__(self, collection: List, functor: Callable[[Any], Any], mover: Callable, processor: Callable):
        self.left = None
        self.right = None
        
        self.collection = collection
        self.functor = functor
        self.mover = mover
        self.processor = processor
        
        
    def run_sameDirection(self):
        left = 0
        right = 1
        
        while right < len(self.collection):
            self.collection[left], self.collection[right]
            
        
        
    def run_oppositeDirection(self):
        pass
        
    def run(self):
        left = 0
        right = len(self.collection) - 1
        
        
        
    # def run(self):
    #     left = 0
    #     right = len(self.collection) - 1
        
    #     while left < right:
    #         self.processor(self.functor(self.collection[left]), self.functor(self.collection[right]))
    #         self.mover(left, right)
            
    #     return self.processor
    
    
    