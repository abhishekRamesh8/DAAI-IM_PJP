def prime(num):
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not Prime")
            break
    else:
        print(f"{num} is Prime")


prime(int(input()))
