import unittest
from models.stock import Stock
from models.trade import Trade

class TestStockValueCalculator(unittest.TestCase):
    def test_dividend_yield_common(self):
        testStock = Stock("ALE", Stock.StockType.COMMON, 23, 60)
        self.assertAlmostEqual(testStock.get_dividend_yield_common(100), 0.23)
        self.assertAlmostEqual(testStock.get_dividend_yield_common(50.78), 0.45293423)
    
    def test_dividend_yield_common_input_values(self):
        testStock = Stock("ALE", Stock.StockType.COMMON, 23, 60)
        self.assertRaises(ValueError, testStock.get_dividend_yield_common, -100)
        self.assertRaises(ValueError, testStock.get_dividend_yield_common, 0)
        self.assertRaises(TypeError, testStock.get_dividend_yield_common, "5.67")
        self.assertRaises(TypeError, testStock.get_dividend_yield_common, [5.67])
        self.assertRaises(TypeError, testStock.get_dividend_yield_common)
    
    def test_dividend_yield_preferred(self):
        testStock = Stock("GIN", Stock.StockType.PREFERRED, 8, 100, 2)
        self.assertAlmostEqual(testStock.get_dividend_yield_preferred(100), 2)
        self.assertAlmostEqual(testStock.get_dividend_yield_preferred(4567234), 0.00004379)
    
    def test_dividend_yield_preferred_input_values(self):
        testStock = Stock("GIN", Stock.StockType.PREFERRED, 8, 100, 2)
        self.assertRaises(ValueError, testStock.get_dividend_yield_preferred, -100)
        self.assertRaises(ValueError, testStock.get_dividend_yield_preferred, 0)
        self.assertRaises(ValueError, testStock.get_dividend_yield_preferred, -56)
        self.assertRaises(TypeError, testStock.get_dividend_yield_preferred, "89")
        self.assertRaises(TypeError, testStock.get_dividend_yield_preferred, [5.67])
        self.assertRaises(TypeError, testStock.get_dividend_yield_preferred)
    
    def test_pe_ratio(self):
        testStock = Stock("ALE", Stock.StockType.COMMON, 23, 60)
        self.assertAlmostEqual(testStock.get_pe_ratio(100), 4.3478260869565215)
        self.assertAlmostEqual(testStock.get_pe_ratio(50.78), 2.20782609)
    
    def test_pe_ratio_input_values(self):
        testStock = Stock("ALE", Stock.StockType.COMMON, 23, 60)
        self.assertRaises(ValueError, testStock.get_pe_ratio, -100)
        self.assertRaises(TypeError, testStock.get_pe_ratio,"5.67")
        self.assertRaises(TypeError, testStock.get_pe_ratio,[5.67])
        self.assertRaises(TypeError, testStock.get_pe_ratio)
    
    def test_get_all_share_index(self):
        share_price_list = [777119567, 6554334, 123345523]

        self.assertAlmostEqual(Stock.get_all_share_index(share_price_list), 85647219.40492451)
    
    def test_get_all_share_index_input_values(self):
        self.assertRaises(ValueError, Stock.get_all_share_index,[])
        self.assertRaises(TypeError, Stock.get_all_share_index)
    
    def test_create_stock_input_values(self):
        testStock = Stock("ALE", Stock.StockType.COMMON, 23, 60)

        self.assertAlmostEqual(testStock.stock_symbol,"ALE")
        self.assertAlmostEqual(testStock.type,Stock.StockType.COMMON)
        self.assertRaises(TypeError, Stock.__init__,Stock('TEST',Stock.StockType.COMMON,"67ytr",8765))
        self.assertRaises(TypeError, Stock.__init__,Stock('TEST',Stock.StockType.COMMON,[],8765))
        self.assertRaises(TypeError, Stock.__init__,Stock('TEST',Stock.StockType.COMMON,87677,"8765"))
        self.assertRaises(TypeError, Stock.__init__,Stock('TEST',Stock.StockType.COMMON,87677,8765,[]))
    