
#Konstantin Shvedov
#Code is intended for Windows 10
import re
import sys
posHelper = 0
posFunction = 0
curScope = ""
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
def dictPush(d, c):
    dictstack.insert(0, (d, c))

#define creates a new dictionary entry
def define(name, value):
    if dictstack:
        dictstack[0][0][name[1:]] = value
    else:
        dictstack.insert(0, ({name[1:]: value}, 0))

#lookup, itterates through the stack to find "name" in static scope
def lookupStatic(name):
    global posHelper
    posHelper = stackSize = len(dictstack) - 1
    if name in dictstack[0][0].keys():
        return dictstack[0][0][name]
    else:
        cur = lookupStaticHelper(name, stackSize - dictstack[0][1])
    if (cur == ""):
        print("Error: No such variable exists")
    else:
        return cur

def lookupStaticHelper(name, pos):
    stackSize = len(dictstack) - 1
    global posHelper
    posHelper = curPos = pos
    if curPos is 0:
        cur = ""
    elif (name in dictstack[curPos][0].keys()):
        posHelper = dictstack[curPos][1]
        cur = dictstack[curPos][0][name]
    else:
        cur = lookupStaticHelper(name, stackSize - dictstack[curPos][1])
    if (cur == ""):
        print("Error: No such variable exists")
    else:
        return cur

#lookup, itterates through the stack to find "name" in dynamic scope
def lookupDynamic(name):
    for item in dictstack:
        if name in item[0].keys():
            return item[0][name]
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
        if(numCopy == 2):
            opPush(opstack[opLength - 2])
            opPush(opstack[opLength - 2])
        elif(numCopy <= len(opstack)):
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
    print("==============")
    if(len(opstack) > 0):
        for elem in (opstack):
            print(elem)
    else:
        print("")
    print("==============")
    i = len(dictstack) - 1
    for item in dictstack:
        print("----", i, "----", item[1], "----")
        i -= 1
        for vars in item[0]:
            print(vars, "\t", item[0][vars])
    print("==============")

#--------------------------------------------------------------------------#
############################################################################
#Dictionary manipulation operators
#----------------------------------PART 6----------------------------------#

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
        interpretTop(opPop(), curScope)
        tempTop = opPop()
        if (isinstance(tempTop, bool)):
            if (tempTop):
                interpretSPS(temp, curScope)
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
        interpretTop(opPop(), curScope)
        tempTop = opPop()
        global posHelper
        if (isinstance(tempTop, bool)):
            if (tempTop):
                posHelper = dictstack[0][1]
                interpretSPS(tempBot, curScope)
            else:
                posHelper = dictstack[0][1]
                interpretSPS(temp, curScope)
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
                interpretSPS(proc, curScope)
                itter += incr
        elif incr < 0:
            while (itter >= limit):
                opPush(itter)
                interpretSPS(proc, curScope)
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
                interpretSPS(proc, curScope)
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
def interpreter(s, scope): # s is a string
    global curScope
    curScope = scope
    interpretSPS(parse(tokenize(s)), scope)

def interpretSPS(code, scope): # code is a code array
    #print("################Going Deeper################")
    global posHelper
    dictPush({}, posHelper)
    posHelper = 0
    for elem in code:
        interpretTop(elem, scope)
    end()
    #print("################Releasing################")

#this is the string interpreter that depending on the string calls a function
def interpretTop(topVar, scope):
    #print("Input: ", topVar)
    #stack()
    #print("------------------------------------------------------------------------")
    global posFunction
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
        if scope is "static":
            tempVar = lookupStatic(topVar)
        elif scope is "dynamic":
            tempVar = lookupDynamic(topVar)
        if (isinstance(tempVar, list)):
            if (all(isinstance(x, int) for x in tempVar)):
                opPush(tempVar)
            else:
                interpretSPS(tempVar, scope)
        else:
            opPush(tempVar)
    #stack()
    #print()
    #print()
    #print()
    #print()
    #print()

#--------------------------------------------------------------------------#
############################################################################
############################################################################
#----------------------------------TESTING---------------------------------#

###########################
#!!!!INSTRUCTORS CASES!!!!#
###########################

testCase1P3 = """
        /m 50 def
        /n 100 def
        /egg1 {/m 25 def n} def
        /chic {
         /n 1 def
         /egg2 { n } def
         m n
         egg1
         egg2
         stack } def
        n
        chic    """

testCase2P3 = """
        /x 10 def
        /A { x } def
        /C { /x 40 def A stack } def
        /B { /x 30 def /A { x } def C } def
        B    """

###########################
#!!!!!!!!MY  CASES!!!!!!!!#
###########################
testCase3P3 = """
        /x 11 def
        /A { x stack} def
        /B { x /x 5 def A } def
        /C { x /x 4 def B } def
        /D { x /x 3 def C } def
        /E { x /x 2 def D } def
        /F { x /x 1 def E } def
        F    """

testCase4P3 = """
        /x 11 def
        /A { x stack} def
        /B { x /x 5 def A } def
        /D { /C { x /x 4 def B } def x /x 3 def C } def
        /E { x /x 2 def D } def
        /F { x /x 1 def E } def
        F    """

testCase5P3 = """ 
  [1 2 3 4 5] dup length /n exch def
  /fact {
         0 /n exch def
         n 2 lt
         { 1 /C { n /n 4 def n stack} def n /n 3 def C}
         {n 1 sub fact n mul stack}
         ifelse
  } def
  n fact
"""

