#define rindex function
def rindex_alternative(text, substring):
#get text length and substring length
    text_length = len(text)
    substring_length = len(substring)
#iterate through text beginning in rightmost part and check first occurence of substring
    for i in reversed(range(text_length - substring_length + 1)):
        if text[i:i + substring_length] == substring:
#return value to i
            return i
#print output 