# read n space separated integers from user and print the multiples of 3 and 7
n=int(input())
nums=input().split()[:n] # n space chars
for num in nums: # chars
    if int(num)%3==0 and int(num)%7==0:
        print(num,end=" ")
