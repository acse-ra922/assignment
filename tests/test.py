import pytest
from assignment_solution.dist_function import distance

s = "red yellow blue"
parameters = "red, blue"
res = 2

def test_1():
    assert distance(s,parameters)==res


string = "red pink yellow green blue"
params = "red, blue"
result = 4

def test_2():
    assert distance(string,params)==result
