#define rindex function
def rindex_alternative(text, substring):
#get text length and substring length
    text_length = len(text)
    substring_length = len(substring)
#iterate through text beginning in rightmost part and check first occurence of substring
#return value to i
#print output 