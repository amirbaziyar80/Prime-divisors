#Mr.B (Amir Hossein Baziyar)
#baziyar72@gmail.com
#iran - Tehran

 
ListNumbers = [] # for prime numbers range [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
PrimeNumbers = [] # for prime numbers [2, 3, 5, 7]
PrimeDivisorsNumbers = [] # For prime divisors numbers (Number = 10) [2, 5]


def numbers(Num):
    for x in range(2, Num+1):
        ListNumbers.append(x)


def delete(x, ListNum):
    for z in ListNum:
        if z % x == 0:
            ListNumbers.remove(z)
    return ListNum


def check_prime(ListNum):
    while(len(ListNum) != 0):
        x = ListNum[0]
        PrimeNumbers.append(x)
        ListNum = delete(x, ListNum)
    #if len(ListNum) != 0: 
        #x = ListNum[0]
        #PrimeNumbers.append(x)
        #NewList = delete(x, ListNum)
        #check_prime(NewList)


def prime_divisors(num, prime):
    for x in prime:
        if num % x == 0:
            PrimeDivisorsNumbers.append(x)


if __name__ == "__main__":
    #MaxNumber = int(input("Enter your max number range for range numbers (More than the desired number) : "))
    numbers(1000) #MaxNumber
    check_prime(ListNumbers)
    #print(PrimeNumbers)
    Number = int(input("Enter your Number to check prime divisors : "))
    prime_divisors(Number, PrimeNumbers)
    print(f"prime divisors of {Number} => {PrimeDivisorsNumbers}")