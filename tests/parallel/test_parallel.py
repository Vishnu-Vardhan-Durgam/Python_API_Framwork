# 2 ways

import pytest


def test_1():
    # need to write full code -- this is just to show a sample
    assert True


def test_2():
    assert 1 == 1


def test_3():
    assert False


def test_4():
    assert True

# pip install pytest-xdist --> Need to install this to run all testcases at once
#  pytest -n auto parallel/test_parallel.py ---> to run test cases


# if you want  to run your Test case parallel
# 1. Your Testcase should be atomic -->1 testcase per method or file
# 2. They should not depend on each other
# 3. They depend --> make them a separate testcase
