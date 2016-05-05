__author__ = 'khushboomandlecha'

global type_parser
type_parser = {}
global index

global dynindex
dynindex = 0
global heap
heap = []
monitor = {}
# This is the main function where all computations happen

import heapq
from slimit.parser import Parser
from slimit.visitors import nodevisitor
from slimit import ast
from slimit.lexer import Lexer
from parsePrimType import parsePrimType
from parseObjType import parseObjType
from parseTypeName import parseTypeName


# parsing the entire function

def ParsingOfFunction():
    index = 0
    parser = Parser()
    tree = parser.parse('l = 0;l = h;')

    # for node in nodevisitor.visit(tree):
    #   if isinstance(node, ast.Identifier) and node.value == 'i':
    #      node.value = 'hello'

    x = tree.to_ecma()  # print awesome javascript :)
    # print x;

    # print "Opening the file..."
    # target = open("file.txt",'w')
    # target.write(x)
    # target.close()
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

            print "Going into the lexer function --------------"
            lex = LexingofFunction(temp)
            temp = ""
            i += 1

        else:

            temp = temp + str

    # print map;

    print "----------------------------- print heap now"

    for x in heap:
        print x.name
        print x.level
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

    addinHeap(lhs, rhs)
    # CompareLHSandRHS(lhs,rhs)


    return token


def heapSort(iterable):
    for value in iterable:
        heapq.heappush(heap, value)
        return [heapq.heappop(heap) for i in range(len(heap))]


def addinHeapRightFirst(lhs, rhs):
    return


def addinHeap(lhs, rhs):
    z = ""
    y = ""
    index = 0;
    if "obj." in rhs:
        # check for p field names

        print "dyanamic checking for rhs 1"

        if "p" in rhs:

            if "p1" in rhs:
                z = parsePrimType("PRIM", 3)
                y = parseTypeName("p1", z.level, z)

            elif "p2" in rhs:
                z = parsePrimType("PRIM", 2)
                y = parseTypeName("p2", z.level, z)

            elif "p3" in rhs:
                z = parsePrimType("PRIM", 1)
                y = parseTypeName("p3", z.level, z)

            x = parseObjType("obj", 0, z, y);


        elif "l" in rhs:

            z = parsePrimType("l", 0)
            x = parseObjType("obj", 0, z, y);

        elif "h" in rhs:

            z = parsePrimType("h", 5)
            x = parseObjType("obj", 0, z, y);

        heapq.heappush(heap, x)
    if "p" in rhs:

        print "static checking for rhs 3"

        if "p1" in lhs:
            z = parsePrimType("PRIM", 3)
            y = parseTypeName("p1", z.level, z)

        elif "p2" in lhs:
            z = parsePrimType("PRIM", 2)
            y = parseTypeName("p2", z.level, z)

        elif "p3" in lhs:

            z = parsePrimType("PRIM", 1)
            y = parseTypeName("p3", z.level, z)

        heapq.heappush(heap, y)

    elif "l" in rhs:

        print "static checking for rhs 4"
        z = parsePrimType("l", 0)
        heapq.heappush(heap, z)

    elif "h" in rhs:

        print "static checking for rhs 5"
        z = parsePrimType("h", 5)
        heapq.heappush(heap, z)
        if "l" in lhs:
             print " Illegal typing"

    elif "NUMBER" in rhs:

        print "static checking for rhs 6 ,No need to check lhs"
        z = parsePrimType("PRIM", 0)
        heap.insert(index, z)
        index += 1



    # -----------------------------------------
    # check for lhs later
    z = ""
    y = ""

    if "obj." in lhs:
        # check for p field names

        print "dynamic checking for rhs 1"

        if "p" in lhs:

            if "p1" in lhs:
                z = parsePrimType("PRIM", 3)
                y = parseTypeName("p1", z.level, z)

            elif "p2" in lhs:
                z = parsePrimType("PRIM", 2)
                y = parseTypeName("p2", z.level, z)

            elif "p3" in lhs:
                z = parsePrimType("PRIM", 1)
                y = parseTypeName("p3", z.level, z)

            x = parseObjType("obj", 0, z, y);

        elif "l" in lhs:

            z = parsePrimType("l", 0)
            x = parseObjType("obj", 0, z, y);

        elif "h" in lhs:

            z = parsePrimType("h", 5)
            x = parseObjType("obj", 0, z, y);

        heapq.heappush(heap, x)
    elif "obj" in lhs:

        if "{}" in rhs:

            print "dynamic checking for rhs 2"
            x = parseObjType("obj", 0, z, y);

        elif "{" in rhs and "}":

            print "dynamic checking for rhs 2.1"

        if "p" in rhs:

            print "dynamic checking for rhs 3"

            if "p1" in lhs:
                z = parsePrimType("PRIM", 3)
                y = parseTypeName("p1", z.level, z)

            elif "p2" in lhs:
                z = parsePrimType("PRIM", 2)
                y = parseTypeName("p2", z.level, z)

            elif "p3" in lhs:

                z = parsePrimType("PRIM", 1)
                y = parseTypeName("p3", z.level, z)

        elif "l" in lhs:

            print "dynamic checking for rhs 4"
            z = parsePrimType("l", 0)


        elif "h" in lhs:

            print "dynamic checking for rhs 5"
            z = parsePrimType("h", 5)

        x = parseObjType("obj", 0, z, y);
        heapq.heappush(heap, x)

    elif "p" in lhs:

        print "dynamic checking for rhs 6"
        y = parseTypeName("p", 2, )
        heapq.heappush(heap, y)

    elif "l" in lhs:

        print "dyanamic checking for rhs 7"
        z = parsePrimType("l", 0)
        # type_parser.__setitem__(index,x)
        # index+=1
        heapq.heappush(heap, z)
    elif "h" in lhs:

        print "dynamic checking for rhs 8"
        z = parsePrimType("h", 5)
        heapq.heappush(heap, z)

    return


def trim(str):
    str.lstrip("LexToken")

    str.lstrip(")")
    str.lstrip()
    return str;


def CompareLHSandRHS(lhs, rhs):

    print "In compare lhs and rhs"
def assignLevels(lhs, rhs):
    if "ID" in lhs and "NUMBER" in rhs:
        addinHeap(lhs, rhs);

        type_parser.__setitem__();
    if "ID" in rhs:
        checkForRhsDyanamic(rhs)

    return


def checkForRhsDyanamic(parseLeft, rhs):
    if "l" in rhs:
        print "yes"


ParsingOfFunction()
# heapSort(heap.__iter__())
