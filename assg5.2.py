largest = None
smallest = None
while True:
    #handle input
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        n=int(num)
    except:
        print('Invalid input')
        continue

    #find smallest
    if smallest is None:
        smallest=n
    elif n < smallest :
        smallest=n

    #find largest
    if largest is None:
        largest=n
    elif n > largest :
        largest=n

print('Maximum is', largest)
print('Minimum is', smallest)
