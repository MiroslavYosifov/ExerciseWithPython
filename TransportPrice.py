km = int(input())
dayOrNigth = input()

if km < 20:
    if dayOrNigth == "day":
        priceWichTaxi = 0.70 + 0.79 *km
        print(priceWichTaxi)
    elif dayOrNigth == "night":
        priceWichTaxi = 0.70 + 0.90 * km
        print(priceWichTaxi)
elif km >= 20 and km < 100:
    if dayOrNigth == "day":
        priceWichAvtobus = 0.09 * km
        print(priceWichAvtobus)
    elif dayOrNigth == "night":
        priceWichAvtobus = 0.09 * km
        print(priceWichAvtobus)
else:
    if dayOrNigth == "day":
        priceWichTrain = 0.06  * km
        print(priceWichTrain)
    elif dayOrNigth == "night":
        priceWichTrain = 0.06  * km
        print(priceWichTrain)


