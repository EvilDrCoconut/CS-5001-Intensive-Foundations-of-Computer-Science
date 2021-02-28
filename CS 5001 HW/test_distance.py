'''
CS 5001
Fall 2019
HW 2 - Euclidean Distance Testing
As I was writing down the functions for test_manhattan and test_absolute, I had forgotten to change
actual from eculidean to absolute and manhattan. Instead, I rewrote euclidean and attempted to run
the test from expected values (which were obtained due to testing on the functions program). This
caused all values to fail, and required me to reinspect through the traceback log as to why.
'''
from defining_functions import absolute
from defining_functions import manhattan
from defining_functions import euclidean

EPSILON = .0001

def test_euclidean():
    ''' function test_euclidean
        Input: none
        Returns: int, # of tests that failed
        Does: tests a few different inputs on the euclidean
              distance function, makes sure each distance value
              is as-expected.
    '''
        
    num_failed = 0

    # Test 1: (0, 0), (0, 0)
    # Distance should be 0
    actual = euclidean(0, 0, 0, 0)
    expected = 0.0
    print('Input (0, 0), (0, 0).\n'
          'Expected result', expected,
          'and actual result =', actual)
    if absolute(actual - expected) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed += 1
    
    # Test 2: (2, -1), (-2, 2).
    # Distance is 5.0
    actual = euclidean(2, -1, -2, 2)
    expected = 5.0
    print('Input (2, -1), (-2, 2).\n'
          'Expected result', expected,
          'and actual result =', actual)
    if absolute(actual - expected) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed += 1


    # Test 3: (1, 1), (0, 1)
    # Distance is 1.0
    actual = euclidean(1, 1, 0, 1)
    expected = 1.0
    print('Input (1, 1), (0, 1).\n'
          'Expected result', expected,
          'and actual result =', actual)
    if absolute(actual - expected) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed += 1

    # Test 4: (-5.2, 3.8), (-13.4, 0.2)
    # Distance is 8.955445
    actual = euclidean(-5.2, 3.8, -13.4, 0.2)
    expected = 8.955445
    print('Input (-5.2, 3.8), (-13.4, 0.2).\n'
          'Expected result', expected,
          'and actual result =', actual)
    if absolute(actual - expected) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :(\n')
        num_failed += 1

    return num_failed

def test_absolute():
    ''' function test_absolute
        Input: none
        Returns: int, # of tests that failed
        Does: tests a few different inputs on the absolute
        function, makes sure each value equals what's expected.
    '''
        
    num_failed2 = 0

    # Test 1: (3)
    # Value should be 3
    actual = absolute(3)
    expected = 3.0
    print('Input (3).\n'
          'Expected result', expected,
          'and actual result =', actual)
    if absolute(actual - expected) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed2 += 1
    
    # Test 2: (0).
    # Value is 0
    actual = absolute(0)
    expected = 0
    print('Input (0).\n'
          'Expected result', expected,
          'and actual result =', actual)
    if absolute(actual - expected) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed2 += 1


    # Test 3: (-7)
    # Value is 7
    actual = absolute(-7)
    expected = 7.0
    print('Input (-7).\n'
          'Expected result', expected,
          'and actual result =', actual)
    if absolute(actual - expected) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed2 += 1

    # Test 4: (-4.2)
    # Value is 4.2
    actual = absolute(-4.2)
    expected = 4.2
    print('Input (-4.2).\n'
          'Expected result', expected,
          'and actual result =', actual)
    if absolute(actual - expected) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :(\n')
        num_failed2 += 1

    return num_failed2

def test_manhattan():
    ''' function test_manhattan
        Input: none
        Returns: int, # of tests that failed
        Does: tests a few different inputs on the manhattan
        distance function, makes sure each distance value
        is as-expected.
    '''
        
    num_failed3 = 0

    # Test 1: (0, 0), (0, 0)
    # Distance should be 0
    actual = manhattan(0, 0, 0, 0)
    expected = 0.0
    print('Input (0, 0), (0, 0).\n'
          'Expected result', expected,
          'and actual result =', actual)
    if absolute(actual - expected) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed3 += 1
    
    # Test 2: (3, 3), (6, 6).
    # Distance is 6.0
    actual = manhattan(3, 3, 6, 6)
    expected = 6.0
    print('Input (3, 3), (6, 6).\n'
          'Expected result', expected,
          'and actual result =', actual)
    if absolute(actual - expected) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed3 += 1


    # Test 3: (-2, 4), (0, -7)
    # Distance is 9.0
    actual = manhattan(-2, 4, 0, -7)
    expected = 9.0
    print('Input (-2, 4), (0, -7).\n'
          'Expected result', expected,
          'and actual result =', actual)
    if absolute(actual - expected) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed3 += 1

    # Test 4: (-4.5, 2.3), (7.6, -0.2)
    # Distance is 8.955445
    actual = manhattan(-4.5, 2.3, 7.6, -0.2)
    expected = 9.6
    print('Input (-4.5, 2.3), (7.6, -0.2).\n'
          'Expected result', expected,
          'and actual result =', actual)
    if absolute(actual - expected) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :(\n')
        num_failed3 += 1

    return num_failed3

def main():
    num_fail = test_euclidean()
    if num_fail == 0:
        print('ALL TESTS PASSED!')
    else:
        print('Sorry', num_fail, 'tests failed. Please go back and fix.')
    
    num_fail2 = test_absolute()
    if num_fail2 == 0:
        print('ALL TESTS PASSED!')
    else:
        print('Sorry', num_fail2, 'tests failed. Please go back and fix.')

    num_fail3 = test_manhattan()
    if num_fail3 == 0:
        print('ALL TESTS PASSED!')
    else:
        print('Sorry', num_fail3, 'tests failed. Please go back and fix.')
    
    if num_fail == 0 and num_fail2 == 0 and num_fail3 == 0:
        print('Eucldiean Distance Test: Success!\n', 'Abosulte Distance Test: Success!\n', 'Manhattan Distance Test: Success!')
    else:
        print('A test has failed, please check the results and adjust accordingly!')

main()