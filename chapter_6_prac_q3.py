comment = input("Enter your comment: ")

if ("Make a lot of money" in comment or 
    "buy now" in comment or 
    "subscribe this" in comment or 
    "click this" in comment):
    
    print("This is a spam comment")
else:
    print("This is not a spam comment")