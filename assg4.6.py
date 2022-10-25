def computepay(h,r):
    if h <= 40 :
        b=h
        p=b*r
        return p
    else:
        o=h-40
        r2=1.5*r
        p=(40*10.50)+(o*r2)
        return p
hrs = input("Enter Hours:")
rt = input("Enter rate:")
hr = float(hrs)
rte = float(rt)

pay = computepay(hr,rte)
print("Pay",pay)
