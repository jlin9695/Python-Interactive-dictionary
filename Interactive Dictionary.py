import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return w
    elif w.title() in data:
        return w
    elif w.upper() in data:
        return w
    elif len(get_close_matches(w, data.keys)) > 0:
        yn = input("Did you mean %s instead? You can enter y for Yes or N for no, as well as typing out the words: " % get_close_matches(word, data.keys())[0])
        if yn.upper() == "Y" or yn.lower() == "yes":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn.upper() == "N" or yn.lower() == "no":
            return "Your word does not exist. Please check your word and try again."
        else:
            return "We didn't understand your response, please try again. Make sure your response is an affirmative or negative."
    else:
        return "The word you have entered does not exist in our database and we cannot return a definition for it. Please check your word and try again. "

word = input("Please enter a word to define. We will return a definition if the word exists in our database: ")

output = translate(word.lower())

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)