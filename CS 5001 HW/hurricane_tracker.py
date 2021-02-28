'''
CS 5001
Fall 2019
HW 2 - Hurrican Tracker
'''
'''
TEST CASES:
Boston; Expected: 1133.0631 miles; Actual: 1133.00631 miles
Miami; Expected: 144.3985 miles; Actual: 144.3985 miles
Grand Bahama Island: Expected: 31.35 miles; Actual: 31.347 miles
Fort Lauderdale: Expected: 126 miles; Actual: 126.8401 miles
Atlanta: Expected: 581 miles; Actual: 581.5472 miles
(Atlanta and Fort Lauderdale extimates recieved from measuring distance on google maps)
'''
from haversine import haversine

# def userquestions(question):


def main():
    print('Welcome to hurricane Tracker!')
    print('______________________________________________________')
    print('Please choose an option listed below!\n', 'B: Boston\n', 'M: Miami\n', 'O: Other') 
    user_input = input('Your input: ')
    
    if user_input != 'B' and user_input != 'M' and user_input != 'O' and user_input != 'b' and user_input != 'm' and user_input != 'o':
        print('Please select one of the options! (Automated Selection: B)')
        user_input = 'B'

    user_ans = user_input.upper()

    dorian_lat = 27.1 
    dorian_long = -78.4

    boston_lat = 42.361145 
    boston_long = -71.057083 
    
    miami_lat = 25.761681 
    miami_long = -80.19178
    
    # distance = haversine(latitude1, longitude1, latitude2, longitude2) 

    if user_ans == "B":
        distance = haversine(dorian_lat, dorian_long, boston_lat, boston_long)
        print('Hurricane Dorrian was ', distance, 'from Boston on September 3rd, 2019.')
        if 150 > distance:
            print('WARNING: Seek shelter immediately!')

    elif user_ans == "M":
        distance = haversine(dorian_lat, dorian_long, miami_lat, miami_long)
        print('Hurricane Dorian was ', distance, 'from Miami on September 3rd, 2019.')
        if 150 > distance:
            print('WARNING: Seek shelter immediately!')
    
    elif user_ans == "O":
        print("If you need to obtain your city's longitude and latitude, please use https://www.latlong.net/ !")
        user_location = input('What is the name of your city?: ')
        user_long = float(input('Please enter the longitude (decimal degrees): '))
        user_lat = float(input('Please enter the latitude (decimal degrees): '))

        distance = round(haversine(dorian_lat, dorian_long, user_lat, user_long), 4)

        print("Hurricane Dorian was ", distance, "from ", user_location, "on September 3rd, 2019.")
        if 150 > distance:
            print('WARNING: Seek shelter immediately!')

main()