# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count=0
add=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count=count+1
    value=float(line[19:])
    add=add+value
    # print(line)
print('Average spam confidence:', add/count)
