'''
CS 5001
Fall 2019
HW 1 - variables and operations
'''
'''
Test Cases:
Test Case 1: 1 pie crust, 7 potatoes, 2 packages of meat, 2 packs of corn; Pies made: 1!
    left over ingredients? pie crust = 0, potatoes = 1, packages of meat = 0, packagaes of corn = 1
Test Case 2: 3 pie crust, 12 potatoes, 8 packages of meat, 2 packs of corn; Pies made: 2!
    left over ingredients? pie crust = 1, potatoes = 0, packages of meat = 2, packagaes of corn = 0
Test Case 3: 2 pie crust, 15 potatoes, 5 packages of meat, 4 packs of corn; Pies made: 2!
    left over ingredients? pie crust = 0, potatoes = 3, packages of meat = 1, packagaes of corn = 2
Test Case 4: 8 pie crust, 51 potatoes, 17 packages of meat, 12 packs of corn; Pies made: 8!
    left over ingredients? pie crust = 0, potatoes = 3, packages of meat = 1, packagaes of corn = 4
Test Case 5: 23 pie crust, 167 potatoes, 64 packages of meat, 78 packs of corn; Pies made: 23!
    left over ingredients? pie crust = 0, potatoes = 29, packages of meat = 16, packagaes of corn = 55
'''
# dictate the required amount of ingredients needed for one pie
pie_crusts_needed = 1
potatoes_needed = 6
packages_of_meat_needed = 2
packages_of_corn_needed = 1

def main():
    # Reminds user of materials needed for a pie
    print("One pie needs 1 pie crust, 6 potatoes, 2 packages of meat, and a package of corn!!!")
    
    #from here, asks user for input of each ingredient and amount collected

    user_answer1 = input("How many pie crusts did we collect? ")
    pie_crusts = int(user_answer1)

    user_answer2 = input("How many potatoes did we collect? ")
    potatoes = int(user_answer2)

    user_answer3 = input("How many packages of meat did we collect? ")
    packages_of_meat = int(user_answer3)

    user_answer4 = input("How many packages of corn did we collect? ")
    packages_of_corn = int(user_answer4)

    # reminds user no negative ingredients, sets negative ingredient to zero
    if 0 > pie_crusts or potatoes or packages_of_meat or packages_of_corn:
        print("You can not have less than zero of an ingredient!")
        if 0 > pie_crusts:
            pie_crusts=0
        if 0 > potatoes:
            potatoes = 0
        if 0 > packages_of_meat:
            packages_of_meat = 0
        if 0 > packages_of_corn:
            packages_of_corn = 0

    # now to determine number of pies created with given ingredients amount and remainder of ingredients
    max_pies_possible = min((pie_crusts / pie_crusts_needed), (potatoes / potatoes_needed), (packages_of_meat / packages_of_meat_needed), (packages_of_corn / packages_of_corn_needed)) 
    number_of_pies = int((pie_crusts / pie_crusts_needed) and (potatoes / potatoes_needed) and (packages_of_meat / packages_of_meat_needed) and (packages_of_corn / packages_of_corn_needed and max_pies_possible))
    
    # gives the remainder of each ingredient
    remainder_pie_crusts = (pie_crusts - number_of_pies)
    remainder_potatoes = (potatoes - (number_of_pies * potatoes_needed))
    remainder_packages_of_meat = (packages_of_meat - (number_of_pies * packages_of_meat_needed))
    remainder_packages_of_corn = (packages_of_corn - number_of_pies)

    # tells number of pies made
    print("You made", number_of_pies, "pies! Congrats!")
    
    #tells remainder of indgredients
    print("You have ", remainder_pie_crusts, ' pie crusts left!')
    print("You have ", remainder_potatoes, ' potatoes left!')
    print("You have ", remainder_packages_of_meat, ' packages of meat left!')
    print("You have ", remainder_packages_of_corn, ' packages of corn left!')
    print("_______________________________________________________________________________")

    # thanks user for help
    print("Thank you for your work and contribution in our Needy Families Program!")


main()