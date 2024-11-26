# Accept a list of borrowed books
borrowed_books_input = input("Enter the borrowed books in the format 'Book Title - Days Borrowed', separated by commas: ")

# Process the input to create a dictionary with book titles and their total borrowed days
borrowed_books_list = borrowed_books_input.split(',')
book_borrow_days = {}

for record in borrowed_books_list:
    title, days = record.strip().split(' - ')
    days = int(days)
    if title in book_borrow_days:
        book_borrow_days[title] += days
    else:
        book_borrow_days[title] = days

# Calculate the most and least borrowed books
most_borrowed_book = max(book_borrow_days, key=book_borrow_days.get)
least_borrowed_book = min(book_borrow_days, key=book_borrow_days.get)

# Calculate the average number of days books were borrowed
average_days = sum(book_borrow_days.values()) / len(book_borrow_days)

# Find unique titles of all borrowed books
unique_titles = set(book_borrow_days.keys())

# Sort the books by the number of days borrowed in descending order
sorted_books = sorted(book_borrow_days.items(), key=lambda item: item[1], reverse=True)

# Output the results
print(f"Most borrowed book: {most_borrowed_book} - {book_borrow_days[most_borrowed_book]} days")
print(f"Least borrowed book: {least_borrowed_book} - {book_borrow_days[least_borrowed_book]} days")
print(f"Average number of days books were borrowed: {average_days:.2f}")
print(f"Unique titles of all borrowed books: {unique_titles}")
print("Books sorted by the number of days borrowed (in descending order):")
for title, days in sorted_books:
    print(f"{title}: {days} days")