from multiprocessing.resource_sharer import stop


x =int(input("Please enter a Interger: "))
if (x % 2) == 0:
    print("Even")
else:
    print ("Odd")
