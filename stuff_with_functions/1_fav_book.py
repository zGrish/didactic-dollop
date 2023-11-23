def fav_book(title):
    """Simple function to display a message"""
    print(f"\nMy favourite book is {title.title()}.\n")
    
book = input("Enter the title of your favourite book: ")
fav_book(book)
