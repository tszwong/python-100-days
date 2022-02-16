import random
print("Coin Flip")

coin_flip_result = random.randint(0,1)
if coin_flip_result == 0:
    print("Heads")
else:
    print("Tails")