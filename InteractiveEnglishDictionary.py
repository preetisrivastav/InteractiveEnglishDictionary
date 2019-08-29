#Version 1 with SequenceMatcher

# import json
# import difflib
# Data = json.load(open("C:\data.json"))

# def findmeaning(W):
# if W in Data.keys():
#        return ("The meaning of the word is %s" %(Data[W]))
#    else:
#        for i in Data:
#            match = difflib.SequenceMatcher(None,W,i).ratio()
#            if match >= 0.8:
#                UserInput = input("Do you mean %s instead of %s ?" %(i, W))
#                if UserInput.lower() == "y":
#                    return ("The meaning of the word is %s" %(Data[i]))
#                else:
#                    return ("Please double check the spelling")
#        return ("Word does not exist")

# Word = input("Enter the word")
# print(findmeaning(Word.lower()))
# exit()

#Version 2 with Get_Close_Matches

import json
from difflib import get_close_matches
Data = json.load(open("C:\data.json"))


def find_meaning(w):
    if w in Data.keys():
        return Data[w]
    elif w.title() in Data.keys():  # Check with first letter Capital like pronouns
        return Data[w.title()]
    elif w.upper() in Data.keys():  # Check acronyms
        return Data[w.upper()]
    elif len(get_close_matches(w, Data.keys())) > 0:
        match = get_close_matches(w,Data.keys())[0]
        user_input = input("Do you mean %s instead of %s ?" %(match, w))
        if user_input.lower() == "y":
            w = match
            return Data[w]
        else:
            return "Please double check the spelling"
    else:
        return "Word does not exist"


def main():
    word = input("Enter the word \n")
    output = find_meaning(word.lower())
    if type(output) == list:
        for item in output:
            print("%s" % item)
    else:
        print(output)


if __name__ == '__main__':
    main()
