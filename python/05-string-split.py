text = "Python decides type for you"
output =text.split()
print("Words:", output)
#Words: ['Python', 'decides', 'type', 'for', 'you']
output1=text.strip()
print(output1)


text = "   Some spaces around   "
stripped_text = text.strip()
print("Stripped text:", stripped_text)
  

 text = " ab cd ef   gh ij      kl"
stripped_text2 = text.strip()
print("Stripped text:", stripped_text)