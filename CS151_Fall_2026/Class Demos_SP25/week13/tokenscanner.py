# A token scanner is an abstract data type that divides a string into
# individual tokens, which are strings of consecutive characters that
# form logical units.  This simplified version recognizes two token types:
#
#   1. A string of consecutive letters and digits
#   2. A single character string
#
# To use this class, you must first create a TokenScanner instance by
# calling its constructor:
#
#     scanner = TokenScanner()
#
# The next step is to call the set_input method to specify the string
# from which tokens are read, as follows:
#
#     scanner.set_input(s)
#
# Once you have initialized the scanner, you can retrieve the next token
# by calling
#
#    token = scanner.next_token()
#
# To determine whether any tokens remain to be read, you can either
# call the predicate method scanner.has_more_tokens() or check to see
# whether next_token returns the empty string.
#
# The following code fragment serves as a pattern for processing each
# token in the string stored in the variable source:
#
#     scanner = TokenScanner(source)
#     while scanner.has_more_tokens():
#         token = scanner.next_token()
#         . . . code to process the token . . .
#
# By default, the TokenScanner class treats whitespace characters
# as operators and returns them as single-character tokens.  You
# can set the token scanner to ignore whitespace characters by
# making the following call:
#
#     scanner.ignore_whitespace()
 
class TokenScanner:
 
    """This class implements a simple token scanner."""
 
# Constructor
 
    def __init__(self, source=""):
        """
        Creates a new TokenScanner object that scans the specified string.
        """
        self.set_input(source)
        self._ignore_whitespace_flag = False
 
# Public methods
 
    def set_input(self, source):
        """
        Resets the input so that it comes from source.
        """
        self._source = source
        self._nch = len(source)
        self._cp = 0
 
    def next_token(self):
        """
        Returns the next token from this scanner.  If called when no
        tokens are available, next_token returns the empty string.
        """
        if self._ignore_whitespace_flag:
            self._skip_whitespace()
        if self._cp == self._nch:
            return ""
        token = self._source[self._cp]
        self._cp += 1
        if token.isalnum():
            while self._cp < self._nch and self._source[self._cp].isalnum():
                token += self._source[self._cp]
                self._cp += 1
        return token
 
    def has_more_tokens(self):
        """
        Returns True if there are more tokens for this scanner to read.
        """
        if self._ignore_whitespace_flag:
            self._skip_whitespace()
        return self._cp < self._nch
 
    def ignore_whitespace(self):
        """
        Tells the scanner to ignore whitespace characters.
        """
        self._ignore_whitespace_flag = True
 
# Private methods
 
    def _skip_whitespace(self):
        """
        Skips over any whitespace characters before the next token.
        """
        while self._cp < self._nch and self._source[self._cp].isspace():
            self._cp += 1