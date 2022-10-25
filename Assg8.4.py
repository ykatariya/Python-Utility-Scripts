# Open the file romeo.txt
# read it line by line. For each line, split the line into a list of words using the split() method.
# The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.



fname = input("Enter file name: ")
fh = open(fname)
lst1 = list()
lst2 = list()


for line in fh:
    lst1=line.split()

    for w in lst1:
        if w in lst2: continue
        # print('This is list 2:')
        lst2.append(w)
        # print('This is content of list 2:',lst2)

# print('out of all for')
lst2.sort()
print(lst2)



    # I guess might need to use double splitting and if condition or again for loop




# print(line.rstrip())
