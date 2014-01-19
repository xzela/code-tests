def is_prime(n):
    for i in range(2,n):
        if (n % i) == 0:
            return False
    return True

limit = 1000
summer = 0
done = False
number = 1 
count = 0 
while not done:
    number = number + 1
    if number == 1:
       continue
    if number == 2:
        summer = summer + number
        count = count + 1
    if number % 2 != 0: 
        if is_prime(number):
            summer = summer + number
            count = count + 1
    if count == limit:
        done = True

print summer
