#Konstantin Shvedov
#Code is intended for Windows 10
import re
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
        return dictstack.pop(0);
    else:
        print("Error: Dictionary Stack Empty")

#dictPush adds an element to the stack
def dictPush(d):
    dictstack.insert(0, d)

#define creates a new dictionary entry
def define(name, value):
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
        for elem in reversed(opstack):
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
            define(defName, defVal)
        else:
            print("Error: Invalid type")
    else:
        print("Error: not enough operands in stack")


#--------------------------------------------------------------------------#
############################################################################
############################################################################
#----------------------------------TESTING---------------------------------#
def testDefine():
    define("/n1", 4)
    if lookup("n1") != 4:
        return False
    return True

def testDefine2():
    define("/n1", 4)
    define("/n1", 8)
    if lookup("n1") != 8:
        return False
    return True

def testDefine3():
    define("/n1", 4)
    define("/n2", 9)
    define("/n2", 6)
    define("/n2", 7)
    define("/n3", 8)
    define("/n4", 0)
    if lookup("n2") != 7:
        return False
    return True

def testLookup():
    opPush("/n1")
    opPush(3)
    psDef()
    if lookup("n1") != 3:
        return False
    return True

def testLookup2():
    opPush(4)
    opPush("/test")
    psDef()
    if lookup("test") != 4:
        return True
    return False

def testLookup3():
    dictPop()
    if lookup("n1") != 3:
        return True
    return False

#Arithmatic operator tests
def testAdd():
    opPush(1)
    opPush(2)
    add()
    if opPop() != 3:
        return False
    return True

def testAdd2():
    opPush(1)
    opPush(2)
    opPush(5)
    add()
    add()
    if opPop() != 8:
        return False
    return True

def testAdd3():
    opPush(1)
    add()
    if opPop() != 1:
        return False
    return True

def testAdd4():
    opPush("hello")
    opPush(1)
    add()
    if opPop() != 1:
        return False
    return True

def testSub():
    clear()
    opPush(10)
    opPush(4.5)
    sub()
    if opPop() != 5.5:
        return False
    return True

def testSub2():
    opPush(10)
    opPush(4.5)
    opPush(1)
    sub()
    sub()
    if opPop() != 6.5:
        return False
    return True

def testSub3():
    opPush(10)
    sub()
    if opPop() != 10:
        return False
    return True

def testSub4():
    opPush("Test")
    opPush(4.5)
    sub()
    if opPop() != 4.5:
        return False
    return True

def testMul():
    clear()
    opPush(2)
    opPush(4.5)
    mul()
    if opPop() != 9:
        return False
    return True

def testMul2():
    opPush(2)
    opPush(4.5)
    opPush(2)
    mul()
    mul()
    if opPop() != 18:
        return False
    return True

def testMul3():
    opPush(2)
    mul()
    if opPop() != 2:
        return False
    return True

def testMul4():
    opPush("Test")
    opPush(2)
    mul()
    if opPop() != 2:
        return False
    return True

def testDiv():
    clear()
    opPush(10)
    opPush(4)
    div()
    if opPop() != 2.5:
        return False
    return True

def testDiv2():
    opPush(10)
    opPush(4)
    opPush(2)
    div()
    div()
    if opPop() != 5:
        return False
    return True

def testDiv3():
    opPush(10)
    div()
    if opPop() != 10:
        return False
    return True

def testDiv4():
    opPush("Test")
    opPush(4)
    div()
    if opPop() != 4:
        return False
    return True
    
#Comparison operators tests
def testEq():
    clear()
    opPush(6)
    opPush(6)
    eq()
    if opPop() != True:
        return False
    return True

def testEq2():
    clear()
    opPush(6)
    opPush(5)
    eq()
    if opPop() != False:
        return False
    return True

def testEq3():
    opPush(6)
    eq()
    if opPop() != 6:
        return False
    return True

def testEq4():
    opPush("Test")
    opPush(6)
    eq()
    if opPop() != 6:
        return False
    return True

def testLt():
    clear()
    opPush(3)
    opPush(6)
    lt()
    if opPop() != True:
        return False
    return True

