# Open a file
fo = open("foo.txt", "w")
tekst = "Python is a great language.\nYeah its great!!\n"
fo.write(tekst)
tal = str(12)
fo.write(tal)
# Close opend file
fo.close()
