wants_backup = (int(input("0 for no backup, 1 for backup: ")))
if wants_backup:
    with open("primes_backup.txt", 'w') as backup:
        with open("primes.txt", 'r') as primes:
            backup.write(primes.read())
#exit(0) 
want_see = False
import math
from os import system
with open("primes.txt", 'r') as primes:
    prime_list = primes.read()
    prime_list.replace(',', '')
    prime_list.replace('\n', ' ')
    prime_list2 = []
    for i in prime_list.split():
        prime_list2.append(int(i[:-1]))


with open("primes.txt", "a") as primes:
        nums = list(range(prime_list2[-1]+1,prime_list2[-1]*4))
        #big_sqrt = math.isqrt(prime_list2[-1]*4)
        
        idx = 1
        length = len(prime_list2)
        newnums = []

        for j in nums:
            if all(j % i != 0 for i in prime_list2 if i <= j/2 + 1):
                newnums.append(j)

        prime = prime_list2[-1]

        while newnums:
            prime = newnums[0]
            primes.write(f"{prime}, ")
            idx += 1
            if want_see:
                length += 1
            
            #prime_list2.append(prime)
            if idx >= 10:
                primes.write("\n")
                idx = 1
            if length == 100 and want_see:
                length = 0
                print("There rests", len(newnums), "numbers left to check")
                

            for i in newnums:
                if i % prime == 0:
                    newnums.remove(i)

wants_second_backup = int(input("Do you want to back up the newly created primes? (0 for no, 1 for yes) "))
if wants_second_backup:
    with open("primes_backup.txt", 'w') as backup:
        with open("primes.txt", 'r') as primes:
            backup.write(primes.read())
system('cls')