testCase6P3 = """
  /x 200 def [9 9 8 4 10] {/x 300 def  dup 5 lt
    /i {/x 400 def {pop x stack} if} def i}  forall
"""

passedTests = 1
def test1_1():
    global passedTests
    interpreter(testCase1P3,"static")
    if (opPop() is 1 and opPop() is 100 and opPop() is 1 and opPop() is 50
        and opPop() is 100):
        print("TEST PASSED")
    else:
        print("Failed")
        passedTests = 0
    dictstack = []
    
def test1_2():
    global passedTests
    interpreter(testCase1P3,"dynamic")
    if (opPop() is 1 and opPop() is 1 and opPop() is 1 and opPop() is 50
        and opPop() is 100):
        print("TEST PASSED")
    else:
        print("Failed")
        passedTests = 0
    dictstack = []

def test2_1():
    global passedTests
    interpreter(testCase2P3,"static")
    if (opPop() is 10):
        print("TEST PASSED")
    else:
        print("Failed")
        passedTests = 0
    dictstack = []

def test2_2():
    global passedTests
    interpreter(testCase2P3,"dynamic")
    if (opPop() is 40):
        print("TEST PASSED")
    else:
        print("Failed")
        passedTests = 0
    dictstack = []

def test3_1():
    global passedTests
    interpreter(testCase3P3,"static")
    if (opPop() is 11 and opPop() is 11 and opPop() is 11 and opPop() is 11
        and opPop() is 11 and opPop() is 11):
        print("TEST PASSED")
    else:
        print("Failed")
        passedTests = 0
    dictstack = []
    
def test3_2():
    global passedTests
    interpreter(testCase3P3,"dynamic")
    if (opPop() is 5 and opPop() is 4 and opPop() is 3 and opPop() is 2
        and opPop() is 1 and opPop() is 11):
        print("TEST PASSED")
    else:
        print("Failed")
        passedTests = 0
    dictstack = []

def test4_1():
    global passedTests
    interpreter(testCase4P3,"static")
    if (opPop() is 11 and opPop() is 11 and opPop() is 3 and opPop() is 11
        and opPop() is 11 and opPop() is 11):
        print("TEST PASSED")
    else:
        print("Failed")
        passedTests = 0
    dictstack = []
    
def test4_2():
    global passedTests
    interpreter(testCase4P3,"dynamic")
    if (opPop() is 5 and opPop() is 4 and opPop() is 3 and opPop() is 2
        and opPop() is 1 and opPop() is 11):
        print("TEST PASSED")
    else:
        print("Failed")
        passedTests = 0
    dictstack = []

def test5_1():
    global passedTests
    interpreter(testCase5P3,"static")
    if (opPop() is 4 and opPop() is 3 and opPop() is 5 and opPop() is 1
        and opPop() is 5 and opPop() == [1, 2, 3, 4, 5]):
        print("TEST PASSED")
    else:
        print("Failed")
        passedTests = 0
    dictstack = []
    
def test5_2():
    global passedTests
    interpreter(testCase5P3,"dynamic")
    if (opPop() is 4 and opPop() is 3 and opPop() is 0 and opPop() is 1
        and opPop() is 5 and opPop() == [1, 2, 3, 4, 5]):
        print("TEST PASSED")
    else:
        print("Failed")
        passedTests = 0
    dictstack = []

def test6_1():
    global passedTests
    interpreter(testCase6P3,"static")
    if (opPop() is 10 and opPop() is 200 and opPop() is 8 and opPop() is 9
        and opPop() is 9):
        print("TEST PASSED")
    else:
        print("Failed")
        passedTests = 0
    dictstack = []
    
def test6_2():
    global passedTests
    interpreter(testCase6P3,"dynamic")
    if (opPop() == 10 and opPop() == 400):
        print("TEST PASSED")
    else:
        print("Failed")
        passedTests = 0
    dictstack = []

if __name__ == '__main__':
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("!!!!!!!!!!!!!!!!!!GIVEN TEST CASES!!!!!!!!!!!!!!!!!!!!!!")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("Test 1: Static")
    print()
    test1_1()
    print()
    print()

    print("Test 1: Dynamic")
    print()
    test1_2()
    print()
    print()

    print("Test 2: Static")
    print()
    test2_1()
    print()
    print()

    print("Test 2: Dynamic")
    print()
    test2_2()
    print()
    print()

    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("!!!!!!!!!!!!!!!!!!!!!MY TEST CASES!!!!!!!!!!!!!!!!!!!!!!")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    print("Test 3: Static")
    print()
    test3_1()
    print()
    print()

    print("Test 3: Dynamic")
    print()
    test3_2()
    print()
    print()
    
    print("Test 4: Static")
    print()
    test4_1()
    print()
    print()

    print("Test 4: Dynamic")
    print()
    test4_2()
    print()
    print()
    
    print("Test 5: Static")
    print()
    test5_1()
    print()
    print()

    print("Test 5: Dynamic")
    print()
    test5_2()
    print()
    print()

    print("Test 6: Static")
    print()
    test6_1()
    print()
    print()

    print("Test 6: Dynamic")
    print()
    test6_2()
    print()
    print()

    if passedTests is 1:
        print("ALL TESTS PASSED")
    else:
        print("NOT ALL PASSED")