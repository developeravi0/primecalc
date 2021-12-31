def primecalc():
    print("Activated prime numbers calculator")
    def prime(x,y):
        prime_list = []
        for i in range(x,y):
            if i==0 or i==1:
                continue
            else:
                for j in range(2, int(i/2)+1):
                    if i%j ==0:
                        break
                else:
                    prime_list.append(i)
        return prime_list
    starting_range=int(input("Enter starting number : "))
    ending_range=int(input("Enter ending number : "))
    primenumbers=prime(starting_range,ending_range)
    length=len(primenumbers)
    if length==0:
        print("There is no prime number in the range you specified")
    else:
        print(f"The prime numbers in the given range are : {primenumbers}")
    print("Exited prime numbers calculator")
if __name__=="__main__":
    primecalc()