from matplotlib import pyplot as plt
import tkinter as tk

def plot(x=[], y=[]):
    plt.plot(x, y, 'o', color="green")
    plt.rcParams["figure.autolayout"] = True
    plt.xlabel("Terms completed")
    plt.ylabel("Profit per term")
    plt.title("Profit-Per-Term in USDT")
    plt.show()

def submit(subAmu=0, termLen=0, apr=0, termAmu=0, targetPrice=0):
    #first, ensure input is readable and throw out bad data, possibly warning the user later on
    subAmu = float(subAmu)
    termLen = float(termLen)
    apr = float(apr) / 100 #remove imaginary %
    termAmu = int(termAmu)
    targetPrice = float(targetPrice)
    #error handling here
    #next, create plotting data
    x = range(termAmu)
    y = []
    for term in range(termAmu):
        subAmuUSDT = subAmu * targetPrice
        subAmu = subAmu * (1 + apr * termLen / 365) # stolen from kucoins dual investment page
        y.append((subAmu * targetPrice) - subAmuUSDT)
    plot(x, y)

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

    targetPriceInputLabel = tk.Label(master=targetPriceFrame, text="Target Price:")
    targetPriceInputLabel.pack(side=tk.LEFT)
    targetPriceInputEntry = tk.Entry(master=targetPriceFrame)
    targetPriceInputEntry.pack()

    # packing frames
    subAmuFrame.pack(anchor='w')
    termLenFrame.pack(anchor='w')
    aprFrame.pack(anchor='w')
    termAmuFrame.pack(anchor='w')
    targetPriceFrame.pack(anchor='w')

    # go button
    submitButton = tk.Button(text="Visualize!", width="10", height="2", font=("Times New Roman", 16), command=lambda : submit(subAmuInputEntry.get(), termAmuInputEntry.get(), aprInputEntry.get(), termAmuInputEntry.get(), targetPriceInputEntry.get()))
    submitButton.pack(anchor='s')

    root.mainloop() #listen for input

initGUI()

# SUMMARY
# -- INPUTS NEEDED --
# 1: Currency Preffered To Visualize (example: if the user prefers ETH over USDT, use the ETH value)
# 2: Subscribed Amount
# 3: Reference APR
# 4: Term length
# 5: Total Terms to visualize
# -- OUTPUTS NEEDED --
# 1: A Plotted Graph of how much profit will be made after each reccuring term assuming full reinvnestment.