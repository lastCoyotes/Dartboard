###################
# A basic example of how to write a unit test. Note that the class name here starts with the word "test".
# This allows pytest to pick this up as a test class.
###################
import pytest


##
# This is another basic test method.
def test_sanity_check1():
    assert 1 != 2
