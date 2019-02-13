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
        ## Problem #2 - This problem was asked by Uber.

                Given an array of integers, return a new array such that
                each element at index i of the new array is the product of all the numbers
                in the original array except the one at i.

                For example:
                If our input is [3, 2, 1], the expected output would be [2, 3, 6].

        ## Problem Analysis -
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

    @staticmethod
    def is_any_two_numbers_add_up_to_k(lst, k):
        """
        ## Problem #1 - This problem was asked by Google.

            Given a list of numbers and a number k,
            return whether any two numbers from the list add up to k.
            For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17

        ## Problem Analysis -
           # Given -> number list
           # And   -> number k
           # When  -> any two numbers add up to k
           # Then  -> return True
           # Else  -> return False
           # Task  ->
                1. needs to loop through numbers to get index and numbers  solution -> for loop with enumerate function
                2. at current index get the list of rest numbers           solution -> get nested for loop
                3. rest number list should have (start, end)          solution -> range(current_index + 1, len(lst) + 1)
                4. need to avoid list outofbound error                Solution -> 2nd last ele don't enter into 2nd loop
                5. check two numbers add up to k                      solution -> current index ele + next index ele
                6. return True if adds up                             solution -> return True
                7. else return False                                  solution -> return False

        :return: boolean True or False
        """
        for index, first_element in enumerate(lst):
            if index != (len(lst) - 1):
                for i, second_element in enumerate(lst[index+1:]):
                    if first_element + second_element == k:
                        return True
                        break

            elif first_element + lst[-1] == k:
                return True
                break

            else:
                return False



