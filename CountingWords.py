#split() method splits string into list. You can specify the seperator, if not specified the default seperator is taken as white space.
#x="Hi this is a string" then  x.split("i") splits x as ['H',' th','s ','s a str','ng']


myString = "Hello, this is a string"
words = myString.split()

length = len(words)
print(f"Number of words are:{length}")
#output:
#Number of words are:4
