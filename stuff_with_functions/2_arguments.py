def make_shirt(size = 'l', quote = 'percy jackson'):
    """Display t-shirt size and 
    custom quote to be printed."""
    print(f"Size: {size.upper()}"
          f"\nQuote: {quote.title()}\n")      # multi-line print statement
    
# positional arguments (ignores default values, assigned left-to-right)
make_shirt('xs', 'star wars')

# keyword arguments (ignores default, assigned as mentioned)
make_shirt(quote = 'harry potter', size = 'xxl')

# positional and keyword arguments (activating default value)
make_shirt('m')
make_shirt(quote = 'i love python')
make_shirt(size = 'xl')
