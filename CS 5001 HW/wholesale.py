'''
CS 5001
Fall 2019
HW 1 - variables and operations
'''
'''
Test Plan:  
Test Case #1   1 book:   $14.97 cost,  $3.00 shipping,  $17.95 total cost    
Test Case #2   8 books:  $119.76 cost, $8.25 shipping,  $128.01 total cost    
Test Case #3   50 books: $748.50 cost, $39.75 shipping, $788.25 total cost
'''

def main():
    # asking the user to input a number of books being order, assuming they input integer greater than 0
    user_answer = input('How many books are being ordered? ')
    textbooks_ordered = float(user_answer)
    
    # This disallows for user to input an order of zero or negative
    if 0 >= textbooks_ordered:
        print("Textbook order must at least be one!")
        textbooks_ordered = 1
    '''
    calculating order costs by multiplying book order by original price and discounting the 40%
    then add on 3 first shipping and rest of shipping by using .75 times books ordered - 1
    finally, calculate total by adding both textbook and shipping costs together
    '''
    order_costs = round(((24.95 * textbooks_ordered) * .60), 2)
    shipping_costs = round((3.00 + ((textbooks_ordered - 1) * .75)), 2)
    total_costs = round((order_costs + shipping_costs), 2)

    # this spits the total back to the user
    print("The total wholesale costs will come to $", order_costs)
    print("The total shipping costs will come to $", shipping_costs)
    print("This order's total cost will come to $", total_costs)
    
main()