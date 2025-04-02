#define count function
def count_alternative(text, substring):
#set count variable to 0 to store the number of appearance
    count = 0
#get length of text and substring
    text_length = len(text)
    substring_length = len(substring)
#iterate through text and check for substring occurences
    for i in range(text_length - substring_length + 1):
        if text[i:i + substring_length] == substring:
            count += 1
#return count
    return count
#print result
text = "for you, for me, for everyone "
substring = "for"

print(count_alternative(text, substring))