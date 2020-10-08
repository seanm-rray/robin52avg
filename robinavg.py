import robin_stocks as rs



rs.login(username= input("Username: "), #handles robinhood login. May prompt for SMS code
         password= input("Password: "),
         expiresIn=86400,
         by_sms=True)

stock_owned = rs.account.get_open_stock_positions(info='instrument') #Returns the url for each stock owned in a list

#instance variables
list_hist = [] 
list_avg = []
ticker_stock = []
count = 0;
count2 = 0;

#Return the symbol as a string for each stock owned
for i in stock_owned:
    ticker_stock.append(rs.stocks.get_symbol_by_url(i))

#Return the daily close price for each stock in a list of lists
for j in ticker_stock:
   list_hist.append(rs.stocks.get_stock_historicals(j, interval='day', span='year', bounds='regular', info='close_price'))   

#Convert prices from strings to floats      
for k in list_hist:
   list_hist[count] = list(map(float, k))
   count = count + 1

#Compute 52 week averages   
for price_list in list_hist:
    list_avg.append((sum(price_list)/(len(price_list))))

#Print table
for ticker in ticker_stock:
    t_list = rs.stocks.get_latest_price(ticker, priceType=None, includeExtendedHours=True)
    
    print(ticker + "\nCurrent Price: " + t_list[0])
    print("52 Week Average: ")
    print(round(list_avg[count2], 2) )
    print("\n")
    
    count2 = count2 + 1
