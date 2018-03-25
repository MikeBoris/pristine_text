#!python3
#
#
# pristine text
#
#

# handle encodings/decodings
def encoding_decoding(text):
	pass



# handle the character set somehow
def character_set(text):
	pass


	# (stretch) language_detection()
	def detect_lanuage(text):
		pass


# handle html
def html_parsing(text):
	pass

# handle xml
def xml_parsing(text):
	pass


# handle urls
def remove_but_store_urls(text):
	pass


# handle special chars
def remove_special_chars(text):
	pass


# handle word/sentence tokenizing
def word_tokenize(text):
	pass


def sentence_tokenize(text):
	pass


# handle stemming
def stem(text):
	pass

#--- PRIMARY FUNCTION ------------------


def make_pristine(text):
	
	# handle encodings/decodings
	encoding_decoding()

	# handle the character set somehow
	character_set()

		# (stretch) language_detection()

	# handle html
	html_parsing()

	# handle xml
	xml_parsing()

	# handle urls
	remove_but_store_urls()

	# handle special chars
	remove_special_chars()

	# handle word/sentence tokenizing
	word_tokenize()
	sentence_tokenize()

	# handle stemming
	stem()


# further text processing

if __name__ == '__main__':
	make_pristine()