n = int(input("Enter the length of the sequence: ")) # Do not change this line#Sumnma af síðustu þremur
counter = 4
num1 = 1
num2 = 2
num3 = 3
sum = 0
print(num1)
print(num2)
print(num3)

while counter <= n:
    sum = num1 + num2 + num3
    print(sum)
    counter += 1
    num1=num2
    num2=num3
    num3=sum

        
    