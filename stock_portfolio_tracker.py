import yfinance as yf

portfolio = {}

def add_stock(symbol, shares):
    if symbol in portfolio:
        portfolio[symbol] += shares
    else:
        portfolio[symbol] = shares
    print(f"Added {shares} shares of {symbol}.")

def remove_stock(symbol, shares):
    if symbol in portfolio:
        if portfolio[symbol] > shares:
            portfolio[symbol] -= shares
            print(f"Removed {shares} shares of {symbol}.")
        elif portfolio[symbol] == shares:
            del portfolio[symbol]
            print(f"Removed all shares of {symbol}.")
        else:
            print("You don't own that many shares.")
    else:
        print("You don't own this stock.")

def show_portfolio():
    if not portfolio:
        print("Your portfolio is empty.")
        return
    
    print("\nYour Portfolio:")
    total_value = 0
    for symbol, shares in portfolio.items():
        stock = yf.Ticker(symbol)
        data = stock.history(period="1d")
        price = data['Close'][0]
        value = price * shares
        total_value += value
        print(f"{symbol}: {shares} shares × ${price:.2f} = ${value:.2f}")
    print(f"Total Portfolio Value: ${total_value:.2f}\n")

def main():
    while True:
        print("\nOptions: add, remove, view, quit")
        choice = input("What would you like to do? ").strip().lower()
        
        if choice == "add":
            symbol = input("Enter stock symbol (e.g., AAPL): ").upper()
            shares = int(input("Enter number of shares: "))
            add_stock(symbol, shares)
        
        elif choice == "remove":
            symbol = input("Enter stock symbol to remove: ").upper()
            shares = int(input("Enter number of shares to remove: "))
            remove_stock(symbol, shares)

        elif choice == "view":
            show_portfolio()
        
        elif choice == "quit":
            print("Exiting portfolio tracker. Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()