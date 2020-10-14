import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def meaning(word):
    global i
    word = word.lower()
    if word in data:
        return data[word]
    if word.title() in data:
        return data[word.tile()]
    if word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("did you mean by %s?,press y for yes and n for no" % get_close_matches(word,data.keys())[0])
        choice = input()
        crct = get_close_matches(word,data.keys())[0]
        if choice == "y":
            return data[crct]
        else:
            return "thank you"
    else:
        return "word does not exist"

choice1 = True
while (choice1):
    word = input("enter a word: ")
    lst= (meaning(word))
    i = 0
    if type(lst) != str:
        print("the meanings are:")
        for mn in lst:
            i += 1
            print(i,".",mn)
    else:
        print(lst)
    choice1 = input("do you want to continue,press y if yes or n if no: ")
    if choice1 == 'n':
        choice1 = False
        print("thank you :)")