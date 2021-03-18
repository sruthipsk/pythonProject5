words=input("enter the word:")
word=input("enter the word:")
word1=words
frst=words[0]
words=words.replace(frst,"$")
word=frst+word[1:]
print(word1,">>",words)