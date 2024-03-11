#Udskriv alle de kvardratiske tal mellem 0 og 99, ved hjælp af while

square = 0
number = 2

while square<99:
#print all squares from 0 to 99
    square = number ** 2
    if square>99:
        break
    print(square)
    number += 1
