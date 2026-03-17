import os
f = open("dfile.txt", "r")
print(f.read())
g= open("defile_copy.txt", "w")
g.write(f.read())
f.close()
g.close()
os.remove("defile.txt")
