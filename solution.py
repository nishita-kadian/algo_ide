from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Return the concatenation of the nums list with itself
        return nums + nums

# Example usage:
# if __name__ == "__main__":
    # solution = Solution()
#     custom_test_cases = None

#     if request.method == 'POST':
#         custom_test_cases = request.POST.get("input_test_cases")

#     if custom_test_cases:
#          nums = [int(x) for x in custom_test_cases.strip().split(",")]
#     else:
#         with open("test_cases.txt", "r") as file:
#             for line in file:
#                 # Convert the line to a list of integers
#                 nums = [int(x) for x in line.strip().split(",")]
    
#     concatenated_nums = solution.getConcatenation(nums)
#     print(concatenated_nums)

# def submit_testcases(request):
#     if request.method == 'POST':
#         input_testcases = request.POST.get('input_testcases')
#         if input_testcases:
#             # Parse the input test cases into a list of integers
#             try:
#                 nums = [int(num.strip()) for num in input_testcases.split(',')]
#                 solution = Solution()
#                 concatenated_nums = solution.getConcatenation(nums)
#                 return render(request, 'accounts/dashboard.html', {'concatenated_nums': concatenated_nums})
#             except ValueError:
#                 return HttpResponse("Invalid input format. Please provide comma-separated integers.")
#         else:
#             return HttpResponse("No input test cases provided.")
#     else:
#         return HttpResponse("Invalid request method.")

