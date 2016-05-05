type_parser = {}


# sec_types.STR = 1

def parseType(index):
    index = type_parser.skip(index)
    # prefix = fullstr[index:index+2]

    parser_table = {'FU': 'parseFunType', 'OB': 'parseObjType', 'PR': 'parsePrimType', 'GL': 'parseGlobalType',
                    '**': 'parseTypeName', '__': 'parseTypeVariable'
                    }
    # parser_fun = parser_table[prefix]

    # if (!parser_fun) throw new Error ('Irrecognizable Type')

    # ret = this[parser_fun](index)
    # return ret

# __k