def testLt2():
    opPush(6)
    opPush(3)
    lt()
    if opPop() != False:
        return False
    return True

def testLt3():
    opPush(6)
    lt()
    if opPop() != 6:
        return False
    return True

def testLt4():
    opPush("Test")
    opPush(6)
    lt()
    if opPop() != 6:
        return False
    return True

def testGt():
    clear()
    opPush(3)
    opPush(6)
    gt()
    if opPop() != False:
        return False
    return True

def testGt2():
    opPush(6)
    opPush(3)
    gt()
    if opPop() != True:
        return False
    return True

def testGt3():
    opPush(6)
    gt()
    if opPop() != 6:
        return False
    return True

def testGt4():
    opPush("Test")
    opPush(6)
    gt()
    if opPop() != 6:
        return False
    return True

#boolean operator tests
def testPsAnd():
    clear()
    opPush(True)
    opPush(False)
    psAnd()
    if opPop() != False:
        return False
    return True

def testPsAnd2():
    opPush(True)
    opPush(True)
    psAnd()
    if opPop() != True:
        return False
    return True

def testPsAnd3():
    opPush(False)
    opPush(False)
    psAnd()
    if opPop() != False:
        return False
    return True

def testPsAnd4():
    opPush(False)
    opPush(True)
    psAnd()
    if opPop() != False:
        return False
    return True

def testPsAnd5():
    opPush(True)
    psAnd()
    if opPop() != True:
        return False
    return True

def testPsAnd6():
    opPush("Test")
    opPush(False)
    psAnd()
    if opPop() != False:
        return False
    return True

def testPsOr():
    clear()
    opPush(True)
    opPush(False)
    psOr()
    if opPop() != True:
        return False
    return True

def testPsOr2():
    opPush(True)
    opPush(True)
    psOr()
    if opPop() != True:
        return False
    return True

def testPsOr3():
    opPush(False)
    opPush(True)
    psOr()
    if opPop() != True:
        return False
    return True

def testPsOr4():
    opPush(False)
    opPush(False)
    psOr()
    if opPop() != False:
        return False
    return True

def testPsOr5():
    opPush(False)
    psOr()
    if opPop() != False:
        return False
    return True

def testPsOr6():
    opPush("Test")
    opPush(False)
    psOr()
    if opPop() != False:
        return False
    return True

def testPsNot():
    opPush(True)
    psNot()
    if opPop() != False:
        return False
    return True

def testPsNot2():
    opPush(False)
    psNot()
    if opPop() != True:
        return False
    return True

def testPsNot3():
    opPush("Test")
    psNot()
    if opPop() != "Test":
        return False
    return True

def testPsNot4():
    psNot()
    opPush(5)
    if opPop() != 5:
        return False
    return True

#Array operator tests
def testLength():
    opPush([1,2,3,4,5])
    length()
    if opPop() != 5:
        return False
    return True

def testLength2():
    opPush([1])
    length()
    if opPop() != 1:
        return False
    return True

def testLength3():
    clear()
    length()
    opPush(5)
    if opPop() != 5:
        return False
    return True

def testLength4():
    opPush("Test")
    length()
    if opPop() != "Test":
        return False
    return True

def testGet():
    opPush([1,2,3,4,5])
    opPush(4)
    get()
    if opPop() != 5:
        return False
    return True

def testGet2():
    opPush([1,2,3,4,5])
    opPush(5)
    get()
    if opPop() != 5:
        return False
    return True

def testGet3():
    clear()
    opPush("Stack")
    opPush(4)
    get()
    if opPop() != 4:
        return False
    return True

def testGet4():
    clear()
    opPush(4)
    get()
    if opPop() != 4:
        return False
    return True

#stack manipulation functions
def testDup():
    opPush(10)
    dup()
    if opPop()!=opPop():
        return False
    return True

def testDup2():
    dup()
    opPush(5)
    if opPop()!= 5:
        return False
    return True

def testDup3():
    opPush(5)
    dup()
    dup()
    if opPop() != opPop():
        return False
    return True

def testExch():
    clear()
    opPush(10)
    opPush("/x")
    exch()
    if opPop()!=10 and opPop()!="/x":
        return False
    return True

