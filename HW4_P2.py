#Konstantin Shvedov
#Code is intended for Windows 10
import re
############################################################################
#################################_P1 of HW_#################################
############################################################################
#--------------------------------------------------------------------------#
#Operand Stack
#----------------------------------PART 1----------------------------------#
#The operand stack, implemented as a list
opstack = []

#opPop removes element/operand from stack
def opPop():
    if(len(opstack) > 0):
        return opstack.pop(0)
    else:
        print("Error: Operand Stack Empty")

#opPush pushes ad operand onto stack
def opPush(value):
    opstack.insert(0, value)

#--------------------------------------------------------------------------#
############################################################################
#Dictionary Stack
#----------------------------------PART 2----------------------------------#
# The dictionary stack, implemented as a list
dictstack = []

#dictPop pops removes an element from the stack
def dictPop():
    if dictstack:
        return dictstack.pop(0)
    else:
        print("Error: Dictionary Stack Empty")

#dictPush adds an element to the stack
def dictPush(d):
    dictstack.insert(0, d)

#define creates a new dictionary entry
def define(name, value):
    if dictstack:
        dictstack[0][name[1:]] = value
    else:
        dictstack.insert(0, {name[1:]: value})

#lookup, itterates through the stack to find "name"
def lookup(name):
    for item in dictstack:
        if name in item.keys():
            return item[name]
    print("Error: No such variable exists")

#--------------------------------------------------------------------------#
############################################################################
#Arithmetic Operators
#----------------------------------PART 3----------------------------------#
#Addition operator
def add():
    if(len(opstack) > 1):
        valOne = opPop()
        valTwo = opPop()
        if ((isinstance(valOne,int) or isinstance(valOne,float))
            and (isinstance(valTwo,int) or isinstance(valTwo,float))):
                res = valOne + valTwo
                opPush(res)
        else:
            print("Error: Invalid type")
            opPush(valTwo)
            opPush(valOne)
    else:
        print("Error: Not enough operands in stack")

#Subtraction operator
def sub():
    if(len(opstack) > 1):
        valOne = opPop()
        valTwo = opPop()
        if ((isinstance(valOne,int) or isinstance(valOne,float))
            and (isinstance(valTwo,int) or isinstance(valTwo,float))):
                res = valTwo - valOne
                opPush(res)
        else:
            print("Error: Invalid type")
            opPush(valTwo)
            opPush(valOne)
    else:
        print("Error: Not enough operands in stack")

#Multiplication operator
def mul():
    if(len(opstack) > 1):
        valOne = opPop()
        valTwo = opPop()
        if ((isinstance(valOne,int) or isinstance(valOne,float))
            and (isinstance(valTwo,int) or isinstance(valTwo,float))):
                res = valOne * valTwo
                opPush(res)
        else:
            print("Error: Invalid type")
            opPush(valTwo)
            opPush(valOne)
    else:
        print("Error: Not enough operands in stack")

#Division operator
def div():
    if(len(opstack) > 1):
        valOne = opPop()
        valTwo = opPop()
        if ((isinstance(valOne,int) or isinstance(valOne,float))
            and (isinstance(valTwo,int) or isinstance(valTwo,float))):
                res = valTwo / valOne
                opPush(res)
        else:
            print("Error: Invalid type")
            opPush(valTwo)
            opPush(valOne)
    else:
        print("Error: Not enough operands in stack")

#Equality operator
def eq():
    if(len(opstack) > 1):
        valOne = opPop()
        valTwo = opPop()
        if ((isinstance(valOne,int) or isinstance(valOne,float))
            and (isinstance(valTwo,int) or isinstance(valTwo,float))):
                if (valTwo == valOne):
                    opPush(True)
                else:
                    opPush(False)
        else:
            print("Error: Invalid type")
            opPush(valTwo)
            opPush(valOne)
    else:
        print("Error: Not enough operands in stack")

