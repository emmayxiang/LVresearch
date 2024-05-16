import yfinance as yf
import matplotlib.pyplot as plt
import csv

# Gets equity data into data frame
def getEquityData(ticker, startDate, endDate):
    equityData = yf.download(ticker, start=startDate, end=endDate)
    return equityData

# Gets crypto data into data frame
def getCryptoData(ticker, startDate, endDate):
    # Ensure correct formatting
    if ticker[-4:] != "-USD":
        ticker += "-USD"
    cryptoData = yf.download(ticker, start=startDate, end=endDate)
    return cryptoData, ticker

# Plots data onto graph
def plot(ticker, data):
    # Create a figure and axis
    fig, ax1 = plt.subplots(figsize=(20, 10))
    ax2 = ax1.twinx()

    # Plotting closing prices on the left axis
    ax2.plot(data["Close"], label = "Close Prices", color = "blue")
    ax2.set_xlabel("Date")
    ax2.set_ylabel("Close Prices", color = "blue")
    ax2.set_title(f"{ticker} Closing Prices Over Time")

    # Save and show the plot
    plt.savefig(f"{ticker}.png")
    plt.show()

# Saves data to csv file
def file(ticker, data):
    # Save data to CSV
    fileName = f"{ticker}_data.csv"
    with open(fileName, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Date', 'Close Price'])
        for date, close_price in zip(data.index, data['Close']):
            csv_writer.writerow([date.strftime('%Y-%m-%d'), close_price])
    print(f"Data saved to {fileName}.")

# User request for equity or crypto data
type = input("Equity or Crypto (E/C): ").upper()
while type != "E" and type != "C":
    type = input("Equity or Crypto (E/C): ").upper()

# User request for ticker and time frame
ticker = input("Ticker: ").upper()
startDate = input("Start date (YYYY-MM-DD): ")
endDate = input("End date (YYYY-MM-DD): ")

if type == "E":
    data = getEquityData(ticker, startDate, endDate)
else:
    data, ticker = getCryptoData(ticker, startDate, endDate)

plot(ticker, data)
file(ticker, data)