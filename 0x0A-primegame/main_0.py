#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner


print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
print("Ben")

print("Winner: {}".format(isWinner(3, [4, 5, 1])))
print("Ben")

print("Winner: {}".format(isWinner(10, [5, 5, 5, 5, 5, 2, 2, 2, 2, 2,])))
print("Maria")

print("Winner: {}".format(isWinner(0, [0])))
print("None")
