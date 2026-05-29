import subprocess
result = subprocess.run(["df","-h"],capture_output=True,text=True)
print(result)
lines = result.stdout.split("\n")
#print(lines)
##print(lines)
##for line in lines:
    #if "/dev/" in line:
        #parts=line.split()
        ##parts = ["/dev/sda1", "50G", "40G", "10G", "80%"]
        ##filesystem=parts[1]
        #print(parts)



