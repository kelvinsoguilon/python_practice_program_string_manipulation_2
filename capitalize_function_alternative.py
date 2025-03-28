#define capitalized text
def capitalize(text):
#set variable to store string
    formatted_string = ""
#split string into word
    words = formatted_string.split()
#iterate through every first letter of the word
    for word in words:
#capitalize the first letter and add the rest unchanged
        formatted_string += word[0].upper() + word[1:] + " "
#print result