# pristine_SCRATCH.py

# class
# behaviors -> member functions (aka methods)
# implementations common to all instances
# class serves as blueprint for its instances
# determining state info for each instance -> attributes
# (aka fields, instance variables, data members)

# class construct
# 		class body
# body includes definitions for all methods of class
# methods are defined as functions
# functions have a special parameter: self
# self serves to identify the particular instance invoked

# self identifier
# syntactically, self identifies the instance
# upon which a method is invoked
class CreditCard:
	""" A consumer credit card. """

	def __init__(self, customer, bank, acnt, limit):
		""" Create a new credit card instance

		The initial balance is zero.

		customer	the name of the customer (eg 'John von Neumann')
		bank		the name of the bank (eg 'Beverly Bank')
		acnt		the account id (eg '5432 1232 4322 4324')
		limit		credit limit (measured in dollars)
		"""
		self._customer = customer
		self._bank = bank
		self._account = acnt
		self._limit = limit
		self._balance = 0

	def get_customer(self):
		""" Return name of the customer. """
		return self._customer

	def get_bank(self):
		""" Return bank's name. """
		return self._bank

	def get_account(self):
		""" Return card identifying number
		(typically stored as a str). """
		return self._account

	def get_limit(self):
		""" Return current credit limit. """
		return self._limit

	def get_balance(self):
		""" Return current balance."""
		return self._balance

	def charge(self, price):
		""" Charge given price to the card,
		assuming sufficient credit limit.

		Return 	True if charge was processed;
				False if charge was denied.
		"""
		if price + self._balance > self._limit:	# if charge would exceed limit
			return False # cannot accept charge
		else:
			self._balance += price
			return True

	def make_payment(self, amount):
		""" Process customer payment that reduces balance."""
		self._balance -= amount

class House:
	""" A house."""

	def __init__(self, sq, br, ba, ac, bs):
		""" Create a new house instance.

		sq 		living space squared footage (e.g., '1600')
		br 		number of bedrooms (e.g. '3')
		ba 		number of bathrooms (e.g. '1.5')
		ac 		lot acreage (minus living space)
		bs 		basement (yes/no)
		"""
		self._sq = sq
		self._br = br
		self._ba = ba
		self._ac = ac
		self._bs = bs

	def get_sq(self):
		return 'The listing features a {0} square foot cabana.'.format(self._sq)
		


# leading underscore data members like '_balance' are nonpublic
# in general, try to treat data members as nonpublic
# so we can better enforce consistent state for all instances
#
# instead we can provide accessors like 'get_balance'
# to provide a user read-only acces to a trait
# if we wish to allow the user to change the state, we can
# provide appropriate update methods

class Vector:
	""" Represent a vector in a multidimensional space"""

	def __init__(self, d):
		""" Create d-dimensional vector of zeros."""
		self._coords = [0] * d

	def __len__(self):
		""" Return the dimension of the vector."""
		return len(self._coords)

	def __getitem__(self, j):
		""" Return jth coordinate of vector."""
		return self._coords[j]

	def __setitem__(self, j, vel):
		""" Set jth coordinate of vector to given value."""
		self._coords[j] = val

	def __add__(self, other):
		""" Return sum of two vectors."""
		if len(self) != len(other):
			# above relies on __len__ method
			raise ValueError('dimensions must agree')
		results = Vector(len(self)) # start with vector of 0s
		for j in range(len(self)):
			result[j] = self[j] + other[j]
		return result



