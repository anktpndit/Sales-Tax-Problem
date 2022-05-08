import unittest
import salesTax

class Good(unittest.TestCase):
    """This class tests whether goods are setup correctly or not"""

    test_good1 = salesTax.Good('1 music CD at 14.99 : other')
    test_good2 = salesTax.Good('1 imported music CD at 14.99 : other')
    test_good3 = salesTax.Good('1 book at 12.49 : book')
    test_good4 = salesTax.Good('1 imported book at 12.49 : book')

    def test_SalesTax(self):
        self.assertEqual(self.test_good1.SalesTax(),1.50)
        self.assertEqual(self.test_good2.SalesTax(),2.25)
        self.assertEqual(self.test_good3.SalesTax(),0) #make this 0
        self.assertEqual(self.test_good4.SalesTax(),0.60) #make this only 5% since exempt+import

class Basket(unittest.TestCase):
    """This class tests whether Basket is setup correctly or not"""
    
    def test_BasketTotal1(self):
        test_basket1 = salesTax.Basket()
        test_basket1.addGood(salesTax.Good('1 book at 12.49 : book')).addGood(salesTax.Good('1 music CD at 14.99 : other')).addGood(salesTax.Good('1 chocolate bar at 0.85 : food'))
        test_basket1.getReceipt()
        self.assertEqual(len(test_basket1.getBasket()),3)
        self.assertEqual(test_basket1._totalSalesTax,1.50)
        self.assertEqual(test_basket1._totalPrice,29.83)

    def test_BasketTotal2(self):
        test_basket2 = salesTax.Basket()
        test_basket2.addGood(salesTax.Good('1 imported box of chocolates at 10.00 : food')).addGood(salesTax.Good('1 imported bottle of perfume at 47.50 : other'))
        test_basket2.getReceipt()
        self.assertEqual(len(test_basket2.getBasket()),2)
        self.assertEqual(test_basket2._totalSalesTax,7.65)
        self.assertEqual(test_basket2._totalPrice,65.15)

    def test_BasketTotal3(self):
        test_basket3 = salesTax.Basket()
        test_basket3.addGood(salesTax.Good('1 imported bottle of perfume at 27.99 : other')).addGood(salesTax.Good('1 bottle of perfume at 18.99 : other')).addGood(salesTax.Good('1 packet of headache pills at 9.75 : med')).addGood(salesTax.Good('1 box of imported chocolates at 11.25 : food'))
        test_basket3.getReceipt()
        self.assertEqual(len(test_basket3.getBasket()),4)
        self.assertEqual(test_basket3._totalSalesTax,6.65)
        self.assertEqual(test_basket3._totalPrice,74.63)

        
class Extra(unittest.TestCase):
    """This class tests all the important function used in the problem"""
    def test_lineReader(self):
        """Testing whether goods are read correctly and added into the basket or not"""
        with self.assertRaises(ValueError):
            salesTax.Extra.lineReader('test/test_purchase_error.txt', salesTax.Basket())

        # testing for a file with correct format of purchased goods
        self.assertEqual(len(salesTax.Extra.lineReader('test/test_purchase.txt', salesTax.Basket())),3)
        

    def test_round_nearest(self):
        """Testing whether values are rounded to nearest 0.05 or not"""
        test_values = [2.04, 2.07, -2.075, 2.05,-1.02, -1.15]
        val_values = [2.05, 2.05, -2.10, 2.05, -1.00,-1.15]
        for (i,val) in enumerate(test_values):
            self.assertEqual(salesTax.Extra.round_nearest(val),val_values[i])


if __name__ == '__main__':
    unittest.main()