import sys

if len(sys.argv)!=2:
    print("Please enter atleast two argument ")
else:
    N=int(sys.argv[1])

    if  0<=N<=31:
        print(f"Enter the value of 2 to the power of {N}")
        for i in range(N+1):
            print(f"2^{N}={2**i}")
    else:
        print("please enter the value in between 0 to 31")