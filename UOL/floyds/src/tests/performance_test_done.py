"""
This module contains a simple performance test which
compares the recursive version of Floyds algorithm with the
imperative version
"""

import sys
sys.path.append('../')
from recursion.recursion_done import *
from iterative.iterative_floyd import *
from time import process_time

def performance_test(function_handle):
    """
    A function that performs a simple performance test
    function_handle -> The function which is being tested. 
                       It must take no parameters

    Please complete this function
    """
    start_time = process_time()  
    function_handle()  
    end_time = process_time()  
    execution_time = end_time - start_time  
    message = "Execution time: {} seconds".format(execution_time)
    print(message)
    
    def main():
        pass
    
    def iterative_floyd():
        pass
    
print ("Recursion Test Time")
performance_test(main)

print ("Iterative Test Time")
performance_test(iterative_floyd)
