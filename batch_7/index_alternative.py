#define index function
def index_alternative(text, substring):
#get text length and substring length
    text_length = len(text)
    substring_length = len(substring)
#iterate through text and find first occurence of substring
    for i in range(text_length - substring_length + 1):
        if text[i:i + substring_length] == substring:
#return i value
            return i
#print result
text = "for you, for me, for everyone"
substring = "me"

print(index_alternative(text, substring))