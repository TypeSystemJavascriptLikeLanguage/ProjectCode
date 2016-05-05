__author__ = 'khushboomandlecha'

# This is the main function where all computations happen

from slimit.parser import Parser
from slimit.visitors import nodevisitor
from slimit import ast
from slimit.lexer import Lexer


def ParsingOfFunction():

    parser = Parser()
    tree = parser.parse('l = 0;h = l;')
    #for node in nodevisitor.visit(tree):
     #   if isinstance(node, ast.Identifier) and node.value == 'i':
      #      node.value = 'hello'

    x = tree.to_ecma()  # print awesome javascript :)
    # print x;

    #print "Opening the file..."
    target = open("file.txt", 'w')
    target.write(x)
    target.close()
    lines = [line.rstrip('\n') for line in open('file.txt')]

    map = {}
    temp = ""
    i = 0

    # print lines;

    for str in lines:

        if ';' in str:
            temp = temp + str
            temp = temp.lstrip(";")
            #print temp;
            map.__setitem__(i, temp)
            #print "Going into the lexer function --------------"
            lex = LexingofFunction(temp)
            temp = ""
            i += 1

        else:

            temp = temp + str

    #print map;

    return

def LexingofFunction(str):

    lexer = Lexer()
    lexer.input(str)

    lhs = ""
    rhs = ""
    flag = 0
    for token in lexer:

        #print token
        tokenTemp = token.__str__()

        if '='not in tokenTemp and flag == 0:

            tokenTemp = trim(tokenTemp)
            lhs = lhs + tokenTemp

        elif '=' in tokenTemp or ';' in tokenTemp :
            flag = 1;
            continue

        else :
            rhs = rhs + tokenTemp

    print "Printing lhs",lhs
    print "Printing rhs",rhs
    print "-----------------------------"
    return token

def trim(str):

    str.lstrip("LexToken")

    str.lstrip(")")
    str.lstrip()
    return str;

ParsingOfFunction()