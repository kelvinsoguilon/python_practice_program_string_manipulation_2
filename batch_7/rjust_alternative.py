#define rjust
def rjust(text, width, fillchar = " "):
#get length of string
    text_length = len(text)
#get the count of padding characters needed
    padding_needed = max(0, width - text_length)
#return string in rjust format
#print output