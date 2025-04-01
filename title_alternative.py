#define title function
def title(text):
#set a variable to store the texts
    format_title = ""
#capitalize every first letter of word while keeping rest on lowercase
    words = text.split()
    for word in words:
        format_title += word[0].upper() + word[1:].lower() + " "
#print output on title casing