
import sys

if len(sys.argv)!=2:
    print("Enter atleast one arugument")
else:
    N=int(sys.argv[1])

    if N<0:
        print("Enter the value above 0")
    else:
        harmonic=0.0
        for i in range(1,N+1):
            harmonic +=1/i
        print(f"{N} Harmonic number is :{harmonic:.4f}")