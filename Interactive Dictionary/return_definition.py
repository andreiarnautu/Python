#  How to manipulate ther data in the json file

import json


#  Import data
data = json.load(open("data.json", "r"))

def translate(word) :
  if(word in data) :
    print("This word has %d definitions: " % (len(data[word])))
    for definition in data[word]:
      print("---> " + definition)
  else:
    print("This word's definition does not exist in the dictionary")  

word = input("Enter word: ")
translate(word.lower())
