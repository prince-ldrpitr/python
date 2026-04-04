username = input("enter the name:")
if(len(username)<10):
    print("the username are less than 10 charcter")
else:
    print("all is well")

# q5
list =["prince","janak","chirag","vansh"]
a = input("enter your name:")
if(a in list):
    print("your name in list")
else:
    print("your name are not in list")