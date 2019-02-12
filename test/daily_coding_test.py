"""
This is test module for daily coding problem.
This module uses python proboscis libray
to test problem implemented in daily coding problem.py file
"""


# Third party package import
import unittest
from proboscis import test
from proboscis.asserts import assert_equal
from proboscis import TestProgram

# Application package import
from dailycodingproblem.list_excercises import DailyCoding


@test
def test_product_of_array_except_current_index():
    input_array = [[3, 2, 1], [1, 1, 1]]
    expected = [[2, 3, 6], [1, 1, 1]]

    for actual_array, expected_array in zip(input_array, expected):
        product_array = DailyCoding.product_of_array_except_current_index(actual_array)
        assert_equal(expected_array, product_array)


TestProgram().run_and_exit()

