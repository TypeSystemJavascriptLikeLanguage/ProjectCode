__author__ = 'khushboomandlecha'

global type_parser
type_parser = {}
global index
index = 0
global dynindex
dynindex = 0
global heap
heap = []
monitor = {}
# This is the main function where all computations happen

from slimit.parser import Parser
from slimit.visitors import nodevisitor
from slimit import ast
from slimit.lexer import Lexer
from parsePrimType import parsePrimType
from parseObjType import parseObjType
from parseTypeName import parseTypeName


# parsing the entire function

def ParsingOfFunction():
    parser = Parser()
    tree = parser.parse('l = 0;h = l;')

    # for node in nodevisitor.visit(tree):
    #   if isinstance(node, ast.Identifier) and node.value == 'i':
    #      node.value = 'hello'

    x = tree.to_ecma()  # print awesome javascript :)
    # print x;

    # print "Opening the file..."
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
            # print temp;
            map.__setitem__(i, temp)

            # print "Going into the lexer function --------------"
            lex = LexingofFunction(temp)
            temp = ""
            i += 1

        else:

            temp = temp + str

    # print map;

    return

# pass every line one by one to put in the heap

def LexingofFunction(str):
    lexer = Lexer()
    lexer.input(str)

    lhs = ""
    rhs = ""
    flag = 0
    for token in lexer:

        # print token
        tokenTemp = token.__str__()

        if '=' not in tokenTemp and flag == 0:

            tokenTemp = trim(tokenTemp)
            lhs = lhs + tokenTemp

        elif '=' in tokenTemp or ';' in tokenTemp:
            flag = 1;
            continue

        else:
            rhs = rhs + tokenTemp

    print "Printing lhs", lhs
    print "Printing rhs", rhs

    addinHeap(lhs,rhs)
    #CompareLHSandRHS(lhs,rhs)

    print "-----------------------------"

    return token

def addinHeapRightFirst(lhs,rhs):



    return
def addinHeap(lhs,rhs):







    z = ""
    y = ""



    # check for lhs later


    if "obj." in lhs:
        # check for p field names

        print "dyanamic checking for rhs 1"

        if "p" in lhs:

            if "p1" in lhs:
                z = parsePrimType("PRIM",3)
                y = parseTypeName("p1",z.level,z)

            elif "p2" in lhs:
                z = parsePrimType("PRIM",2)
                y = parseTypeName("p2",z.level,z)

            elif "p3" in lhs:
                z = parsePrimType("PRIM",1)
                y = parseTypeName("p3",z.level,z)

            x = parseObjType("obj",0,z,y);

        elif "l" in lhs:

            z = parsePrimType("l",0)
            x = parseObjType("obj",0,z,y);

        elif "h" in lhs :

            z = parsePrimType("h",5)
            x = parseObjType("obj",0,z,y);

    elif "obj" in lhs:

        if "{}" in rhs:

            print "dyanamic checking for rhs 2"
            x = parseObjType("obj",0,z,y);

        elif "{" in rhs and "}" :

            print "dyanamic checking for rhs 2.1"


        if "p" in rhs:

            print "dyanamic checking for rhs 3"

            if "p1" in lhs:
                z = parsePrimType("PRIM",3)
                y = parseTypeName("p1",z.level,z)

            elif "p2" in lhs:
                z = parsePrimType("PRIM",2)
                y = parseTypeName("p2",z.level,z)

            elif "p3" in lhs:

                z = parsePrimType("PRIM",1)
                y = parseTypeName("p3",z.level,z)

        elif "l" in lhs:

                print "dyanamic checking for rhs 4"
                z = parsePrimType("l",0)


        elif "h" in lhs:

                print "dyanamic checking for rhs 5"
                z = parsePrimType("h",5)

        x = parseObjType("obj",0,z,y);

    elif "p" in lhs:

        print "dyanamic checking for rhs 6"

    elif "l" in lhs:

        print "dyanamic checking for rhs 7"
        x = parsePrimType("l",0)
        type_parser.__setitem__(index,x)
        index+=1

    elif "h" in lhs:

        print "dyanamic checking for rhs 8"
        x = parsePrimType("h",5)

    elif "l" in lhs:

        print "dyanamic checking for rhs 9"
        x = parsePrimType("l",0)
        #type_parser.__setitem__(index,x)
        #index+=1

    elif "h" in lhs:

        x = parsePrimType("h",5)

    return

def trim(str):
    str.lstrip("LexToken")

    str.lstrip(")")
    str.lstrip()
    return str;


def CompareLHSandRHS(lhs, rhs):

    if "ID" in lhs:

        x = parsePrimType("l",0)

        if "NUMBER" in rhs:

            print "ok assignment"

        elif "ID" in rhs:

            y = parsePrimType("h",5)
            print "ok comparision of levels"
            if y.level < x.level :

                print "Illegal Typing"
        else:
            print " continue "

    return

def assignLevels(lhs,rhs):


    if "ID" in lhs and "NUMBER" in rhs:

        addinHeap(lhs,rhs);

        type_parser.__setitem__();
    if "ID" in rhs :
            checkForRhsDyanamic(rhs)

    return



def checkForRhsDyanamic(parseLeft,rhs):

    if "l" in rhs:
        print "yes"




ParsingOfFunction()
