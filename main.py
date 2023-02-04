from matplotlib import pyplot as plt

# inputs
#TODO: allow other pairs besides ETH and USDT
#TODO: GUI Stuff
#TODO: Plot
#for now assume eth vis usdt, no dual support yet
calsCurrency = input("What currency are you investing? ") # string
visCurrency = input("What currency are you visualizing? ") # string
subAmount = float(input("How much did you subscribe with? ")) # float
termLength = float(input("How many days is each term? ")) # float
apr = float(input("What is the reference APR? ")) / 100 # float, remove %
termAmu = int(input("How many terms are you going to reccuringly reinvest for? ")) # int
targetPrice = int(input("What is the Target price? ")) # float

profitListY = []

for i in range(termAmu):
    subAmountToUSDT = subAmount * targetPrice
    subAmount = subAmount * (1 + apr * termLength / 365) # stolen from kucoins dual investment page
    profitListY.append((subAmount * targetPrice) - subAmountToUSDT)
    print(str((subAmount * targetPrice) - subAmountToUSDT)) # print the increase in profit each iteration by finding the new subAmountToUSDT then subtracting that by the previously found one.

profitListX = []

for j in range(termAmu):
    profitListX.append(j+1)

plt.plot(profitListX, profitListY)
plt.xlabel("Terms completed")
plt.ylabel("Profit per term")
plt.title("The Graph Title")
plt.show()

# SUMMARY
# -- INPUTS NEEDED --
# 1: Currency Preffered To Visualize (example: if the user prefers ETH over USDT, use the ETH value)
# 2: Subscribed Amount
# 3: Reference APR
# 4: Term length
# 5: Total Terms to visualize
# -- OUTPUTS NEEDED --
# 1: A Plotted Graph of how much profit will be made after each reccuring term assuming full reinvnestment.