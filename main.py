from matplotlib import pyplot as plt
import tkinter as tk

def plot(x=[], y=[]):
    #TODO: make plot function
    plt.plot(profitListX, profitListY, 'o', color="green")
    plt.rcParams["figure.autolayout"] = True
    plt.xlabel("Terms completed")
    plt.ylabel("Profit per term")
    plt.title("Profit-Per-Term in USDT")
    plt.show()

def initGUI():
    root = tk.Tk() #create root window
    root.resizable(False, False)
    root.title("KuCoin POT Visualizer")
    #title text
    title = tk.Label(text="Kucoin Profit-Over-Time(POT) Visualizer", font=("Times New Roman", 22))
    title.pack()

    # frames
    subAmuFrame = tk.Frame(relief="groove", borderwidth=5)
    termLenFrame = tk.Frame(relief="groove", borderwidth=5)
    aprFrame = tk.Frame(relief="groove", borderwidth=5)
    termAmuFrame = tk.Frame(relief="groove", borderwidth=5)
    targetPriceFrame = tk.Frame(relief="groove", borderwidth=5)

    #frame content
    subAmuInputLabel = tk.Label(master=subAmuFrame, text="Subscribed Amount (Any Currency, Numbers Only):")
    subAmuInputLabel.pack(side=tk.LEFT)
    subAmuInputEntry = tk.Entry(master=subAmuFrame)
    subAmuInputEntry.pack()

    termLenInputLabel = tk.Label(master=termLenFrame, text="Term Length (in days):")
    termLenInputLabel.pack(side=tk.LEFT)
    termLenInputEntry = tk.Entry(master=termLenFrame)
    termLenInputEntry.pack()

    aprInputLabel = tk.Label(master=aprFrame, text="Reference APR:")
    aprInputLabel.pack(side=tk.LEFT)
    aprInputEntry = tk.Entry(master=aprFrame)
    aprInputEntry.pack()

    termAmuInputLabel = tk.Label(master=termAmuFrame, text="Amount of Reccuring Terms:")
    termAmuInputLabel.pack(side=tk.LEFT)
    termAmuInputEntry = tk.Entry(master=termAmuFrame)
    termAmuInputEntry.pack()

    targetPriceFrameInputLabel = tk.Label(master=targetPriceFrame, text="Target Price:")
    targetPriceFrameInputLabel.pack(side=tk.LEFT)
    targetPriceFrameInputEntry = tk.Entry(master=targetPriceFrame)
    targetPriceFrameInputEntry.pack()

    # packing frames
    subAmuFrame.pack(anchor='w')
    termLenFrame.pack(anchor='w')
    aprFrame.pack(anchor='w')
    termAmuFrame.pack(anchor='w')
    targetPriceFrame.pack(anchor='w')

    # go button
    submitButton = tk.Button(text="Visualize!", width="10", height="2", font=("Times New Roman", 16))
    submitButton.pack(anchor='s')

    root.mainloop() #listen for input

initGUI()

# inputs
#TODO: GUI Stuff
# OPTIONAL
#calsCurrency = input("What currency are you investing? ") # string
#visCurrency = input("What currency are you visualizing? ") # string
# OPTIONAL
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
    #print(str((subAmount * targetPrice) - subAmountToUSDT)) # print the increase in profit each iteration by finding the new subAmountToUSDT then subtracting that by the previously found one.

profitListX = []

for j in range(termAmu):
    profitListX.append(j+1)


plot(profitListX, profitListY)

# SUMMARY
# -- INPUTS NEEDED --
# 1: Currency Preffered To Visualize (example: if the user prefers ETH over USDT, use the ETH value)
# 2: Subscribed Amount
# 3: Reference APR
# 4: Term length
# 5: Total Terms to visualize
# -- OUTPUTS NEEDED --
# 1: A Plotted Graph of how much profit will be made after each reccuring term assuming full reinvnestment.