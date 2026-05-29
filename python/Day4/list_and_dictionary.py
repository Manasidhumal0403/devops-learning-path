##List: List in square bracket
servers=["server1","server2","server3"]
servers.append("server4")
for i in servers:
  print(i)

 ##Dictionary: Dictionary are created in curly bracse{} 

info = { 
   "name":"serv1",
   "cpu":80,
   "Status":"server is running"
 }
print(info)

text = "error error warning info error "
words = text.split()
words_count ={}
for word in words:
  
  if word in words_count:
    ##print(words_count[word]) //error:1 error:2
    words_count[word] += 1
  else:words_count[word] = 1
  ##print(words_count[word]) 
##print(words_count[word]) 


print(words_count)
print(words_count[word])

