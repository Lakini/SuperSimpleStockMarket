from models.trade import Trade
from models.stock import Stock
import datetime

#Create stocks
s1 = Stock("TEA",Stock.StockType.COMMON,0,100)
s2 = Stock("POP",Stock.StockType.COMMON,8,100)
s3 = Stock("ALE",Stock.StockType.COMMON,23,60)
s4 = Stock("GIN",Stock.StockType.PREFERRED,8,100,2)
s5 = Stock("JOE",Stock.StockType.COMMON,13,250)

'''
Calculate Dividend yeild
@param stock:
@param price:
'''
def calculate_dividend_yield(stock, price):
    try:
        if(stock.type == Stock.StockType.COMMON):
            dividend_yield = stock.get_dividend_yield_common(price)
            print("Dividend yeild is %f" %dividend_yield)
        else:
            dividend_yield = stock.get_dividend_yield_preferred(price)
            print("Dividend yeild is %f" %dividend_yield)
        
    except ValueError as e:
        print(e)
    except Exception as e:
        print("Error in calculating divident yeild: %s" %e)

'''
Calculate PE Ratio
@param stock:
@param price:
'''
def calculate_pe_ratio(stock, price):
    try:
        pe_ratio = stock.get_pe_ratio(price)
        print("PE Ratio is %f" %pe_ratio)
    except ValueError as e:
        print(e)
    except Exception as e:
        print("Error in calculating PE Ratio: %s" %e)

'''
Create trades for the given stock
@param stock:
@param no_of_shares:
@param trade_type:
@param trade_price
'''
def create_trades(stock, no_of_shares, trade_type, trade_price):
    try:
        trade = Trade(no_of_shares, trade_type, trade_price)
        stock.add_trades(trade)
    except ValueError as e:
        print(e)
    except Exception as e:
        print("Error in creating trades for the given stock: %s" %e)

'''
Get trades for the  last 15 mins
@param stock:
'''
def get_trades(stock):
    period_value = datetime.datetime.now() - datetime.timedelta(minutes = 15)
    filtered_trades = filter(lambda x: x.created_at > period_value, stock.trades)
    return list(filtered_trades)

'''
Calculate Volume weighted stock price
@param stock:
'''
def calculate_volume_weighted_stock_price(stock):
    try:
        latest_trades = get_trades(stock)
        volume_weighted_stock_price = stock.get_volume_weighted_stock_price(latest_trades)
        print("Volume Weighted Stock Price is %f" %volume_weighted_stock_price)
    except ValueError as e:
        print(e)
    except Exception as e:
        print("Error in calculating volume weighted Stock price: %s" %e)

'''
Calculate all share index
@param stock_list:
'''
def calculate_all_share_index(stock_list):
    try:
        all_stock_price_list = []
        for stock in stock_list:
            total = 0
            for trade in stock.trades:
                #Assumption : Considering the price for all stock as the total of trade price for the given stock
                total = total + (trade.traded_price)
            if len(stock.trades) > 0 :
                all_stock_price_list.append(total)

        all_share_index = Stock.get_all_share_index(all_stock_price_list)
        print("All Share Index price is %f" %all_share_index)
    except ValueError as e:
        print(e)
    except Exception as e:
        print("Error in calculating volume weighted Stock price: %s" %e)

#1.a.i
calculate_dividend_yield(s2, 460)
calculate_dividend_yield(s4, 460)

#1.a.ii
calculate_pe_ratio(s3, 523)

#1.a.iii
create_trades(s1,5, Trade.TradeType.SELL, 545768)
create_trades(s1,6, Trade.TradeType.SELL, 56473798)
create_trades(s1,6, Trade.TradeType.SELL, 54654345)
create_trades(s1,6, Trade.TradeType.SELL, 665445656)
create_trades(s2,8, Trade.TradeType.SELL, 6554334)
create_trades(s5,124, Trade.TradeType.SELL, 123345523)

#1.a.iv
calculate_volume_weighted_stock_price(s1)

#1.b
calculate_all_share_index([s1,s2,s3,s4,s5])


