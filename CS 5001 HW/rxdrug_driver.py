'''
Luke Parkhurst
CS 5001
Fall 2019
'''
from rxdrug import RxDrug

interactions = []; drugs = []


def main():
    dfile = open('5001 CS Foundations\CS 5001 HW\xcui_drugs.txt','r')
    for line in dfile:
        drugs.append(line)


    print(drugs)

main()
    