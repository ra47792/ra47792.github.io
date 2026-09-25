string = input("Enter a string.:")
delete = input("Enter a letter to remove:") 
newstring = ""
for s in string:
    if s != delete:
        newstring = newstring + s
print(newstring)
