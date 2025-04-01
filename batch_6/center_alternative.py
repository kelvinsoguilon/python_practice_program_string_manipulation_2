#define center function
def alternative_center(text, width, fillchar = " "):
#get string length
    text_length = len(text)
#get the padding needed
    padding_needed = max(0, width - text_length)
#divide padding in left and right
    left_pad = padding_needed // 2
    right_pad = padding_needed - left_pad
#return characters in center string format
    return (fillchar * left_pad) + text + (fillchar * right_pad)
#print result
text = "Kelvin Soguilon"
width = 31

print(alternative_center(text, width))