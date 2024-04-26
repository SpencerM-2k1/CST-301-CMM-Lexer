from antlr4 import *
from grammar.CMMLexer import CMMLexer

#Test strings: uncomment code here

# inputString = "int x = 5;"
# inputString = "if (x < 4) write 5;"
inputString = "if (x >= [4 - -5]) if (y && z) break;"

# Set up Lexer
inputStream = InputStream(inputString)
lexer = CMMLexer(inputStream)

# Get the symbolic names list
#   (Allows for a more readable output)
symbolicNames = lexer.symbolicNames

# Iterate through all tokens
token = lexer.nextToken()
while token.type != Token.EOF:
    tokenName = symbolicNames[token.type]
    print("Token Type: {}, \tToken Value: {}".format(tokenName, token.text))
    token = lexer.nextToken()