#Less than operator
def lt():
    if(len(opstack) > 1):
        valOne = opPop()
        valTwo = opPop()
        if ((isinstance(valOne,int) or isinstance(valOne,float))
            and (isinstance(valTwo,int) or isinstance(valTwo,float))):
                if (valOne > valTwo):
                    opPush(True)
                else:
                    opPush(False)
        else:
            print("Error: Invalid type")
            opPush(valTwo)
            opPush(valOne)
    else:
        print("Error: Not enough operands in stack")

#Greator than operator
def gt():
    if(len(opstack) > 1):
        valOne = opPop()
        valTwo = opPop()
        if ((isinstance(valOne,int) or isinstance(valOne,float))
            and (isinstance(valTwo,int) or isinstance(valTwo,float))):
                if (valOne < valTwo):
                    opPush(True)
                else:
                    opPush(False)
        else:
            print("Error: Invalid type")
            opPush(valTwo)
            opPush(valOne)
    else:
        print("Error: Not enough operands in stack")

#--------------------------------------------------------------------------#
############################################################################
#Array operators
#----------------------------------PART 4----------------------------------#
#Finds the length of array if top of stack is an array
def length():
    if(len(opstack) > 0):
        arr = opPop()
        if (isinstance(arr, list)):
            opPush(len(arr))
        else:
            print("Error: Top element is not an array")
            opPush(arr)
    else:
        print("Error: Stack empty")

#Gets the value at the index position that is at top of stack
def get():
    if(len(opstack) > 1):
        index = opPop()
        arr = opPop()
        if(isinstance(arr, list)):
            if (index < len(arr) and index >= 0):
                opPush(arr[index])
            else:
                print("Error: Index out of Bounds")
                opPush(arr)
                opPush(index)
        else:
            print("Error: Not a List")
            opPush(arr)
            opPush(index)
    else:
        print("Error: not enough operands in stack")

#--------------------------------------------------------------------------#
############################################################################
#Boolean operators
#----------------------------------PART 5----------------------------------#
#Boolean post script operator and
def psAnd():
    if(len(opstack) > 1):
        boolOne = opPop()
        boolTwo = opPop()
        if(isinstance(boolOne, bool) and isinstance(boolTwo, bool)):
            if((boolOne is True) and (boolTwo is True)):
                opPush(True)
            else:
                opPush(False)
        else:
            print("Error: Invalid type")
            opPush(boolTwo)
            opPush(boolOne)
    else:
        print("Error: not enough operands in stack")

#Boolean post script operator or
def psOr():
    if(len(opstack) > 1):
        boolOne = opPop()
        boolTwo = opPop()
        if(isinstance(boolOne, bool) and isinstance(boolTwo, bool)):
            if((boolOne is False) and (boolTwo is False)):
                opPush(False)
            else:
                opPush(True)
        else:
            print("Error: Invalid type")
            opPush(boolTwo)
            opPush(boolOne)
    else:
        print("Error: not enough operands in stack")

#Boolean post script operator not
def psNot():
    if(len(opstack) > 0):
        boolVal = opPop()
        if(isinstance(boolVal, bool)):
            if(boolVal is True):
                opPush(False)
            else:
                opPush(True)
        else:
            print("Error: Invalid type")
            opPush(boolVal)
    else:
        print("Error: stack is empty")

#--------------------------------------------------------------------------#
############################################################################
#Stack manipulation
#----------------------------------PART 6----------------------------------#
#duplicates top element of stack
def dup():
    if(len(opstack) > 0):
        tempVar = opPop()
        opPush(tempVar)
        opPush(tempVar)
    else:
        print("Error: stack is empty")

#Exchanges the two top elements of the operand stack
def exch():
    if(len(opstack) > 1):
        tempVarOne = opPop()
        tempVarTwo = opPop()
        opPush(tempVarOne)
        opPush(tempVarTwo)
    else:
        print("Error: not enough operands in stack")

#Pops top element off
def pop():
    if(len(opstack) > 0):
        opPop()
    else:
        print("Error: stack is empty")

