import os

# directory ka path (yaha tum apna path likh sakte ho)
path = "/"

# directory ke andar ke files aur folders ki list
contents = os.listdir(path)

# print karna
print("Directory ke contents:")
for item in contents:
    print(item)