__author__ = 'khushboomandlecha'

# Trying out the lexer function

from slimit.lexer import Lexer
lexer = Lexer()
lexer.input('o = {};o.p1 = 3;y = prompt(\'Which property do you want?\');if (o[y]) {l = 0;}')
file = open('outputfile.txt','w')



for token in lexer:

    file.write(str(token))
    file.write('\n')
    print token

file.close()
