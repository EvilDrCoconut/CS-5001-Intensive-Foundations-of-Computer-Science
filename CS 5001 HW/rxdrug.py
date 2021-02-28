'''
Luke Parkhurst
CS 5001
HW 6
Fall 2019
'''

class RxDrug:     
    def __init__(self, name, rx_ID):              
        self.name = name
        self.rx_ID = rx_ID
        self.lst_interactions = []
        self.description = ''

    def add_interaction(self, other_drug):        
        if other_drug != lst_interactions:   
            self.lst_interactions.append(other_drug)
 
    def check_interaction(self, other_drugs):
        new_list =[]
        for i in other_drugs:
            if i in self.lst_interactions:
                new_list.append(i)
        return new_list          
    
    def set_description(self, description):         
        self.description = description              
    
    def __str__(self):
        return self.name