# mutable like lists, hold multiple values, each value has its own key, not quite an index position
weather = dict()
weather ['Sunday'] = [95.5, 2.2]
weather ['Monday'] = [86]

language = dict()
language ['hello'] = 'bonjour'
language ['how are you'] = 'comment ca va'

def main():
    print(weather)
    print(language)
    print(language['hello'])
    print(language.keys()) #this gives a list of dictionary keys to show what can be typed

    for each_key in language.keys():
        print(each_key)
    for each_value in language.values():
        print(each_value)
   
    del(language['hello']) # deletes key and value
    print(language)
   
    language['goodbye'] = 'au revoir'
    print(language)
   
    x = language.pop('goodbye') # removes key and value, sets it to variable x
    print(x)

    language['how are you'] = 'que pasa' #overwrites the key's value
    print(language)

    for each_key, each_val in language.items():
        print(each_key, ' ', each_val)

    language['hello'] = 'konichiwa', 'bonjour', 'bom dia', 'hi mate' #creates a list for hello key
    print(language)

    print(language['hello'][0]) # takes first word from hello list

    print(language['hello'][0][0]) #takes the first letter of the first word in hello's list

main()