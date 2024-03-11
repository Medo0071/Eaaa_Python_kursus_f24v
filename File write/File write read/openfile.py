# Open a file
fo = open("foo.txt", "r+")
str = fo.read(50);
print("Read String is : ", str)
# Close opend file
fo.close()
