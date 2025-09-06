#Writing  to a file.

'''
f = open( “demo.txt”,“w”)
f.write( "this is a new line") #Overwrites the entire file

f = open( “demo.txt”,“a”)
f.write( “this is a new line“ ) #adds to the file

'''

f = open("A:\Study\Data Analyst\Python\Code\Problems Sagar\File Input & Output\demo.txt", "w")

f.write("I am want to learn c++ next week. 1212")

f.close()