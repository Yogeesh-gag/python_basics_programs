import random

class CouponCollector:

    @staticmethod
    def generate_random_coupon(n):

        return random.randint(0,n-1)

    def collect_coupons(n):

        collected=set()
        count=0

        while len(collected)<n:
            coupon=CouponCollector.generate_random_coupon(n)
            count+=1
            collected.add(coupon)

        return count

n=int(input("Enter number of distinct coupons: "))

total_randoms=CouponCollector.collect_coupons(n)
print(f"\nTotal random numbers generated to collect all {n} coupons: {total_randoms}")