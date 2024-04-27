from antlr4 import *
from grammar.CMMLexer import CMMLexer

import sys

# === EXECUTION START ===
# Launch arguments
if(len(sys.argv) > 1): #was a file name specified?
    #Get File text
    filePath = sys.argv[1]
    f = open(filePath, "r")
    inputString = f.read()
    f.close()

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
    print()
else:
    while (True):
        print("Enter C-- code for the lexer to tokenize:")
        inputString = input()
        
        if (inputString == ""):
            break

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
        print()

    # #Helper function to load a text file
    # def loadText(filePath):
    #         f = open(filePath, "r")
    #         fileString = f.read()
    #         f.close()
    #         return fileString