def testExch2():
    opPush(10)
    opPush("/x")
    opPush(10)
    exch()
    if opPop()!="/x" and opPop()!=10:
        return False
    return True

def testExch3():
    clear()
    opPush("/x")
    exch()
    if opPop()!="/x":
        return False
    return True

def testPop():
    l1 = len(opstack)
    opPush(10)
    pop()
    l2= len(opstack)
    if l1!=l2:
        return False
    return True

def testPop2():
    l1 = len(opstack)
    pop()
    l2= len(opstack)
    if l1!=l2:
        return False
    return True

def testPop3():
    l1 = len(opstack)
    opPush(10)
    opPush(10)
    pop()
    l2= len(opstack)
    if l1==l2:
        return False
    return True

def testCopy():
    opPush(1)
    opPush(2)
    opPush(3)
    opPush(4)
    opPush(5)
    opPush(2)
    copy()
    if opPop()!=5 and opPop()!=4 and opPop()!=5 and opPop()!=4 and opPop()!=3 and opPop()!=2:
        return False
    return True

def testCopy2():
    clear()
    opPush(4)
    opPush(5)
    opPush(3)
    copy()
    if opPop()!=3 and opPop()!=5 and opPop()!=4:
        return False
    return True

def testCopy3():
    clear()
    opPush(5)
    copy()
    if opPop() != 5:
        return False
    return True

def testCopy4():
    opPush(1)
    opPush(1)
    copy()
    if opPop()!=1 and opPop()!=1:
        return False
    return True

def testClear():
    opPush(10)
    opPush("/x")
    clear()
    if len(opstack)!=0:
        return False
    return True

def testClear2():
    opPush(10)
    opPush(10)
    opPush(10)
    opPush(10)
    opPush(10)
    opPush(10)
    opPush(10)
    opPush(10)
    clear()
    if len(opstack)!=0:
        return False
    return True

def testClear3():
    clear()
    if len(opstack)!=0:
        return False
    return True

#dictionary stack operators
def testDict():
    opPush(1)
    psDict()
    if opPop()!={}:
        return False
    return True

def testDict2():
    opPush(1)
    opPush(2)
    opPush(3)
    psDict()
    if opPop()!={}:
        return False
    return True

def testDict3():
    dictPop()
    dictPop()
    dictPop()
    dictPop()
    dictPop()
    dictPop()
    dictPop()
    dictPop()
    dictPop()
    opPush(1)
    psDict()
    if opPop()!={}:
        return True
    return False

def testBeginEnd():
    opPush("/x")
    opPush(3)
    psDef()
    opPush({})
    begin()
    opPush("/x")
    opPush(4)
    psDef()
    end()
    if lookup("x")!=3:
        return False
    return True

def testBeginEnd2():
    dictPop()
    dictPop()
    begin()
    end()
    if lookup("x")!=3:
        return True
    return False

def testBeginEnd3():
    opPush("/x")
    opPush(3)
    psDef()
    opPush("/y")
    opPush(3)
    psDef()
    opPush("/x")
    opPush(7)
    psDef()
    opPush({})
    begin()
    opPush("/x")
    opPush(6)
    psDef()
    end()
    if lookup("x")!=7:
        return False
    return True

def testpsDef():
    opPush("/x")
    opPush(10)
    psDef()
    if lookup("x")!=10:
        return False
    return True

def testpsDef2():
    opPush("/x")
    opPush(10)
    psDef()
    opPush(1)
    psDict()
    begin()
    if lookup("x")!=10:
        end()
        return False
    end()
    return True

def testpsDef3():
    opPush("/x")
    opPush(10)
    psDef()
    opPush("/x")
    opPush(21)
    psDef()
    opPush("/x")
    opPush(32)
    psDef()
    if lookup("x")!=32:
        return False
    return True

def testpsDef4():
    opPush(10)
    opPush("/x")
    psDef()
    if lookup("x")!=32:
        return False
    return True

def testpsDef5():
    clear()
    opPush("/x")
    psDef()
    if opPop()!="/x":
        return False
    return True

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

if __name__ == '__main__':
    print(main_part1())