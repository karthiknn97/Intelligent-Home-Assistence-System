#import String
"""
term = {"message","light"} #term we want to search for
inp = input("enter") #read input from user
inp=inp.lower()
words = inp.split() #split the sentence into individual words

if term in words: #see if one of the words in the sentence is the word we want
   print("Keyword is there")
else:
    print("not there")

    """

swear = ("turn", "on", "it")
Userinput = str.lower(input("enter  "))

if all(Userinput.find(s)>=0 for s in swear):
     print("turning on")
else:
     print("please try")
