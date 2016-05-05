from Stack import Stack


def TestInput(inputStr):
    s = Stack();

    for i in inputStr:

        if i == '(' or i == '[' or i == '{':

            s.push(i)

        elif i == ')' or i == ']' or i == '}':

            temp = s.pop()

            if temp == '(':

                if i == ']' or i == '}':
                    return False

            elif temp == '[':

                if i == '(' or i == '}':
                    return False

            if temp == '{':

                if i == ']' or i == ')':
                    return False

    return True


out=TestInput("{ [ }")

print out
