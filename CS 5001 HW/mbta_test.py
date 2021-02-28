'''
Luke Parkhurst
CS 5001
Fall 2019
HW 4
'''
'''
Test cases for the whole program (you"ll still need to test your individual functions as well):
TEST CASES:
Test Case 1: Input: Shawmut to Fields Corner. Output: 1 stop, towards Alewife
Test Case 2: Input: Kendall to Savin Hill. Output: 8 stops, towards Ashmont
Test Case 3: Input: Alewife to Davis. Output: 1 stop, towards Ashmont
Test Case 4: Input: Broadway to Charles/MGH. Output: 4 stops, towards Alewife
Test Case 5: Input: Ashmont to Alewife. Output: 16 stops, towards Alewife
Test Case 6: Input: Porter to Porter. Output: I can't help you
'''

import mbta

def main():
    
    # Gather and validate input (user provides names of start/end stations)
    # Assumption: User is not transferring
    start_station = input("Enter a starting T station\n")
    while not mbta.is_valid_station(start_station):
        start_station = input("I've never heard of that station, "
                              "please enter again\n")
        
    end_station = input("Enter your destination T station\n")
    while not mbta.is_valid_station(end_station):
        end_station = input("I've never heard of that station, "
                            "please enter again\n")
    
    # Figure out the direction to go on that line (final station
    # in the direction from start to end)
    direction = mbta.get_direction(start_station, end_station)
    num_stops = mbta.get_num_stops(start_station, end_station)

    # Report the result, assuming we"re actually going somewhere
    if num_stops == 0:
        print(start_station, " to ", end_station, "? "
              "I can't help you with that one!", sep = "")
    else:
        print("Get on at ", start_station, " toward ", direction, ".\n"
              "Take the train for ", num_stops, " stops and arrive at ",
              end_station, ".", sep = "")
        
main()
