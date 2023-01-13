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

s1 = "red green white violet red blue"
param = "red, blue"
r = 1

def test_3():
    assert distance(s1,param)==r


s2 = "red red blue red"
p = "red, blue"
r1 = 1

def test_4():
    assert distance(s2,p)==r1


s3 = "yellow yellow blue yellow yellow red"
p3 = "red, blue"
r3 = 3

def test_5():
    assert distance(s3,p3)==r3
