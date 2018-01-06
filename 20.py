"""
Exercise 20: Multistate Sales Tax Calculator

Create a tax calculator that handles multiple states and multiple counties within each state.
The program props the user for the order amound and the state where the order will be shipped.

For Wisconsin residents, prompt for the county of residence.
  - For Eau Claire county residents, add an additional 0.005 tax.
  - For Dunn county residents, add an additional 0.004 tax.

Illinois residents must be charged 8'%' sales tax with no additional count-level charge.
All other states are not charged tax.  The program then displays the tax and the total
for wisconsin and Illinois residents but just the total for everyone else.

Constraints:
 - Ensure that all money is rounded up to the nearest cent.
 - Use a single ouput statement at the end of the program to display the program results.

"""
from ex_20_func import *

def state_sales_tax_calculator():
    greeting()
    order = order_amount_input()
    state = state_input()
    total = total_calculations(order_amount= order, state=state)

state_sales_tax_calculator()
