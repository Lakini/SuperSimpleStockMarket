import numpy as np

class Stock:
    class StockType:
        COMMON = "COMMON"
        PREFERRED = "PREFERRED"
        
        ALL = [
            (COMMON, "Common"),
            (PREFERRED, "Preferred")
        ]
    allowed_types = [int, float]

    def __init__(self, stock_symbol, stock_type, last_dividend, par_value, fixed_dividend = None):
        if stock_type not in [Stock.StockType.COMMON, Stock.StockType.PREFERRED] :
            raise ValueError("Invalid Stock type")

        if not any(elem in [type(last_dividend),type(par_value)] for elem in self.allowed_types) :
            raise TypeError("Last devidend and par values  should be int or float type values")

        if fixed_dividend and type(fixed_dividend) not in self.allowed_types:
            raise TypeError("Fixed devidend should be int or float type value")

        self.stock_symbol = stock_symbol
        self.last_dividend = last_dividend
        self.type = stock_type
        self.fixed_dividend = fixed_dividend
        self.par_value = par_value,
        self.trades = []

    '''
    Add trades to the given stock
    @param trade:
    '''
    def add_trades(self,trade):
        self.trades.append(trade)

    '''
    Get dividend yeild for Common Type
    @param price:
    @return dividend_yield:
    '''
    def get_dividend_yield_common(self, price):

        if type(price) not in [int, float]:
            raise TypeError("The type of price can only be a Float or Int types")
 
        if self.last_dividend < 0.0:
            raise ValueError("Last dividend cannot be a minus value")
        elif price <= 0.0:
            raise ValueError('Price cannot be zero or minus value')

        return self.last_dividend/price

    '''
    Get dividend yeild for Preferred Type
    @param price:
    @return dividend_yield:
    '''
    def get_dividend_yield_preferred(self, price):
        if type(price) not in [int, float]:
            raise TypeError("The type of price can only be a Float or Int types")

        # Assumption: fixed_dividend is considered without the ratio value.example 2 as the fixed_dividend in 2%
        if self.fixed_dividend < 0.0 :
            raise ValueError("Fixed Dividend cannot be a minus value")
        elif self.par_value[0] < 0.0 :
            raise ValueError("Par Value cannot be a minus value")
        elif price <= 0:
            raise ValueError("Price cannot be zero or minus value")

        return (self.fixed_dividend * self.par_value[0])/price

    '''
    Get P/E Ratio
    @param price:
    @return pe_ratio:
    '''
    def get_pe_ratio(self, price):

        if type(price) not in [int, float]:
            raise TypeError("The type of price can only be a Float or Int types")

        # Assumption: dividend used in the given formula is last devidend
        if self.last_dividend <= 0.0 :
            raise ValueError("Dividend cannot be zero or minus value")
        elif price < 0.0 :
            raise ValueError("Par Value cannot be a minus value")

        return price/self.last_dividend

    '''
    Get Volume Weighted Stock Price
    @param traded_list:
    @return volume_weighted_stock_price:
    '''
    def get_volume_weighted_stock_price(self, trade_list):

        if not trade_list:
            raise ValueError("Trade list for past 15 mins cannot be null")

        total_quantity, total_quantity_price = 0,0
        for trade in trade_list:
            total_quantity = total_quantity + trade.no_of_shares
            total_quantity_price = total_quantity_price + (trade.traded_price * trade.no_of_shares)
        
        return total_quantity_price/total_quantity
        #return (np.cumsum(np.multiply(price_list , quantity_list))/ np.cumsum(quantity_list))

    '''
    Get All Share Index
    @param share_prices:
    @return all_share_index:
    '''
    @staticmethod
    def get_all_share_index(share_prices):
        if not share_prices:
            raise ValueError("Share_prices array cannot be null")

        log_share_prices = np.log(share_prices)
        return np.exp(log_share_prices.mean())