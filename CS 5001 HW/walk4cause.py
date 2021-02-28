import math
'''
CS 5001
Fall 2019
HW 1 - variables and operations
'''
'''

# 1 mile is 1.61 km, and 1 km is 0.62 miles
Test Plan:
Test Case #1    .25 km walk, .25 hr, $4/mile    ml walked = .16,  .64 mph, $2.56 earned
Test Case #2    .5 km walk, .4 hr, $2/mile      ml walked = .31,  .78 mph, $0.62 earned
Test Case #3    1 km walk, 0.5 hr, $5/mile      ml walked = .62,  1.24 mph, $3.10 earned
Test Case #4    5 km walk, 1 hr, $0.55/mile     ml walked = 3.1,  3.10 mph, $1.71 earned
Test Case #5    10 km walk, 3.5 hr, $2.43/mile  ml walked = 6.2,  1.77 mph, $15.07 earned
'''
def main():
    # allow user to input data for distance walked and time taken
    user_answer1 = input('Kilometers walked ?')
    kilometers_walked = float(user_answer1)

    user_answer2 = input('Time taken in hours to walk distance? ')   
    hours_walked = float(user_answer2)          

    user_answer3 = input('What is your sponsor paying per mile? ')   
    sponsor_money = float(user_answer3)
    
    # input raw data into conversion formulas set to variables
    miles_walked = round((kilometers_walked * 0.62), 2)
    miles_per_hour = round((60 / (hours_walked * 60)) * miles_walked, 2)
    pace = round((hours_walked / miles_walked), 2)
    minutes = math.floor(pace * 60)
    seconds = math.floor((((pace * 60) - minutes) * 60))
    money_earned = round((sponsor_money * miles_walked), 2)

    # print the outputs of converted raw data from variables
    print('You have walked ', miles_walked, 'miles!')
    print('You walked at a pace of ', miles_per_hour, 'miles per hour!')
    print('Your average pace per mile is ', minutes, 'minutes and ', seconds, 'seconds!')
    print('You have earned ', money_earned, 'for contribution!!!')
    print('______________________________________________________________________________________')

    # thank user for participating in event
    print('Thank you for participating in this charity fund raiser event!')

main()
