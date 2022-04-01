




def to_usd(my_price):
    """
    This is a docstring. It tells us what this function is about.
    What its responsibilities are. 
    What the params are about. 
    What datatypes the params are. 
    What this fucntion will return.
    Example of invoking the function.

    Invoke like this: to_usd(9.99999)
    
    Example return value "$9.99"
    """
    return '${:,.2f}'.format(my_price)


# nesting code in the main condition will
# allow other scripts to cleanly import functions from this file
# without running this code

# this code still gets run when we invoke the script from the command line
# 
if __name__ == "__main__":
# if this code is in the global scope
# ... of a file we're trying to import from 
# .... it will throw errors when we try to run those other

    price = input("Please choose a price like 4.99999 ")

    print(to_usd(float(price)))
