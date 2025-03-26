#define lowercase
def lowercase(text):
#store text in variable
    formatted_string = ""
#check if the characters are in uppercase
    for char in text:
        if 'A' <= char <= 'Z':
            formatted_string += chr(ord(char) + 32)
        else:
            formatted_string += char
    return formatted_string
#print output
print(lowercase("Kelvin Soguilon"))