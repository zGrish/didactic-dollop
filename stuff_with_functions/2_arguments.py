def make_shirt(size, quote = 'percy jackson'):
    """Display t-shirt size and 
    custom quote to be printed."""
    print(f"Size: {size.upper()}"
          f"\nQuote: {quote.title()}\n")      # multi-line print statement
    
# positional arguments
make_shirt('xs', 'star wars')

# keyword arguments
make_shirt(quote = 'harry potter', size = 'xxl')

# positional and keyword arguments (activating default value)
make_shirt('m')