#Copy copies a certain amount of elements and puts it on top of stack
def copy():
    if(len(opstack) > 1):
        numCopy = opPop()
        opLength = len(opstack)
        if(numCopy <= len(opstack)):
            for i in range((opLength - numCopy - 1), (opLength - 1)):
                opPush(opstack[i])
        else:
            print("Error: not enough elements to use copy")
            opPush(numCopy)
    else:
        print("Error: not enough operands")

#Clear pops all elements from list
def clear():
    if(len(opstack) > 0):
        while(len(opstack) > 0):
            opPop()
    else:
        print("Error: stack is empty")

#Prints every element
def stack():
    if(len(opstack) > 0):
        for elem in (opstack):
            print(elem)
    else:
        print("")

#--------------------------------------------------------------------------#
############################################################################
#Dictionary manipulation operators
#----------------------------------PART 6----------------------------------#
def psDict():
    if(len(dictstack) > 0):
        opPop()
        opPush({})
    else:
        print("Error: Dictionary is empty")

def begin():
    dictElem = opPop()
    if(isinstance(dictElem, dict)):
        dictstack.insert(0, dictElem)
    else:
        opPush(dictElem)

def end():
    if(len(dictstack) is not 0):
        return dictPop()
    else:
        print("Error: dictionary is empty")

def psDef():
    if(len(opstack) > 1):
        defVal = opPop()
        defName = opPop()
        if(isinstance(defName, str)):
            if (defName[0] == '/'):
                define(defName, defVal)
            else:
                print("Error: to define var, \"/\" required before var name")
        else:
            print("Error: Invalid type")
    else:
        print("Error: not enough operands in stack")

