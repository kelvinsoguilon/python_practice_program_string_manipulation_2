#define center function
def alternative_center(text, width, fillchar = " ")
#get string length
    text_length = len(text)
#get the padding needed
    padding_needed = max(0, width - text_length)
#divide padding in left and right
#return characters in center string format
#print result