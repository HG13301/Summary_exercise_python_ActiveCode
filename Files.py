names_list=["orel","hadas","eliya","yeonatan","michal","yedidya","talya"]

name_file=input("Enter a name for file")
f=open(name_file+".txt","a")
f.write(str(names_list))
f.close()

#open and read the file after the appending:
f = open(name_file+".txt", "r")
print(f.read())