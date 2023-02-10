#Mr.B (Amir Hossein Baziyar)
#baziyar72@gmail.com
#iran - Tehran
#Quesion = Write a function that receives a number as an input argument,
#          then calculates the prime numbers from 1 to that number.
#          In the next step,    
#          it receives a number as an input argument,
#          then calculates its prime divisors and prints it in the output. 
#Result =>
#Enter your max number range for range numbers (More than the desired number) : 10
#Enter your Number to check prime divisors : 10
#prime divisors of 10 => [2, 5]

 
ListNumbers = [] # for prime numbers range [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
PrimeNumbers = [] # for prime numbers [2, 3, 5, 7]
PrimeDivisorsNumbers = [] # For prime divisors numbers (Number = 10) [2, 5]


def numbers(Num): #To fill the ListNumbers
    for x in range(2, Num+1): # Because the first  prime number is 2, then our array also starts from 2. In order to have the number entered by the user in the array, we add one 
        ListNumbers.append(x)


# I used the sieve algorithm for this


def delete(x, ListNum): # get prime number and latest list number list
    for z in ListNum:
        if z % x == 0:
            ListNumbers.remove(z) #Remove numbers divided by the prime number
    return ListNum


def check_prime(ListNum): # get prime numbers
    if len(ListNum) != 0: # At the end, ListNumbers[] will be empty. So if it is empty, it means there is no number to check. In other words, my exit point is empty ListNumber[]. 
        x = ListNum[0] # The first available number is the prime number
        PrimeNumbers.append(x) # Add prime number to PrimeNumbers list
        NewList = delete(x, ListNum) # Call the Delete() function and assign two parameters, the last prime number and the last list of numbers.
        check_prime(NewList) # (recursive function) After removing the remaining divisible numbers in the list, we get the new list and call check_prime() again with the "NewList" parameter.


def prime_divisors(num, prime): # Get target number and prime number list
    for x in prime:
        if num % x == 0:
            PrimeDivisorsNumbers.append(x) # Add the prime numbers that are divisible by the target number to "prime_divisors".


if __name__ == "__main__":
    MaxNumber = int(input("Enter your max number range for range numbers (More than the desired number) : "))
    numbers(MaxNumber) # create list
    check_prime(ListNumbers) # create prime numbers
    # print(PrimeNumbers)
    Number = int(input("Enter your Number to check prime divisors : "))
    prime_divisors(Number, PrimeNumbers) # Get Prime Divisors Numbers List
    print(f"prime divisors of {Number} => {PrimeDivisorsNumbers}")