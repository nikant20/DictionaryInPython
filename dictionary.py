import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif len(get_close_matches(word,data.keys()))>0:
        yn = input("Did you mean %s ? Enter Y if yes, or N if no." % get_close_matches(word,data.keys())[0])
        if yn == "Y":        
            return data[get_close_matches(word,data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exists. Please check the word."
        else:
            return "We didn't understood what did you said?"
    else:
        return "Word doesn't exsist. Please check the word."

word = input("Enter word: ")


output = translate(word)

if type(output) == list:
   for item in output:
      print(item)
else:
    print(output)      