Basic sales tax is applicable at a rate of 10% on all goods, except books, food, and medical
products that are exempt. Import duty is an additional sales tax
applicable on all imported goods at a rate of 5%, with no exemptions. When I purchase items
I receive a receipt which lists the name of all the items and their price (including tax),
finishing with the total cost of the items,
and the total amounts of sales taxes paid. The rounding rules for sales tax are that for a tax
rate of n%, a shelf price of p contains (np/100 rounded up to the nearest 0.05) amount of
sales tax.

# Cloning and Running the file

1) Go to the terminal and clone the repository using the following command:

```
git clone https://github.com/anktpndit/Sales-Tax-Problem.git 
```

2) Cd into the cloned directory and run the test cases and the python script using the following command:

```
python3 test_salesTax.py 
python3 salesTax.py
```

Any purchase[1-3].txt file can be edited according to the purchases made and the receipt will be shown in the terminal.

# Output of salesTax.py

```
-----------------
Input
-----------------
1 book at 12.49 : book
1 music CD at 14.99 : other
1 chocolate bar at 0.85 : food

-----------------
Output
-----------------
1 book: 12.49
1 music CD: 16.49
1 chocolate bar: 0.85
Sales Taxes: 1.50
Total: 29.83

-----------------
Input
-----------------
1 imported box of chocolates at 10.00 : food
1 imported bottle of perfume at 47.50 : other

-----------------
Output
-----------------
1 imported box of chocolates: 10.50
1 imported bottle of perfume: 54.65
Sales Taxes: 7.65
Total: 65.15

-----------------
Input
-----------------
1 imported bottle of perfume at 27.99 : other
1 bottle of perfume at 18.99 : other
1 packet of headache pills at 9.75 : med
1 box of imported chocolates at 11.25 : food

-----------------
Output
-----------------
1 imported bottle of perfume: 32.19
1 bottle of perfume: 20.89
1 packet of headache pills: 9.75
1 box of imported chocolates: 11.80
Sales Taxes: 6.65
Total: 74.63
```

# Output of the test_salesTax.py
```
----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```
