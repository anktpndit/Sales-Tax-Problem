
#!/usr/bin/python3

# Problem 1: SALES TAX
import ast
import re

# macro variables
SALES_TAX = 10
IMPORT_TAX = 5

class Extra:
    """This class holds all the important function used in the problem of Sales Tax"""
    @staticmethod
    def lineReader(filename, basket_goods):
        """This function reads from the purchase.txt file and adds them into the basket"""
        with open(filename,'r') as file:
            for (lineNum, line) in enumerate(file):
                line = line.rstrip()
                print(line)
                # using regex to check if pattern of the string matches to the required format
                if bool(re.fullmatch(r"^\d+(.*)\bat\b \d+.\d\d : (book|food|med|other)$", line)):
                    basket_goods.addGood(Good(line))
                else:
                    raise ValueError(f"Use the correct string pattern at line {lineNum+1} in the purchase.txt file!")
        
        return basket_goods.getBasket()

    @staticmethod
    def round_nearest(value, nearestOf = 0.05):
        """This function rounds values to nearest 0.05."""
        return round(round(value/nearestOf) * nearestOf,2)
    
class Good:
    """Good class represent the good that are bought"""
    exempt = ["book", "food", "med"]

    def __init__(self, input):
        input = input.split(" ")
        self._quantity= int(input[0])
        self._itemName = input[1:-4]
        self._price = ast.literal_eval(input[-3])
        self._category = input[-1]
        
    @property 
    def _imported(self):
        if "imported" in self._itemName:
            return True
        else:
            return False

    #getters
    def getPrice(self):
        return self._price

    def getQuantity(self):
        return self._quantity

    def getItemName(self):
        return self._itemName

    def isImported(self):
        return self._imported
    
    def getCategory(self):
        return self._category

    # method for calculating sales tax of a good
    def SalesTax(self):
        salesTax = 0
        goodPrice = self.getPrice()
        # !!!! change this if exempt 0 else 10%, and then import then add 5%
        if self.getCategory() in Good.exempt:
            salesTax=0
        else:
            salesTax = Extra.round_nearest(goodPrice*(SALES_TAX/100))

        if self.isImported():
            salesTax += Extra.round_nearest(goodPrice*(IMPORT_TAX/100))
        return salesTax

class Basket:
    """Basket contains all the goods purchased"""
    def __init__(self):
        self._basketArr = []
        self._totalSalesTax = 0
        self._totalPrice = 0

    """Calculating our receipt from the basket"""
    def getReceipt(self):
        receipt = []
        for good in self._basketArr:
            salesTax = good.SalesTax()
            valueIncTax = good.getPrice()+salesTax
            stringExp = ' '.join(good.getItemName())
            receipt.append(str(good.getQuantity()) + ' ' + stringExp + ': %.2f' % valueIncTax)
            self._totalSalesTax += salesTax
            self._totalPrice += valueIncTax

        #decimal are calculated as floating point number so we need to round them again
        self._totalSalesTax = round(self._totalSalesTax,2)
        self._totalPrice = round(self._totalPrice,2)
        return ('\n').join(receipt)

    #setters
    def addGood(self, good):
        if isinstance(good,Good):
            self._basketArr.append(good)
            return self
        else:
            raise ValueError(f"Type {type(good)} cannot be added to the basket! Instance of Good Class can only be added!")

    #getters
    def getBasket(self):
        return self._basketArr

if __name__== "__main__":

    for i in range(1,4):
        # making a basket for the purchased goods
        basket_goods = Basket()

        # reading the purchase.txt file and printing the receipt
        print("\n-----------------\nInput\n-----------------")
        Extra.lineReader(f'purchase{i}.txt',basket_goods)
        print("\n-----------------\nOutput\n-----------------")
        print(basket_goods.getReceipt() + '\nSales Taxes: %.2f\nTotal: %.2f' % (basket_goods._totalSalesTax,basket_goods._totalPrice))
