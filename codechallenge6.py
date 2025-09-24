

num = eval(input("Input a number --> "))

result = 1
for x in range(num, 0, -1):
    #print(x)
    print(result, "*", x, " = ",result)
    result *= x

print("Factorial is ",result)