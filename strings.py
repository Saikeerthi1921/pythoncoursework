#string defination
strg1 = "Hello"
strg2 = "world"
strg3 = "this is a multi-line example"
print(strg1)
print(strg2)
print(strg3)

#string operations
#concatenation
str1 = 'Hello'
str2 = 'world'
result = str1+ ' ' +str2
print(result)

#repetiton
print("python!"*5)

#indexing
text = "python"
print(text[0])
print(text[-1])

#sciling
print(text[0:3])
print(text[:4])
print(text[2:])

#Membership
print("pyt" in text)
print("pyt" not in text)

#Built-in Functions
#len(), min() / max(), sorted(), chr() or ord()
#len()
text1 = "Umadevi"
print(len(text1))
 
#min()/ max()
print(min(text1))
print(max(text1))

#sorted
print(sorted(text1))

#chr() / ord()
print(chr(97))


                     #complete list of string methods with examples
#case Conversions
#upper(), lower(), capitalize(), title(), swapcase(), caseflod()
obj = "hello world"
print(obj.upper())
print(obj.lower())
print(obj.capitalize())
print(obj.title())
print("SU".casefold())

 #Alignment & Formartting methods
 #center(width,fillchar), ljust(width,fillchar), rjust(width,fillchar),zfill(width)
print("python program lang".center(100,"*"))
print("python".ljust(20," "))
print("python".ljust(20,"_"))
print("course".ljust(20,"*")+':language')
print("course".rjust(20,"*")+':language')
print("101".zfill(5))
print("saikeerthi".zfill(15))

#search& find methods
#find(sub), index(sub), rindex(sub), count(sub)
print("saikeerthi".find("1"))
print("saikeerthi".rfind("1"))
print("saikeerthi".index("e"))
print("saikeerthi".rindex("i"))
print("saikeerthi".count("i"))


