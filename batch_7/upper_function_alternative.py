#set string example
text = "Kelvin Soguilon"
formatted_text = ""
#checks if char is on lowercase
for char in text:
    if 'a' <= char <= 'z':
        formatted_text += chr(ord(char) - 32)
#otherwise keep the same text
    else:
        formatted_text += char
#print result