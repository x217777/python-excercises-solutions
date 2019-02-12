"""
This module holds the list type
exercises from daily coding site
"""


class DailyCoding:

    def __int__(self):
        pass

    @staticmethod
    def product_of_array_except_current_index(array):
        """
        ## Question - This problem was asked by Uber.

                Given an array of integers, return a new array such that
                each element at index i of the new array is the product of all the numbers
                in the original array except the one at i.

                For example:
                If our input is [3, 2, 1], the expected output would be [2, 3, 6].

        ## Solution Analysis about problem statement.
                # Given  -> Integer array [3, 2, 1]
                # When   -> multiply each element of array except current index
                # Then   ->  [2, 3, 6]
                # Task   ->
                    1. Need array index and value,                   solution -> enumerate function
                    2. At current index, grab other index and value, solution -> nested for loop with if condition
                    3. perform mul of other index element,           solution -> temp var to hold mul val at second loop
                    4. Can't update same array,                      solution -> create new temp array
                    5. append mul value to new array                 solution -> append new val to new array
                    6. print original array and new array            solution -> print both arrays at end

        """
        product_array = []

        for index, value in enumerate(array):
            mul_total = 1

            for index_, value_ in enumerate(array):
                if index != index_:
                    mul_total *= value_

            product_array.append(mul_total)

        print("\nOriginal array is: -> ", end='')
        print(array)
        print("Product array is: -> ", end='')
        print(product_array)
        return product_array

