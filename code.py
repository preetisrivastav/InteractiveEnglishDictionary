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


def find_meaning(W):
    if W in Data.keys():
        return Data[W]
    elif W.title() in Data.keys(): #Check with first letter captial like pronouns
        return Data[W.title()]
    elif W.upper() in Data.keys(): #Check acronyms
        return (Data[W.upper()])
    elif len(get_close_matches(W, Data.keys())) > 0:
            Match = get_close_matches(W,Data.keys())[0]
            UserInput = input("Do you mean %s instead of %s ?" %(Match, W))
            if UserInput.lower() == "y":
                W = Match
                return Data[W]
            else:
                return "Please double check the spelling"
    else:
        return "Word does not exist"

Word = input("Enter the word")
Output = find_meaning(Word.lower())
if type(Output) == list:
    for item in Output:
        print("%s" %item)
else:
    print(Output)
exit()
