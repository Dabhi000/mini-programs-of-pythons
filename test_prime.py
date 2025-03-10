def test_prime(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not prime number")
                break
            else:
                print(num,"is prime number")
    else:
        print(num,"is not prime number")
num = int(input("enter the to check prime or not:"))
test_prime(num)