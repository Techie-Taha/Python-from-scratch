course = "Python is the easiest programming language"
print(course[7]) #in the terminal we will see i
print(course[6]) #in the terminal we won't see anything since there's a gap at index 6
print(course[4:8]) #it will start from index 7 which is i and will go all the way to index 10, and will ignore index 11
print(course[:]) #here 0 is the leading index
print(course[-2]) #it's gonna start from the end and index -2 is g
print(course[1:-1]) #it will ignore index 0 and will start from 1 which is y, and will ignore e because that's index -1
print(course[:6]) #it will include 0 as a leading index, and will ignore 6, will print out python
print(course[0:]) #including 0, it will print out the whole thing
course2 = "Python is the easiest language"
print(course2[-8:-4]) # count -8 in terms of positive index which is 22, and -4 is 26, so it's gonna be [22:26], in th terminal we should see lang
name = "Taha"
x = name[:2]
print(x) # here I defined another variable x to store name, and in [:2], 0 is the leading index so in the terminal we see Ta

y = "amazing"
z = y[1:6:2]
print(z)