#shop keeper will input product name and price and in the end it will show a summary

sum= 0
count=-1
number=0
b=list()
p=list()
while True:
    d= input("Enter product name: ")
    a= input("Enter the Product price: ")

    if d=="" :
        break
    else:
        b.append(int(a))
        p.append(d)
        sum=sum+int(a)

print("\n \n \n"
      "Thanks For Shopping to our shop\n\n"
      "Product list:")
for c in b:
    count=count+1
    number = number + 1
    print(f'{number}. {p[count]} = {c} Taka ')

print(f"----------------- \nTotal = {sum} Taka")
