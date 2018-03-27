#!python3
#
#
# pristine text
#
#
import re
import unicodedata

from .stop_words import ENGLISH_STOP_WORDS

# select random document for testing


# handle encodings/decodings
def encoding_decoding(text):
	pass



# handle the character set somehow
def character_set(text):
	pass


	# (stretch) language_detection()
	def detect_lanuage(text):
		pass

	# if you know the language has direct transliteration to ascii
	def strip_accents_ascii(s):
	    """Transform accentuated unicode symbols into ascii or nothing
	    Warning: this solution is only suited for languages that have a direct
	    transliteration to ASCII symbols.
	    See also
	    --------
	    strip_accents_unicode
	        Remove accentuated char for any unicode symbol.
	    """
	    nkfd_form = unicodedata.normalize('NFKD', s)
		return nkfd_form.encode('ASCII', 'ignore').decode('ASCII')
		
	# otherwise use strip_accents_unicode
	def strip_accents_unicode(s):
    """Transform accentuated unicode symbols into their simple counterpart
    Warning: the python-level loop and join operations make this
    implementation 20 times slower than the strip_accents_ascii basic
    normalization.
    See also
    --------
    strip_accents_ascii
        Remove accentuated char for any unicode symbol that has a direct
        ASCII equivalent.
    """
    	normalized = unicodedata.normalize('NFKD', s)
    	if normalized == s:
        	return s
    	else:
			return ''.join([c for c in normalized if not unicodedata.combining(c)])


# handle html
def html_parsing(text):
	pass

# handle xml
def xml_parsing(text):
	pass

def strip_tags(s):
    """Basic regexp based HTML / XML tag stripper function
    For serious HTML/XML preprocessing you should rather use an external
    library such as lxml or BeautifulSoup.
    """
	return re.compile(r"<([^>]+)>", flags=re.UNICODE).sub(" ", s)

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
		detect_lanuage()

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