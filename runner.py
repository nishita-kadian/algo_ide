from solution import Solution as our_solution
from subprocess import Popen, PIPE, STDOUT
import ast
import time

class Runner:
    def __init__(self):
        pass

    def read_testcases(self):
        with open("test_cases.txt", "r") as file:
            testcases = file.readlines()
        processed_testcases = []
        for testcase in testcases:
            processed_testcases.append([list(map(int, testcase.split(' '))), testcase])
        return processed_testcases

    def compare(self, custom_testcase):
        pass

    def read_custom_testcases(self):
        with open("custom_testcases.txt", 'r') as file:
            testcases = file.readlines()
        processed_testcases = []
        for testcase in testcases:
            processed_testcases.append([list(map(int, testcase.split(' '))), testcase])
        return processed_testcases
    
    def run(self, custom):
        """
        Reference: https://stackoverflow.com/a/51950538
        """
        if custom:
            testcases = self.read_custom_testcases()
        else:
            testcases = self.read_testcases()
        results = []
        user_results = []
        correct_results = []
        for testcase in testcases:
            correct_result = our_solution().getConcatenation(nums=testcase[0])
            user_subprocess = Popen(["python", "snippets.py"], stdout=PIPE, stdin=PIPE, stderr=PIPE, text=True)
            
            time_to_run = time.time()
            user_result = user_subprocess.communicate(input=testcase[1])[0]
            processed = list(map(int, ast.literal_eval(user_result)))
            
            time_to_run = time.time() - time_to_run

            user_results.append(user_result)
            correct_results.append(correct_result)
            if time_to_run > 5:
                results.append('TIME LIMIT EXCEEDED') 
            elif processed == correct_result:
                results.append('ACCEPTED')
            else:
                results.append('WRONG ANSWER')
        # all_results.append((user_result, results))
        zip_result = zip(user_results, correct_results, results)
        return zip_result
        