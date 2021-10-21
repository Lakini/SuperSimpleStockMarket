from datetime import datetime

class Trade:
    class TradeType:
        SELL = "SELL"
        BUY = "BUY"
        
        ALL = [
            (SELL, "Selling"),
            (BUY, "Buying")
        ]
    
    allowed_types = [int, float]

    def __init__(self, no_of_shares, trade_type, traded_price ):
        if trade_type not in [Trade.TradeType.SELL, Trade.TradeType.BUY] :
            raise ValueError("Invalid Trade type")

        if not any(elem in [type(no_of_shares),type(traded_price)] for elem in self.allowed_types) :
            raise TypeError("No of shares and traded price should be int or float type values")

        self.created_at = datetime.now(tz=None)
        self.no_of_shares = no_of_shares
        self.type = type
        self.traded_price = traded_price





