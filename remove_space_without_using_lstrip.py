#set a string example
fullname = "     Kelvin Soguilon"
#set variable that stores text after ignoring spaces
fullname_formatted = ""
#check if there are leading spaces and skip it
space_found = True
for char in fullname:
    if char != " " or not space_found:
        fullname_formatted += char
        space_found = False
#print the result without the leading spaces