def finder_fake_coin(Coins,beginning,last):

    mid = int((beginning + last) / 2)

    if((last-beginning)%2 == 0):
        if (last - beginning - 1) == 1:
            if Coins[last] == Coins [beginning]:
                return beginning+1
            elif Coins[last] == Coins [beginning+1]:
                return beginning
            else:
                return last
        else:
            Lsum = 0
            Rsum = 0
            for i in range(beginning, mid):
                Lsum = Lsum + Coins[i]
            for i in range(mid, last):
                Rsum = Rsum + Coins[i]

            if Lsum == Rsum:
                return last
            elif Lsum>Rsum:
                return finder_fake_coin(Coins, beginning, mid-1)
            else:
                return finder_fake_coin(Coins, mid, last-1)

    else:
        if (last-beginning) == 1:
            if Coins[beginning]>Coins[last]:
                return beginning
            else:
                return last
        else:
            Lsum = 0
            Rsum = 0
            for i in range(beginning, mid):
                Lsum = Lsum + Coins[i]
            for i in range(mid, last):
                Rsum = Rsum + Coins[i]

            if Lsum>Rsum:
                return finder_fake_coin(Coins,beginning,mid)
            else:
                return finder_fake_coin(Coins,mid+1,last)

print("-------------------------------------------------")
coins = [2,2,2,2,3]
fakeCoin = finder_fake_coin(coins,0,len(coins)-1)
print(coins)
print("Fake Coin Index -> {} \nFake Coin Weight -> {}".format(fakeCoin,coins[fakeCoin]))
print("-------------------------------------------------")

print("-------------------------------------------------")
coins = [3,2,2,2,2]
fakeCoin = finder_fake_coin(coins,0,len(coins)-1)
print(coins)
print("Fake Coin Index -> {} \nFake Coin Weight -> {}".format(fakeCoin,coins[fakeCoin]))
print("-------------------------------------------------")

print("-------------------------------------------------")
coins = [2,2,2,2,2,2,2,2,2,2,2,2,2,3,2]
fakeCoin = finder_fake_coin(coins,0,len(coins)-1)
print(coins)
print("Fake Coin Index -> {} \nFake Coin Weight -> {}".format(fakeCoin,coins[fakeCoin]))
print("-------------------------------------------------")

print("-------------------------------------------------")
coins = [3,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
fakeCoin = finder_fake_coin(coins,0,len(coins)-1)
print(coins)
print("Fake Coin Index -> {} \nFake Coin Weight -> {}".format(fakeCoin,coins[fakeCoin]))
print("-------------------------------------------------")

