#define capitalized text
def capitalize(text):
#set variable to store string
    formatted_string = ""
#split string into word
    words = text.split()
#iterate through every first letter of the word
    for word in words:
#capitalize the first letter and add the rest unchanged
        formatted_string += word[0].upper() + word[1:] + " "
#print result
    return formatted_string.strip()
print(capitalize("kelvin soguilon"))