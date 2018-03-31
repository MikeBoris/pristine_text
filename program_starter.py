# 3-30-18
#
# program_starter.py
#
# >>> python program_starter.py {2}
# [**creates starter file named {2}.py 
# w/ default class instantiated]
from datetime import date
from sys import argv

#
file_text = '''
# {0}
# 
# {1}
# 


class {2}:
	""" A {2}."""

	def __init__(self, sq, br, ba, ac, bs):
		""" Create a new {2} instance.

		>>> from {2} import {2}
		>>> casa = {2}(1300, 3, 2, 2.0, 'Yes')
		>>> casa
		<{2}{2} object at 0x7f2fb18030b8>
		>>> casa.get_sq()
		'The listing features 1300 square foot cabana.'


		sq 		squared footage living space (e.g., '1600')
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
		listing = """
		The listing features a {0} square foot cabana.
		"""
		return listing.format(self._sq)



if __name__ == '__main__':
	

	casa = {2}(1300, 3, 2, 2.0, 'Yes')
	print(casa)
'''

#
#
#
DATE = date.today().isoformat()
FILE_NAME = argv[1] + '.py'
THING_NAME = argv[1]


f = open(FILE_NAME, 'w')
f.write(file_text.format(DATE,
	FILE_NAME,
	THING_NAME))
f.close()

print('All set')
