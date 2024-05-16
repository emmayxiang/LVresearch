import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Normalize the numeric data using Min-Max scaling
def normalizeData(data):
    numericCols = data.select_dtypes(include=["number"])
    normalized_data = (numericCols - numericCols.min()) / (numericCols.max() - numericCols.min())
    return pd.concat([data.drop(columns = numericCols.columns), normalized_data], axis = 1)

equityTicker = "SPY"
cryptoTicker = "BTC-USD"

equitydf = normalizeData(pd.read_csv(equityTicker + "_data.csv", parse_dates = ["Date"]))
cryptodf = normalizeData(pd.read_csv(cryptoTicker + "_data.csv", parse_dates = ["Date"]))

# Plots the equity and crypto datasets
plt.figure(figsize=(20, 10))
plt.plot(equitydf["Date"], equitydf["Close Price"], label = f"{equityTicker} Close Price", color = "blue")
plt.plot(cryptodf["Date"], cryptodf["Close Price"], label = f"{cryptoTicker} Close Price", color = "red")

plt.title(f"{equityTicker} & {cryptoTicker} Time Series Plot")
plt.xlabel("Date")
plt.ylabel("Normalized Closing Price")
plt.legend(labels = [f"{equityTicker} Close Price", f"{cryptoTicker} Close Price"])
plt.grid(True)
plt.savefig(f"{equityTicker}_{cryptoTicker}_timeSeriesPlot.png")
plt.show()

# Rename columns to indicate equity and crypto
equitydf.rename(columns = {"Close Price": f"{equityTicker} Close Price"}, inplace = True)
cryptodf.rename(columns = {"Close Price": f"{cryptoTicker} Close Price"}, inplace = True)

# Calculate the correlation matrix
correlation_matrix = pd.concat([equitydf[f"{equityTicker} Close Price"], cryptodf[f"{cryptoTicker} Close Price"]], axis = 1).corr()

# Plot correlation matrix as heatmap
plt.figure(figsize=(20, 10))
sns.heatmap(correlation_matrix, annot = True, cmap = "coolwarm", fmt = ".5f", annot_kws = {"size": 10})
plt.title(f"{equityTicker} & {cryptoTicker} Correlation Matrix")
plt.savefig(f"{equityTicker}_{cryptoTicker}_correlationMatrix.png")
plt.show()