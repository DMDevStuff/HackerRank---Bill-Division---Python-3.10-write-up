##    https://www.hackerrank.com/challenges/bon-appetit/problem
##
##    Two friends Anna and Brian, are deciding how to split the bill at a
##    dinner. Each will only pay for the items they consume. Brian gets the
##    check and calculates Anna's portion. You must determine if his
##    calculation is correct.

##    The webpage associated with the problem has an example containing
##    the formula for finding the correct amount due.

##### ##### ##### #####

#   Calculate and check
#   O(n)
#   n is the length of the bill - caused by the list summing
#   a note:
#       they guarantee the amounts will always be integers
#       so I use integer division in the correct amount calculation
#       as it is a constant time operation

def bonAppetit(bill, k, b):

    correct_amount = (sum(bill) - bill[k]) // 2

    print('Bon Appetit' if b - correct_amount == 0 else b - correct_amount)
