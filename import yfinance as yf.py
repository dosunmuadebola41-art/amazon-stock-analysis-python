import yfinance as yf
import matplotlib.pyplot as plt
from textwrap import fill

# ----------- Helper Functions -----------

def print_section(title):
    print("\n" + "="*60)
    print(title)
    print("="*60)

def show_news(stock):
    print_section("📢 Latest News")
    try:
        news = stock.news
        if not news:
            print("No news found.")
            return

        for i, article in enumerate(news[:5], start=1):
            print(f"\n[{i}] {article.get('title')}")
            print(f"Source: {article.get('publisher')}")
            print(f"Link: {article.get('link')}")
            if article.get("summary"):
                print(fill("Summary: " + article["summary"], width=80))

    except Exception as e:
        print("Error fetching news:", e)


def show_basic_info(info):
    print_section("📊 Company Information")
    fields = [
        ("Name", "longName"),
        ("Sector", "sector"),
        ("Market Cap", "marketCap"),
        ("Current Price", "currentPrice"),
        ("Day High", "dayHigh"),
        ("52w High", "fiftyTwoWeekHigh"),
        ("52w Low", "fiftyTwoWeekLow")
    ]
    for label, key in fields:
        print(f"{label}: {info.get(key)}")


def show_financials(stock):
    print_section("📒 Financial Statements Preview")

    try:
        print("\n--- Balance Sheet ---")
        print(stock.balance_sheet.head())

        print("\n--- Income Statement ---")
        print(stock.income_stmt.head())

        print("\n--- Cashflow Statement ---")
        print(stock.cashflow.head())
    except Exception as e:
        print("Error loading financials:", e)


def plot_chart(stock):
    print_section("📈 Chart Options")
    print("1. Close Price (6mo)\n2. OHLC Plot (6mo)\n3. Volume (6mo)\n")

    choice = input("Choose a chart (1/2/3): ")

    hist = stock.history(period="6mo")
    plt.style.use("Solarize_Light2")
    plt.figure(figsize=(10, 6))

    if choice == "1":
        plt.plot(hist["Close"], label="Close", color="#00ff88")
        plt.title("Close Price (6 months)")

    elif choice == "2":
        plt.plot(hist["Open"], label="Open", color="#ff3388")
        plt.plot(hist["Close"], label="Close", color="#00ff88")
        plt.plot(hist["High"], label="High", color="#00ccff")
        plt.plot(hist["Low"], label="Low", color="#ffaa00")
        plt.title("OHLC (6 months)")

    elif choice == "3":
        plt.bar(hist.index, hist["Volume"], color="#8888ff")
        plt.title("Volume (6 months)")

    else:
        print("Invalid selection.")
        return

    plt.legend()
    plt.tight_layout()
    plt.show()


# ----------- Main Program -----------

print_section("📌 Interactive Stock Analyzer with News")

ticker = input("Enter a stock ticker symbol (e.g., AMZN, AAPL, TSLA): ").upper()

stock = yf.Ticker(ticker)

try:
    info = stock.get_info()
except Exception:
    print("Invalid ticker or data unavailable.")
    exit()

show_basic_info(info)
show_financials(stock)
show_news(stock)

plot_chart(stock)

print_section("✅ All Done!")
