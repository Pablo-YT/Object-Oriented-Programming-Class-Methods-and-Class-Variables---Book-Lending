import random
from datetime import datetime

#options = [15,20,234203, 2032, 230, 90, 39, 1]
#print(random.choice(options))
#print(random.choice(options))
#print(random.choice(options))

#now = datetime.now()
#print(now)

#print(now.timestamp())

#print(type(datetime))


class Book(object):
	"""docstring for Book"""
	on_shelf = []
	on_loan = []

	def __init__(self, book_title, author, ISBN):
		self.book_title = book_title
		self.author = author
		self.ISBN = ISBN

	def borrow(self):
		if self.lent_out():
			return False
		else:
			due_date = Book.current_due_date()
			Book.on_shelf.remove(self)
			Book.on_loan.append(self)
		return True
			

	def return_to_library(self):
		if not self.lent_out():
			return False
		else: 
			self.due_date = None
			Book.on_loan.remove(self)
			Book.on_loan.append(self)
			return True



	def lent_out(self):
		return self in Book.on_loan
				

	@classmethod
	def create(cls, book_title, author, ISBN):
		new_book = Book(book_title, author, ISBN)
		cls.on_shelf.append(new_book)
		return new_book


	@classmethod
	def current_due_date(cls):
		now = datetime.now()
		two_weeks = 60* 60 *24 *14
		future_timestamp = now.timestamp() + two_weeks
		return datetime.fromtimestamp(future_timestamp)
			


	@classmethod
	def overdue_books(cls):
		overdue_books = []
		now = datetime.now()
		for book in Book.on_loan:
			if book.current_due_date() < now:
				overdue_books.append(book)
		return overdue_books

	@classmethod
	def browse(cls):
		browse = random.choice(cls.on_shelf)
		return browse




sister_outsider = Book.create("Sister Outsider", "Audre Lorde", "9781515905431")
aint_i = Book.create("Ain't I a Woman?", "Bell Hooks", "9780896081307")
if_they_come = Book.create("If They Come in the Morning", "Angela Y. Davis", "0893880221")
rich_dad_poor_dad = Book.create("Rich Dad Poor Dad", "Robert Kiyosaki", "1237748483")
print(Book.browse().book_title) 
print(Book.browse().book_title) 
print(Book.browse().book_title)
print(len(Book.on_shelf)) # 3
print(len(Book.on_loan)) # 0
print(sister_outsider.lent_out()) # False
print(sister_outsider.borrow()) # True
print(len(Book.on_shelf)) # 2
print(len(Book.on_loan)) # 1
print(sister_outsider.lent_out()) # True
print(sister_outsider.borrow()) # False
print(sister_outsider.current_due_date()) 
print(len(Book.overdue_books())) # 0
print(sister_outsider.return_to_library()) # True
print(sister_outsider.lent_out()) # False
print(len(Book.on_shelf)) # 2
print(len(Book.on_loan)) # 0