s="hello world" #strings are immutable

a = len(s) #length of string
print(a)

print(s.upper())
print(s.lower())
print(s.capitalize()) #capital the first letter of string
print(s.title())

print("removing the whitespaces....")
print(s.strip())
print(s.lstrip())
print(s.rstrip())

print("FINDING AND REPLACE...")

text="python is fun"

print(text.find("is")) #return the index of first occurence
print(text.replace("fun","awesome")) #replace all the word with given word

print("SEPERATING AND JOINING.....")
sentence="Apples,Banana,Pineapples"
print(sentence.split(","))
print(",".join(['Apples','Banana','Pineapple']))

text1 = "python123"
print(text1.isalpha()) #tell all the digit in string is alphabet
print(text1.isdigit()) #tell all the digit in string is digit
print(text1.isalnum()) #tell all the digit in string is alpha numeric type
print(text1.isspace()) #if string is all whitespace
