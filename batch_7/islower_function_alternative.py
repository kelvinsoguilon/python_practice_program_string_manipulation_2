#set string example
text = "Kelvin Soguilon"
#define the range of lowercase letters
lowercase = ("a", "z")
#identify if character is on lowercase
for char in text:
    if char in lowercase:
        continue
#print not all character are in lowercase
    else:
        print("Not all characters are in lowercase")
        break