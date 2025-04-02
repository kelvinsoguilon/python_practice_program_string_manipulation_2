#define startswith function
def startswith_alternative(text, prefix):
#return the function and split the string into words. only take the first word
    first_word = text.split()[0] if text.split() else ""
#compare the first word to the splitted part
#print result