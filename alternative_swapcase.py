#define swapcase
def swapcase(text):
#set variable to store text
    formatted_string = ""
#iterate through every char
    for char in text:
#check if uppercase or lowercase and reverse it
        if 'A' <= char <= 'Z':
            formatted_string += chr(ord(char) + 32)
        else:
            formatted_string += chr(ord(char) - 32)
#print output