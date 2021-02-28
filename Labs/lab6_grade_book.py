'''
Luke Parkhurst
CS 5001
Fall 2019
Lab 6
'''


def add_student(student_roster):
    userinp = ''
    print('Step 1:')
    while userinp != ':Q:':
        userinp = input('Enter a unique student name (:q: to quit, or :check: to see current roster): ')
        userinp = userinp.upper()
        if userinp == ':Q:':
            break
        if userinp == ':CHECK:':
            print(student_roster)
        if userinp != ':CHECK:':
            student_roster.append(userinp)
        
    return student_roster

def add_grades(student_roster,grade_book):

    print("Step 2:")
    print("Let's add some grades!")
    userinp = ''
    print(student_roster)
    grade = []
    while userinp != ':Q:':
        userinp = input('Please choose a student from the roster: ')
        userinp = userinp.upper()
        if userinp in student_roster:
            if userinp in grade_book.keys():
                i = input('What grade (number) do you want to add? ' )
                grade.append(i)
                grade_book[userinp] = grade
            else:
                grade_book[userinp] = []
                i = input('What grade (number) do you want to add? ')
                grade.append(i)
                grade_book[userinp] = grade
        if userinp not in student_roster:
            print('That is not a student in the records, to add this name, please go to Add Student menu.')
    return grade_book

def score_avg(student, grade_book):
    score = 0
    # score is now a list
    score = grade_book[student]
    for i in range(len(score)):
         score[i] = int(score[i])
    return sum(score)/len(score)


def main():
    
    student_roster = []
    grade_book = {}

    print('Welcome to Cartoon Network University!')
    print('___________________________________________________')
    
    userinp = ''
    
    while userinp != ':Q:':
        userinp = input("Please choose one of the following options:\n Add Student to Roster: Student\n Add grade to grade book: Grades\n Check on current student's score and average: Scores\n Check who is on the student roster: Roster\n Or type :q: to quit\n")
        userinp = userinp.upper()
        if userinp == 'STUDENT':
            add_student(student_roster)
        if userinp == 'GRADES':
            add_grades(student_roster, grade_book)    
        if userinp == 'SCORES':
            print(student_roster)
            student = input('Choose a student to see current Grade average! ')
            if student not in student_roster:
                print('Please choose a student from the list! ')
            else:
                print(score_avg(student, grade_book))
        if userinp == 'ROSTER':
            print(student_roster)
            print(grade_book)
        if userinp is not 'STUDENT' and not 'GRADES' and not 'ROSTER' and not 'SCORES' and not ':Q:':
            print('That is not a valid option, please choose an option listed below.')

main()