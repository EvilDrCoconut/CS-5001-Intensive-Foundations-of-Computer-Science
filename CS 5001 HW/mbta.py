'''
Luke Parkhurst
CS 5001
Fall 2019
HW 4
'''
'''
TEST CASES:

is_valid_station Tests:
Test Case 1: Shawmut                 Returns True
Test Case 2: Porter                  Returns True
Test Case 3: Dogwood                 Returns False
Test Case 4: Smithers                Returns False

get_directions Tests:
Test Case 1: Alewife to Ashmont             Returns South
Test Case 2: Park St to Kendall/MIT         Returns North
Test Case 3: South Station to Savin Hill    Returns South
Test Case 4: Park St to Park St             Returns No destination found

get_num_stops Tests:
Test Case 1: Ashmont to Park St      Returns 9
Test Case 2: Park St to Ashmont      Returns 9
Test Case 3: Kendall/MIT to Central  Returns 1
Test Case 4: South Station to Porter Returns 7
'''

# list of all red line stations
red_line = ['ASHMONT', 'SHAWMUT', 'FIELDS CORNER', 'SAVIN HILL', 'JFK/UMASS', 'ANDREW', 'BROADWAY', 'SOUTH STATION', 'DOWNTOWN CROSSING', 'PARK ST', 'CHARLES/MGH', 'KENDALL/MIT', 'CENTRAL', 'HARVARD', 'PORTER', 'DAVIS', 'ALEWIFE' ]

# start of the is valid station function, takes the station name as a parameter
def is_valid_station(station_name):
    
    station_name = station_name.upper() #converts station name to upper for check against list

    if station_name in red_line: # creates if statement to check if station name in list
        return True # returns true if station name is in list
    else:
        return False # returns false is station name not in list


# start of the get directions function
def get_direction(start_station, end_station):

    if start_station == end_station: # sees if start destinations and end destination are same
        return 'No destination found' # returns no destination found if they are the same

    i = start_station.upper() # sets constant and turns start station into uppercase for check against red line list
    b = end_station.upper() # set constant and turns end station into uppercase for check against red line list

    i = red_line.index(i) # sets constant to index value of start station

    b = red_line.index(b) # sets constant to index value of end station

    if i - b < 0: # creates if statements that subtracts end value from start value
        return 'Alewife' # if start station is higher index value than end station, will return number over 0
    elif i - b > 0: # but if start station has lower index value than end station, will return number under 0
        return 'Ashmont'# so will return South if under 0, but North if over 0


# start of the number of stops function
def get_num_stops(start_station, end_station):

    if start_station == end_station: # compares to see if the start and end station are the same
        return 0 # returns 0 if the station inputs are the same
    
    i = start_station.upper() # sets constant and turns start station into uppercase for check against red line list
    b = end_station.upper() # set constant and turns end station into uppercase for check against red line list

    i = red_line.index(i) # sets constant to index value of start station

    b = red_line.index(b) # sets constant to index value of end station

    num_stops = abs(i - b) # takes the absolute difference between start and end stations' indexes
    
    return num_stops # returns the number of stops between stations