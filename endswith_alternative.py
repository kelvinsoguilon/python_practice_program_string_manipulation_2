#define endswith function
def endswith(text, suffix):
#get length of suffix
    suffix_length = len(suffix)
#extract end part of string with same length as suffix
    end_part = text[- suffix_length:]
#compare extracted part and suffix
#print result