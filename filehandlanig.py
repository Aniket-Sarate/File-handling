
# file read method 

"""file = open("D:\\Aniket\\PY\\filehandaling\\file.txt" , "r")
readfile = file.read()
print(readfile)
file.close"""

# second method of read
# in following method to read particulaer words in file
"""
file = open("D:\\Aniket\\PY\\filehandaling\\file.txt","r")
readfile = file.read(10)
print(readfile)
file.close"""

# 3rd method of read
# read file line by line

"""file = open("D:\\Aniket\\PY\\filehandaling\\file.txt","r")

readline1 = file.readline()
print(readline1)

readline2 = file.readline()
print(readline2)

file.close"""

#file write method (in this method file are overwrite) old file data (my roles & responsblity is understanding requriment)

"""file = open("D:\\Aniket\\PY\\filehandaling\\file.txt","w")
writefile = file.write("Hii my is aniket mahadev sarate \n I have a working application support in past 2 years")
print(writefile)
file.close()
"""
# file append method (in this method file are not overwrite only append file )

file = open("D:\\Aniket\\PY\\filehandaling\\file.txt","a")
appendfile = file.write("\n and i am looking for job change")
print(appendfile)
file.close