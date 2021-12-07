#https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list


file="C:/Users/danie/Desktop/Tests/test_for_rewriting_a_file.txt"

f= open(file, "a")
f.write("\rweitere Zeile")
f.close()

# f= open(file, "w")
# f.write("HI")
# f.close()

# f= open(file, "r")
# print(f.read())
# print(f.readlines(20))
# f.close()

# f= open(file, "r+")
# f.write("\rweitere Zeile")
# print(f.read())
# f.close()