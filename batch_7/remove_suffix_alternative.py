#define remove suffix
def remove_suffix(text):
#split string into word and remove the last word
    return " " .join(text.split()[:-1])
#print result
print(remove_suffix("Kelvin Soguilon"))