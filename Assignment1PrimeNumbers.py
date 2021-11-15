N = int(input("Please select here the number N of primes you want to print:"))
a = 2 # initializing the starting value (as 0 and 1 is no prime number by definition)

while N != 0: # repeat 'for loop' as long as the remaining numbers of primes to print is not 0:
    for i in range (2,a): # 'for loop' sequence, start = 2, stop = a
        if a%i == 0: # if the number is divisible by i, then a is not a prime number
            break
    else: #otherwise, n is prime number
        print(a,end = ", ") # print a and create a blank space
        N -= 1 # update the remaining amount of prime numbers to print by -1
    a += 1 # update the starting value by +1