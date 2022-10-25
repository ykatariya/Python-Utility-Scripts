# Use words.txt as the file name
fname = input("Enter file name: ")
# print('The entered file name is :', fname)
fh = open(fname)

for line in fh :
    line=line.rstrip()
    line=line.upper()
    print(line)
