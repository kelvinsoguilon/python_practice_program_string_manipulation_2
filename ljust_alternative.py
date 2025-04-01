#define ljust function
def ljust(text, width, char_fill = " "):
#get length of string
    text_length = len(text)
#get the padding characters needed
    padding_char = max(0, width - text_length)
#fill characters to the end of the string
#print result