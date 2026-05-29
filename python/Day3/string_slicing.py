#string[start : end]

#Start index INCLUDED

#End index EXCLUDED (not included)

a = "Hello,World"
b =a[3:5]
print(b)
print(a[:5])
print(len(a))
print(a[2:])
print(a[:5])
#
if "Hello" in a:
    x=len("Hello")
    z=a[x+1:len(a)]
    print(z)
stringupper =z.upper()
stringupper_second = a.upper()
print(a.lower())
print(stringupper)
print(stringupper_second)


##Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
##The strip() method removes any whitespace from the beginning or the end:
txt="   i am lerning python"
print(txt.strip())

##The replace() method replaces a string with another string:
a2="Hello, World!"
a3="Manasi"
print(a2.replace("Hello",a3))

print(a.split(","))
