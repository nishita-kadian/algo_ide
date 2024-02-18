from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Return the concatenation of the nums list with itself
        return nums + nums

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    with open("test_cases.txt", "r") as file:
        for line in file:
            # Convert the line to a list of integers
            nums = [int(x) for x in line.strip().split(",")]
    concatenated_nums = solution.getConcatenation(nums)
    print(concatenated_nums)
