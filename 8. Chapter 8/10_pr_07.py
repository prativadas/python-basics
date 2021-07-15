#to remove a given word from a string and strip at the same time


def remove_and_split(string, word):
    newStr = string.replace(word, "")          #any word in the string is replaced with blank.
    return newStr.strip()                       # removes space from th newstr

this = "     Harry is a good      "
n = remove_and_split(this, "Harry")
print(n)
# print(this)
# print(this.strip())     # strip removes the extra spaces.