############################################################################
#################################_P2 of HW_#################################
############################################################################
#--------------------------------------------------------------------------#
############################################################################
#Tokenizer used to split "PostScript" Code
#Converting the token list to a code array
#----------------------------------PART 1----------------------------------#
def tokenize(s):
    return re.findall("/?[a-zA-Z][a-zA-Z0-9_]*|[[][\.-a-zA-Z0-9_\s!]+[]]|[-]?[0-9]+[.][0-9]+|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)

# The it argument is an iterator.
# The sequence of return characters should represent a list of properly nested
# tokens, where the tokens between '{' and '}' is included as a sublist. If the
# parenteses in the input iterator is not properly nested, returns False.
def groupMatching2(it):
    res = []
    for c in it:
        if c == '}':
            return res
        elif c=='{':
            res.append(groupMatching2(it))
        else:
            res.append(parseHelper(c))
    return False

# Function to parse a list of tokens and arrange the tokens between { and } braces
# as code-arrays.
# Properly nested parentheses are arranged into a list of properly nested lists.
def parse(L):
    res = []
    it = iter(L)
    for c in it:
        if c=='}':
            return False
        elif c=='{':
            res.append(groupMatching2(it))
        else:
            res.append(parseHelper(c))
    return res

#This function is in charge of helping the parser identify ints bools and int arrays
def parseHelper(S):
    if (S == "true"):
        return True
    elif (S == "false"):
        return False
    elif (S.lstrip('-').replace('.','',1).isdigit() == True):
        if '.' in S:
            return float(S)
        else:
            return int(S)
    elif (S[0] == '['):
        tempArr = []
        regex = r"(-?\d+\.?\d*)"
        matches = re.findall(regex, S)
        for match in matches:
            if '.' in match:
                tempArr.append(float(match))
            else:
                tempArr.append(int(match))
        return tempArr
    return S

#--------------------------------------------------------------------------#
############################################################################
#implementation of if/ifelse, for, forall operators and function calling
#----------------------------------PART 2----------------------------------#

def psIf():
    if(len(opstack) > 1):
        temp = opPop()
        interpretTop(opPop())
        tempTop = opPop()
        if (isinstance(tempTop, bool)):
            if (tempTop):
                interpretSPS(temp)
        else:
            print("Error: no bool to evaluate to execute if statement")
            opPush(tempTop)
            opPush(temp)
    else:
        print("Error: Not enough operands in stack")

def psIfElse():
    if(len(opstack) > 2):
        temp = opPop()
        tempBot = opPop()
        interpretTop(opPop())
        tempTop = opPop()
        if (isinstance(tempTop, bool)):
            if (tempTop):
                interpretSPS(tempBot)
            else:
                interpretSPS(temp)
        else:
            print("Error: no bool to evaluate to execute if statement")
            opPush(tempTop)
            opPush(tempBot)
            opPush(temp)
    else:
        print("Error: Not enough operands in stack")

def psFor():
    if(len(opstack) > 3):
        proc = opPop()
        limit = opPop()
        incr = opPop()
        init = opPop()
        itter = init
        if incr > 0:
            while (itter <= limit):
                opPush(itter)
                interpretSPS(proc)
                itter += incr
        elif incr < 0:
            while (itter >= limit):
                opPush(itter)
                interpretSPS(proc)
                itter += incr
        else:
            print("Error: Infinite loop may be caused")
            opPush(init)
            opPush(incr)
            opPush(limit)
            opPush(proc)
    else:
        print("Error: Not enough operands in stack")

def psForAll():
    if(len(opstack) > 1):
        proc = opPop()
        tempArr = opPop()
        if (isinstance(tempArr, list) and isinstance(proc, list)):
            for elem in tempArr:
                opPush(elem)
                interpretSPS(proc)
        else:
            print("Error: Incorrect opernad types")
            opPush(tempArr)
            opPush(proc)
    else:
        print("Error: Not enough operands in stack")

#--------------------------------------------------------------------------#
############################################################################
#implementation of if/ifelse, for, forall operators and function calling
#----------------------------------PART 3----------------------------------#
def interpreter(s): # s is a string
    interpretSPS(parse(tokenize(s)))

def interpretSPS(code): # code is a code array
    for elem in code:
        interpretTop(elem)

#this is the string interpreter that depending on the string calls a function
def interpretTop(topVar):
    if (isinstance(topVar, (list, bool, int, float))):
        opPush(topVar)
    elif (topVar[0] == '/'):
        opPush(topVar)
    elif topVar == "add":
        add()
    elif topVar == "sub":
        sub()
    elif topVar == "mul":
        mul()
    elif topVar == "div":
        div()
    elif topVar == "eq":
        eq()
    elif topVar == "lt":
        lt()
    elif topVar == "gt":
        gt()
    elif topVar == "length":
       length()
    elif topVar == "get":
        get()
    elif topVar == "and":
        psAnd()
    elif topVar == "or":
        psOr()
    elif topVar == "not":
        psNot()
    elif topVar == "dup":
        dup()
    elif topVar == "exch":
        exch()
    elif topVar == "pop":
        pop()
    elif topVar == "copy":
        copy()
    elif topVar == "clear":
        clear()
    elif topVar == "stack":
        stack()
    elif topVar == "dict":
        psDict()
    elif topVar == "begin":
        begin()
    elif topVar == "end":
        end()
    elif topVar == "def":
        psDef()
    elif topVar == "if":
        psIf()
    elif topVar == "ifelse":
        psIfElse()
    elif topVar == "for":
        psFor()
    elif topVar == "forall":
        psForAll()
    else:
        tempVar = lookup(topVar)
        if (isinstance(tempVar, list)):
            if (all(isinstance(x, int) for x in tempVar)):
                opPush(tempVar)
            else:
                interpretSPS(tempVar)
        else:
            opPush(tempVar)

#--------------------------------------------------------------------------#
############################################################################
############################################################################
#----------------------------------TESTING---------------------------------#
def testPsIf():
    opPush(True)
    opPush([True])
    psIf()
    if(opPop()):
        return True
    return False

def testPsIf2():
    opPush(True)
    opPush(False)
    opPush([True])
    psIf()
    if(opPop()):
        return True
    return False

def testPsIf3():
    opPush(6)
    opPush([True])
    psIf()
    if(opPop() == [True] and opPop() == 6):
        return True
    return False

def testPsIf4():
    opPush(6)
    psIf()
    if(opPop() == 6):
        return True
    return False

def testPsIfElse():
    opPush(True)
    opPush([True])
    opPush([6])
    psIfElse()
    if(opPop()):
        return True
    return False

def testPsIfElse2():
    opPush(False)
    opPush([True])
    opPush([6])
    psIfElse()
    if(opPop() == 6):
        return True
    return False

def testPsIfElse3():
    opPush(6)
    opPush([True])
    opPush([True])
    psIf()
    if(opPop() == [True] and opPop() == [True] and opPop() == 6):
        return True
    return False

def testPsIfElse4():
    opPush(6)
    psIf()
    if(opPop() == 6):
        return True
    return False

def testPsFor():
    opPush(0)
    opPush(1)
    opPush(1)
    opPush(4)
    opPush(["add"])
    interpreter("for")
    if(opPop() == 10):
        return True
    return False

def testPsFor2():
    opPush(0)
    opPush(4)
    opPush(-1)
    opPush(1)
    opPush(["add"])
    interpreter("for")
    if(opPop() == 10):
        return True
    return False

def testPsFor3():
    opPush(0)
    opPush(4)
    opPush(0)
    opPush(1)
    opPush(["add"])
    interpreter("for")
    if(opPop() == ["add"]):
        clear()
        return True
    return False

def testPsFor4():
    opPush(0)
    interpreter("for")
    if(opPop() == 0):
        return True
    return False

def testPsForAll():
    opPush(0)
    opPush([1, 2, 3, 4])
    opPush(["add"])
    interpreter("forall")
    if(opPop() == 10):
        return True
    return False

def testPsForAll2():
    opPush(0)
    opPush(["add"])
    interpreter("forall")
    if(opPop() == ["add"] and opPop() == 0):
        return True
    return False

def testPsForAll3():
    opPush(0)
    interpreter("forall")
    if(opPop() == 0):
        return True
    return False

input1 = """
  /square {dup mul} def  
  [1 2 3 4] {square} forall 
  add add add 30 eq true 
  stack
"""

input2 = """ 
  [1 2 3 4 5] dup length /n exch def
  /fact {
      0 dict begin
         /n exch def
         n 2 lt
         { 1}
         {n 1 sub fact n mul }
         ifelse
      end 
  } def
  n fact stack    
"""

input3 = """
  [9 9 8 4 10] {dup 5 lt {pop} if}  forall 
  stack 
"""

input4 = """
  [1 2 3 4 5] dup length exch {dup mul}  forall
  add add add add
  exch 0 exch -1 1 {dup mul add} for
  eq stack 
"""

input5 = """
    true false and false or not
        {false}
        if stack
"""

input6 = """
    0 [0.12 -34 476.23 3 -0.023] {add} forall 440.327 sub -5 add 96 add stack
"""

def testTokenize():
    tokenizeAnswer1 = ['/square', '{', 'dup', 'mul', '}', 'def', '[1 2 3 4]', '{', 'square', '}',
                        'forall', 'add', 'add', 'add', '30', 'eq', 'true', 'stack']

    if ((tokenize(input1) == tokenizeAnswer1)):
        return True
    return False

def testTokenize2():
    tokenizeAnswer2 = ['[1 2 3 4 5]', 'dup', 'length', '/n', 'exch', 'def', '/fact', '{', '0', 'dict',
                        'begin', '/n', 'exch', 'def', 'n', '2', 'lt', '{', '1', '}', '{', 'n', '1', 'sub',
                        'fact', 'n', 'mul', '}', 'ifelse', 'end', '}', 'def', 'n', 'fact', 'stack']

    if ((tokenize(input2) == tokenizeAnswer2)):
        return True
    return False

def testTokenize3():
    tokenizeAnswer3 = ['[9 9 8 4 10]', '{', 'dup', '5', 'lt', '{', 'pop', '}', 'if', '}', 'forall',
                        'stack']

    if ((tokenize(input3) == tokenizeAnswer3)):
        return True
    return False

def testTokenize4():
    tokenizeAnswer4 = ['[1 2 3 4 5]', 'dup', 'length', 'exch', '{', 'dup', 'mul', '}', 'forall', 'add',
                        'add', 'add', 'add', 'exch', '0', 'exch', '-1', '1', '{', 'dup', 'mul', 'add', '}',
                        'for', 'eq', 'stack']

    if ((tokenize(input4) == tokenizeAnswer4)):
        return True
    return False

def testTokenize5():
    tokenizeAnswer5 = ['true', 'false', 'and', 'false', 'or', 'not', '{', 'false', '}', 'if', 'stack']

    if ((tokenize(input5) == tokenizeAnswer5)):
        return True
    return False

def testTokenize6():
    tokenizeAnswer6 = ['0', '[0.12 -34 476.23 3 -0.023]',
                      '{', 'add', '}', 'forall', '440.327', 'sub', '-5', 
                      'add', '96', 'add', 'stack']
    if (tokenize(input6) == tokenizeAnswer6):
        return True
    return False

def testParse():
    parseAnswer1 = ['/square', ['dup', 'mul'], 'def', [1, 2, 3, 4], ['square'], 'forall', 'add',
                'add', 'add', 30, 'eq', True, 'stack']

    if (parse(tokenize(input1)) == parseAnswer1):
        return True
    return False

def testParse2():
    parseAnswer2 = [[1, 2, 3, 4, 5], 'dup', 'length', '/n', 'exch', 'def', '/fact', [0, 'dict',
                    'begin', '/n', 'exch', 'def', 'n', 2, 'lt', [1], ['n', 1, 'sub', 'fact', 'n',
                    'mul'], 'ifelse', 'end'], 'def', 'n', 'fact', 'stack']

    if (parse(tokenize(input2)) == parseAnswer2):
        return True
    return False

def testParse3():
    parseAnswer3 = [[9, 9, 8, 4, 10], ['dup', 5, 'lt', ['pop'], 'if'], 'forall', 'stack']

    if (parse(tokenize(input3)) == parseAnswer3):
        return True
    return False

def testParse4():
    parseAnswer4 = [[1, 2, 3, 4, 5], 'dup', 'length', 'exch', ['dup', 'mul'], 'forall', 'add', 'add',
                    'add', 'add', 'exch', 0, 'exch', -1, 1, ['dup', 'mul', 'add'], 'for', 'eq',
                    'stack']

    if (parse(tokenize(input4)) == parseAnswer4):
        return True
    return False

def testParse5():
    parseAnswer5 = [True, False, 'and', False, 'or', 'not', [False], 'if', 'stack']

    if (parse(tokenize(input5)) == parseAnswer5):
        return True
    return False

def testParse6():
    parseAnswer6 = [0, [0.12, -34, 476.23, 3, -0.023],
                      ['add'], 'forall', 440.327, 'sub', -5, 
                      'add', 96, 'add', 'stack']

    if (parse(tokenize(input6)) == parseAnswer6):
        return True
    return False

def testInterpereter1():
    clear()
    print("Interpreter Test for INPUT1")
    print("Stack after completion:")
    interpreter(input1)
    if(opPop()):
        if(opPop()):
            return True
    return False

def testInterpereter2():
    clear()
    print("Interpreter Test for INPUT2")
    print("Stack after completion:")
    interpreter(input2)
    if(opPop() == 120):
        if(opPop() == [1, 2, 3, 4, 5]):
            return True
    return False

def testInterpereter3():
    clear()
    print("Interpreter Test for INPUT3")
    print("Stack after completion:")
    interpreter(input3)
    if(opPop() == 10):
        if(opPop() == 8):
            if(opPop() == 9):
                if(opPop() == 9):
                    return True
    return False

def testInterpereter4():
    clear()
    print("Interpreter Test for INPUT4")
    print("Stack after completion:")
    interpreter(input4)
    if(opPop()):
        return True
    return False

def testInterpereter5():
    clear()
    print("Interpreter Test for INPUT5")
    print("Stack after completion:")
    interpreter(input5)
    if(opPop()):
        return False
    return True

def testInterpereter6():
    clear()
    print("Interpreter Test for INPUT6")
    print("Stack after completion:")
    interpreter(input6)
    if(opPop() == 96):
        return True
    return False

def main_part1():
    print("All ERROR statements are printed before the test \nif there is an ERROR and the test is true," +
            "\nwe were trying to break the code\nand the code worked")
    print("-------------------------------------")
    print("testDefine:--------------------------")
    print("Test 1: ", testDefine())
    print("Test 2: ", testDefine2())
    print("Test 3: ", testDefine3())
    print()
    print("-------------------------------------")
    print("testLookup:--------------------------")
    print("Test 1: ", testLookup())
    print("Test 2: ", testLookup2())
    print("Test 3: ", testLookup3())
    print()
    print("-------------------------------------")
    print("testAdd:-----------------------------")
    print("Test 1: ", testAdd())
    print("Test 2: ", testAdd2())
    print("Test 3: ", testAdd3())
    print("Test 4: ", testAdd4())
    print()
    print("-------------------------------------")
    print("testSub:-----------------------------")
    print("Test 1: ", testSub())
    print("Test 2: ", testSub2())
    print("Test 3: ", testSub3())
    print("Test 4: ", testSub4())
    print()
    print("-------------------------------------")
    print("testMul:-----------------------------")
    print("Test 1: ", testMul())
    print("Test 2: ", testMul2())
    print("Test 3: ", testMul3())
    print("Test 4: ", testMul4())
    print()
    print("-------------------------------------")
    print("testDiv:-----------------------------")
    print("Test 1: ", testDiv())
    print("Test 2: ", testDiv2())
    print("Test 3: ", testDiv3())
    print("Test 4: ", testDiv4())
    print()
    print("-------------------------------------")
    print("testEq:------------------------------")
    print("Test 1: ", testEq())
    print("Test 2: ", testEq2())
    print("Test 3: ", testEq3())
    print("Test 4: ", testEq4())
    print()
    print("-------------------------------------")
    print("testLt:------------------------------")
    print("Test 1: ", testLt())
    print("Test 2: ", testLt2())
    print("Test 3: ", testLt3())
    print("Test 4: ", testLt4())
    print()
    print("-------------------------------------")
    print("testGt:------------------------------")
    print("Test 1: ", testGt())
    print("Test 2: ", testGt2())
    print("Test 3: ", testGt3())
    print("Test 4: ", testGt4())
    print()
    print("-------------------------------------")
    print("testPsAnd:---------------------------")
    print("Test 1: ", testPsAnd())
    print("Test 2: ", testPsAnd2())
    print("Test 3: ", testPsAnd3())
    print("Test 4: ", testPsAnd4())
    print("Test 5: ", testPsAnd5())
    print("Test 6: ", testPsAnd6())
    print()
    print("-------------------------------------")
    print("testPsOr:---------------------------")
    print("Test 1: ", testPsOr())
    print("Test 2: ", testPsOr2())
    print("Test 3: ", testPsOr3())
    print("Test 4: ", testPsOr4())
    print("Test 5: ", testPsOr5())
    print("Test 6: ", testPsOr6())
    print()
    print("-------------------------------------")
    print("testPsNot:---------------------------")
    print("Test 1: ", testPsNot())
    print("Test 2: ", testPsNot2())
    print("Test 3: ", testPsNot3())
    print("Test 4: ", testPsNot4())
    print()
    print("-------------------------------------")
    print("testLength:---------------------------")
    print("Test 1: ", testLength())
    print("Test 2: ", testLength2())
    print("Test 3: ", testLength3())
    print("Test 4: ", testLength4())
    print()
    print("-------------------------------------")
    print("testGet:---------------------------")
    print("Test 1: ", testGet())
    print("Test 2: ", testGet2())
    print("Test 3: ", testGet3())
    print("Test 4: ", testGet4())
    print()
    print("-------------------------------------")
    print("testDup---------------------------")
    print("Test 1: ", testDup())
    print("Test 2: ", testDup2())
    print("Test 3: ", testDup3())
    print()
    print("-------------------------------------")
    print("testExch:---------------------------")
    print("Test 1: ", testExch())
    print("Test 2: ", testExch2())
    print("Test 3: ", testExch3())
    print("-------------------------------------")
    print("testPop:---------------------------")
    print("Test 1: ", testPop())
    print("Test 2: ", testPop2())
    print("Test 3: ", testPop3())
    print()
    print("-------------------------------------")
    print("testCopy:---------------------------")
    print("Test 1: ", testCopy())
    print("Test 2: ", testCopy2())
    print("Test 3: ", testCopy3())
    print("Test 4: ", testCopy4())
    print()
    print("-------------------------------------")
    print("testClear:---------------------------")
    print("Test 1: ", testClear())
    print("Test 2: ", testClear2())
    print("Test 3: ", testClear3())
    print()
    print("-------------------------------------")
    print("testDict:----------------------------")
    print("Test 1: ", testDict())
    print("Test 2: ", testDict2())
    print("Test 3: ", testDict3())
    print()
    print("-------------------------------------")
    print("testBeginEnd:------------------------")
    print("Test 1: ", testBeginEnd())
    print("Test 2: ", testBeginEnd2())
    print("Test 3: ", testBeginEnd3())
    print()
    print("-------------------------------------")
    print("testpsDef:---------------------------")
    print("Test 1: ", testpsDef())
    print("Test 2: ", testpsDef2())
    print("Test 3: ", testpsDef3())
    print("Test 4: ", testpsDef4())
    print("Test 5: ", testpsDef5())

def main_part2():
    print("-------------------------------------")
    print("testPsIf:----------------------------")
    print("Test 1: ", testPsIf())
    print("Test 2: ", testPsIf2())
    print("Test 3: ", testPsIf3())
    print("Test 4: ", testPsIf4())
    print("-------------------------------------")
    print("testPsIfElse:------------------------")
    print("Test 1: ", testPsIfElse())
    print("Test 2: ", testPsIfElse2())
    print("Test 3: ", testPsIfElse3())
    print("Test 4: ", testPsIfElse4())
    print("-------------------------------------")
    print("testPsFor:------------------------")
    print("Test 1: ", testPsFor())
    print("Test 2: ", testPsFor2())
    print("Test 3: ", testPsFor3())
    print("Test 4: ", testPsFor4())
    print("-------------------------------------")
    print("testPsFor:------------------------")
    print("Test 1: ", testPsForAll())
    print("Test 2: ", testPsForAll2())
    print("Test 3: ", testPsForAll3())
    print("-------------------------------------")
    print("testTokenize:------------------------")
    print("Test 1: ", testTokenize())
    print("Test 2: ", testTokenize2())
    print("Test 3: ", testTokenize3())
    print("Test 4: ", testTokenize4())
    print("Test 5: ", testTokenize5())
    print("Test 6: ", testTokenize6())
    print("-------------------------------------")
    print("testParse:---------------------------")
    print("Test 1: ", testParse())
    print("Test 2: ", testParse2())
    print("Test 3: ", testParse3())
    print("Test 4: ", testParse4())
    print("Test 5: ", testParse5())
    print("Test 6: ", testParse6())
    print()
    print("-------------------------------------")
    print("#####################################")
    print("testInterpreter:---------------------")
    print("Test 1:*******************")
    print("Is result valid:_" ,testInterpereter1(), '_\n')
    dictPop()
    print("#####################################")
    print("Test 2:*******************")
    print("Is result valid:_" ,testInterpereter2(), '_\n')
    dictPop()
    print("#####################################")
    print("Test 3:*******************")
    print("Is result valid:_" ,testInterpereter3(), '_\n')
    print("#####################################")
    print("Test 4:*******************")
    print("Is result valid:_" ,testInterpereter4(), '_\n')
    print("#####################################")
    print("Test 5:*******************")
    print("Is result valid:_" ,testInterpereter5(), '_\n')
    print("#####################################")
    print("Test 6:*******************")
    print("Is result valid:_" ,testInterpereter6(), '_\n')


if __name__ == '__main__':
    main_part2()