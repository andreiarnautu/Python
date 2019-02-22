#  How to manipulate ther data in the json file
import json
import difflib
from difflib import get_close_matches

#  Import data
data = json.load(open("data.json", "r"))

def translate(word) :
    if word.lower() in data :
        word = word.lower()
    elif word.upper() in data :
        word = word.upper()
    elif word.title() in data :
        word = word.title()


    if(word in data) :
        print("This word has %d definitions: " % (len(data[word])))
        for definition in data[word]:
           print("---> " + definition)
    else:
        close_matches = get_close_matches(word, data.keys())

        if len(close_matches) == 0:
            print("This word's definition does not exist in the dictionary")  
        else:
            verdict = input("The word could not be found in the dictionary. Did you mean '%s'? [y/n]"  % (close_matches[0]))
            if verdict.lower() == "y":
                translate(close_matches[0])
            elif verdict.lower() != "n":
                print("It was supposed to be a 'y' or a 'n'...")

word = input("Enter word: ")
translate(word)
