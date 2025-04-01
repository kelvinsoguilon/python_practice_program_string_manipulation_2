#set string example
text = "   Kelvin Soguilon      "
#set variable to store the text in correct format
formatted_text = ""
#identify space characters
space_found = True
#iterate through every character and check if there is space
for char in reversed(text):
    if char != " " or not space_found:
        formatted_text = char + formatted_text
        space_found = False
#print result
print(formatted_text)