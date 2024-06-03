def book():
    while True:
        book_title =input('input book name : ')
        if not book_title or not isinstance(book_title, str):
            print('Please just alphabet!')
            continue
        # return book_title
        # else:
            # print(book_title,'judul buku : ')
        book_year = input('input book year relase : ')
        if not book_year or not isinstance(book_year, int):
            print('Please just number!')
            continue
        # return book_year
        book_price = input('input price the book : ')
        if not book_price or not isinstance(book_price, int):
            print('Please just number!')
            continue
        # return book_price
book()

