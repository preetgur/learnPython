""" 
Authour : Gurpreet Singh
Date : 18 jan 2020
Purpose : How to perform unit testing.


########## Always save the name of test file with prefix "test_" and the function should also be in same prefis " def test_fxn():"

############ How to Run Test file
cmd / gitbash : python -m pytest
cmd /gitbash : py.test
cmd / gitbash : py.tes -v

############
First import the file where you want to execute unit test 

#########
Create functino staring with the prefix "test_"
Inside the test fxn call the function of imported file

########
assert : is used to match expected output vs actual output

"""


"""
############ How To Skip tests
>> First import pytest : import pytest

>> Use Decorator to the function to whom you dont want to execute the test case :

@pytest.mark.skip(reason="give any reason")

#### Skip test if it meets some condition [skipif]
@pytest.mark.skipif(reason="give any reason")


>> In order to see the reason type

pytest -v -rxs

############ Selectively run test using their name
pytest -k multiply  : it runs all the function that contains multiply as substring

pytest -k multiply -v : to show which test is exceuted

############  custom markers : creating categories of the test

for exmaple : If you want that test run according to operating system 

>>> First import :
import pytest

>>> use Decorator

@pytest.mark.windows  ["windows" is name of categories]
#There should be any name in palce of "windows" it is just the name of mark

@pytest.mark.mac


>>>> run 

pytest -m "catergorie name" -v

pytest -m mac -v
pytest -m window -v

>>>> reverse

pytest -m "not windows" -v
"""
import codebasic_testing
import pytest

a = 10
b = 20
# Unit Test one

# @pytest.mark.skip(reason='I dont want to run this test at the moment')
@pytest.mark.skipif(a > 8 and b<21 , reason='condition of a and b is matched ')

def test_calc_total():
    total = codebasic_testing.calc_total(4,5)
    assert total == 9   # excepted result

# Unit Test second
def test_calc_multiply():
    total = codebasic_testing.calc_multiply(4,5)
    assert total == 20   # excepted result


def test_dummy():
    assert True

@pytest.mark.windows
def test_windows_1():
    assert True    

@pytest.mark.windows
def test_windows_2():
    assert True        

@pytest.mark.mac
def test_mac_1():
    assert True    

@pytest.mark.mac
def test_mac_2():
    assert True    