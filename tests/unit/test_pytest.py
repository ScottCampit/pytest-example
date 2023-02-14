import pytest

# function we want to test
def add_one(num:int):
    return num + 1

# test function
def test_answer_pass():
    assert add_one(4) == 5

# This xfail decorator indicates that the function is expected fail - more on that later.
@pytest.mark.xfail
def test_answer_fail():
    assert add_one(4) == 6