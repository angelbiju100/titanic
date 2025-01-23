a=int(input("enter the price of the bike"))
if a<=50000:
    b=(a*5)/100
    print("road tax to be paid is ",b)
elif 50000<a<=100000:
    c=(a*10)/100
    print("road tax to be paid is", c)
else:
    d=(a*15)/100
    print("road tax to be paid is", d)
