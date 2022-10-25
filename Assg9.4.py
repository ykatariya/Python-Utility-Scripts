 # Write a program to read through the mbox-short.txt
 # figure out who has sent the greatest number of mail messages.
 # The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
 # The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
 # After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

fname=input('Enter the file name:')
handle=open(fname)
l1=list()
l2=list()
d=dict()

for line in handle:
     if line.startswith('From '):
         l1=line.split()
         # print('SplitLine:',l1)
         l2.append(l1[1])
         # print('Only emailaddr:',l2)


# for developing dictionary histogram
for e in l2:
    d[e]=d.get(e,0)+1

# print('The dictionary:',d)

# for the greatest number of mail messages
ecount=None
eword=None

for eword1,ecount1 in d.items():
    if ecount is None or ecount1 > ecount:
        eword=eword1
        ecount=ecount1

print(eword, ecount)
