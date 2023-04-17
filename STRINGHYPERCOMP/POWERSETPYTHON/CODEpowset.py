
frame = 0

# Python program to illustrate the intersection
# of two lists using set() and intersection()

def powerSet(L):
    global frame
    frame += 1
    if len(L) == 0:
        # print('\nbase case, frame is', frame)
        # print('returning [[]]')
        return [[]]
    else:
        # print('\npre-recursive, frame', frame)
        # print('list in this frame is ', L)
        # print('operator in this frame is ', L[-1:])
        base = powerSet(L[:-1])
        operator = L[-1:]
        frame -= 1
        # print('\npost-recursive, frame', frame)
        # print('base in this frame is', base)
        # print('operated on by', operator)
        r = base + [(b + operator) for b in base]
        # print('returning', r)
        return r

print('global frame is', frame)

L = ['a', 'b', 'c', 'd', 'c', 'd', 'd', 'e']
L = ['', '', '', '', '', '','', '', '', '', '', '']
L = ['a', 'b', 'c', 'd', 'e']
print('L =', L)
POWSETS=powerSet(L)
print('POWER SETS')
print(POWSETS)
xx=0
TOTAL=[]
TOTALclusters=[]
streetno = {}
for itemx in POWSETS:
    stx=xx
    QA=[itemx,stx, xx,[int(n) for n in bin(xx)[2:].zfill(len(L))]]
    TOTAL.extend(QA)
    for itemx11 in L:
        if itemx11 in itemx:
            stxq=[[itemx11,stx]]
            TOTALclusters.extend(stxq)
    xx=xx+1

streetno = {}
for itemx22 in L:
    TOTAL=[]
    print('STATE' +' '+' '+ itemx22)
    for itemx11 in TOTALclusters:
        if itemx22 == itemx11[0]:
            TOTAL.extend(itemx11[1:])
    streetno[itemx22] = TOTAL
    print((TOTAL))

print('INTERSECTIONS BETWEEN STATES')
for i in L:
    a=streetno[i]
    for  j in L:
        b=streetno[j]
        if i != j:
            www=list(set(a) & set(b))
            # sorts the list in place
            www.sort()
            # this prints the ordered list
            print(i + ' and '+ j + ' has size '+ str(len(www)))
            print("Ordered intersected list: ", www)

    
























frame = 0

# Python program to illustrate the intersection
# of two lists using set() and intersection()

def powerSet(L):
    global frame
    frame += 1
    if len(L) == 0:
        # print('\nbase case, frame is', frame)
        # print('returning [[]]')
        return [[]]
    else:
        # print('\npre-recursive, frame', frame)
        # print('list in this frame is ', L)
        # print('operator in this frame is ', L[-1:])
        base = powerSet(L[:-1])
        operator = L[-1:]
        frame -= 1
        # print('\npost-recursive, frame', frame)
        # print('base in this frame is', base)
        # print('operated on by', operator)
        r = base + [(b + operator) for b in base]
        # print('returning', r)
        return r

print('global frame is', frame)

L = ['a', 'b', 'c', 'd', 'c', 'd', 'd', 'e']
L = ['', '', '', '', '', '','', '', '', '', '', '']
L = ['a', 'b', 'c', 'd', 'e']
print('L =', L)
POWSETS=powerSet(L)
xx=0
TOTAL=[]
TOTALclusters=[]
streetno = {}
for itemx in POWSETS:
    stx=xx
    QA=[itemx,stx, xx,[int(n) for n in bin(xx)[2:].zfill(len(L))]]
    TOTAL.extend(QA)
    for itemx11 in L:
        if itemx11 in itemx:
            stxq=[[itemx11,stx]]
            TOTALclusters.extend(stxq)
    xx=xx+1

streetno = {}
for itemx22 in L:
    TOTAL=[]
    print(itemx22)
    for itemx11 in TOTALclusters:
        if itemx22 == itemx11[0]:
            TOTAL.extend(itemx11[1:])
    streetno[itemx22] = TOTAL
    print((TOTAL))

print('&&&')
for i in L:
    a=streetno[i]
    for  j in L:
        b=streetno[j]
        if i != j:
            print(i+j)
            www=list(set(a) & set(b))
            # sorts the list in place
            www.sort()
            # this prints the ordered list
            print(len(www))
            print("Ordered list: ", www)

    






























frame = 0

# Python program to illustrate the intersection
# of two lists using set() and intersection()

def powerSet(L):
    global frame
    frame += 1
    if len(L) == 0:
        # print('\nbase case, frame is', frame)
        # print('returning [[]]')
        return [[]]
    else:
        # print('\npre-recursive, frame', frame)
        # print('list in this frame is ', L)
        # print('operator in this frame is ', L[-1:])
        base = powerSet(L[:-1])
        operator = L[-1:]
        frame -= 1
        # print('\npost-recursive, frame', frame)
        # print('base in this frame is', base)
        # print('operated on by', operator)
        r = base + [(b + operator) for b in base]
        # print('returning', r)
        return r

print('global frame is', frame)

L = ['a', 'b', 'c', 'd', 'c', 'd']
L = ['', '', '', '', '', '','', '', '', '', '', '']
L = ['a', 'b', 'c', 'd', 'e']
print('L =', L)
POWSETS=powerSet(L)
xx=0
TOTAL=[]
TOTALclusters=[]
streetno = {}
for itemx in POWSETS:
    stx=xx
    QA=[itemx,stx, xx,[int(n) for n in bin(xx)[2:].zfill(len(L))]]
    TOTAL.extend(QA)
    for itemx11 in L:
        if itemx11 in itemx:
            stxq=[[itemx11,stx]]
            TOTALclusters.extend(stxq)
    xx=xx+1

streetno = {}
for itemx22 in L:
    TOTAL=[]
    print(itemx22)
    for itemx11 in TOTALclusters:
        if itemx22 == itemx11[0]:
            TOTAL.extend(itemx11[1:])
    streetno[itemx22] = TOTAL
    print((TOTAL))

print('&&&')
for i in L:
    a=streetno[i]
    for  j in L:
        b=streetno[j]
        if i != j:
            print(i+j)
            www=list(set(a) & set(b))
            # sorts the list in place
            www.sort()
            # this prints the ordered list
            print(len(www))
            print("Ordered list: ", www)

    
    

























frame = 0

# Python program to illustrate the intersection
# of two lists using set() and intersection()
def Intersection(lst1, lst2):
    return set(lst1).intersection(lst2)
    
def powerSet(L):
    global frame
    frame += 1
    if len(L) == 0:
        # print('\nbase case, frame is', frame)
        # print('returning [[]]')
        return [[]]
    else:
        # print('\npre-recursive, frame', frame)
        # print('list in this frame is ', L)
        # print('operator in this frame is ', L[-1:])
        base = powerSet(L[:-1])
        operator = L[-1:]
        frame -= 1
        # print('\npost-recursive, frame', frame)
        # print('base in this frame is', base)
        # print('operated on by', operator)
        r = base + [(b + operator) for b in base]
        # print('returning', r)
        return r

print('global frame is', frame)

L = ['a', 'b', 'c', 'd', 'c', 'd']
L = ['', '', '', '', '', '','', '', '', '', '', '']
L = ['a', 'b', 'c', 'd', 'f', 'g', 'j']
print('L =', L)
POWSETS=powerSet(L)
xx=0
TOTAL=[]
TOTALclusters=[]
streetno = {}
for itemx in POWSETS:
    stx=xx
    QA=[itemx,stx, xx,[int(n) for n in bin(xx)[2:].zfill(len(L))]]
    TOTAL.extend(QA)
    for itemx11 in L:
        if itemx11 in itemx:
            stxq=[[itemx11,stx]]
            TOTALclusters.extend(stxq)
    xx=xx+1

streetno = {}
for itemx22 in L:
    TOTAL=[]
    print(itemx22)
    for itemx11 in TOTALclusters:
        if itemx22 == itemx11[0]:
            TOTAL.extend(itemx11[1:])
    streetno[itemx22] = TOTAL
    print((TOTAL))

print('&&&')
a=streetno['a']
b=streetno['d']
www=list(set(a) & set(b))
# this prints the unordered list
print("Unordered list: ", www)
# sorts the list in place
www.sort()
# this prints the ordered list
print("Ordered list: ", www)


frame = 0

def powerSet(L):
    global frame
    frame += 1
    if len(L) == 0:
        # print('\nbase case, frame is', frame)
        # print('returning [[]]')
        return [[]]
    else:
        # print('\npre-recursive, frame', frame)
        # print('list in this frame is ', L)
        # print('operator in this frame is ', L[-1:])
        base = powerSet(L[:-1])
        operator = L[-1:]
        frame -= 1
        # print('\npost-recursive, frame', frame)
        # print('base in this frame is', base)
        # print('operated on by', operator)
        r = base + [(b + operator) for b in base]
        # print('returning', r)
        return r

print('global frame is', frame)

L = ['a', 'b', 'c', 'd', 'c', 'd']
L = ['', '', '', '', '', '','', '', '', '', '', '']
L = ['a', 'b', 'c', 'd', 'f', 'g', 'j']
print('L =', L)
POWSETS=powerSet(L)
xx=0
TOTAL=[]
TOTALclusters=[]
streetno = {}
for itemx in POWSETS:
    stx='e' + str(xx)
    QA=[itemx,stx, xx,[int(n) for n in bin(xx)[2:].zfill(len(L))]]
    TOTAL.extend(QA)
    for itemx11 in L:
        if itemx11 in itemx:
            stxq=[[itemx11,stx]]
            TOTALclusters.extend(stxq)
    xx=xx+1

streetno = {}
for itemx22 in L:
    TOTAL=[]
    print(itemx22)
    for itemx11 in TOTALclusters:
        if itemx22 == itemx11[0]:
            TOTAL.extend(itemx11[1:])
    streetno[itemx22] = TOTAL
    print((TOTAL))

print(list(set(streetno['a']) & set(streetno['c'])))
   




























frame = 0

def powerSet(L):
    global frame
    frame += 1
    if len(L) == 0:
        # print('\nbase case, frame is', frame)
        # print('returning [[]]')
        return [[]]
    else:
        # print('\npre-recursive, frame', frame)
        # print('list in this frame is ', L)
        # print('operator in this frame is ', L[-1:])
        base = powerSet(L[:-1])
        operator = L[-1:]
        frame -= 1
        # print('\npost-recursive, frame', frame)
        # print('base in this frame is', base)
        # print('operated on by', operator)
        r = base + [(b + operator) for b in base]
        # print('returning', r)
        return r

print('global frame is', frame)

L = ['a', 'b', 'c', 'd', 'c', 'd']
L = ['', '', '', '', '', '','', '', '', '', '', '']
L = ['a', 'b', 'c', 'd', 'f', 'g', 'j']
print('L =', L)
POWSETS=powerSet(L)
xx=0
TOTAL=[]
TOTALclusters=[]
streetno = {}
for itemx in POWSETS:
    stx='e' + str(xx)
    QA=[itemx,stx, xx,[int(n) for n in bin(xx)[2:].zfill(len(L))]]
    TOTAL.extend(QA)
    for itemx11 in L:
        if itemx11 in itemx:
            stxq=[[itemx11,stx]]
            TOTALclusters.extend(stxq)
    xx=xx+1

streetno = {}
for itemx22 in L:
    TOTAL=[]
    print(itemx22)
    for itemx11 in TOTALclusters:
        if itemx22 == itemx11[0]:
            TOTAL.extend(itemx11[1:])
    streetno[itemx22] = TOTAL
    print(len(TOTAL))










frame = 0

def powerSet(L):
    global frame
    frame += 1
    if len(L) == 0:
        # print('\nbase case, frame is', frame)
        # print('returning [[]]')
        return [[]]
    else:
        # print('\npre-recursive, frame', frame)
        # print('list in this frame is ', L)
        # print('operator in this frame is ', L[-1:])
        base = powerSet(L[:-1])
        operator = L[-1:]
        frame -= 1
        # print('\npost-recursive, frame', frame)
        # print('base in this frame is', base)
        # print('operated on by', operator)
        r = base + [(b + operator) for b in base]
        # print('returning', r)
        return r

print('global frame is', frame)

L = ['a', 'b', 'c', 'd', 'c', 'd']
L = ['', '', '', '', '', '','', '', '', '', '', '']
L = ['a', 'b', 'c', 'd', 'f', 'g', 'j']
print('L =', L)
POWSETS=powerSet(L)
xx=0
TOTAL=[]
TOTALclusters=[]
streetno = {}
for itemx in POWSETS:
    stx='e' + str(xx)
    QA=[itemx,stx, xx,[int(n) for n in bin(xx)[2:].zfill(len(L))]]
    TOTAL.extend(QA)
    for itemx11 in L:
        if itemx11 in itemx:
            stxq=[[itemx11,stx]]
            TOTALclusters.extend(stxq)
    xx=xx+1

streetno = {}
for itemx22 in L:
    TOTAL=[]
    print(itemx22)
    for itemx11 in TOTALclusters:
        if itemx22 == itemx11[0]:
            TOTAL.extend(itemx11[1])
    streetno[itemx22] = TOTAL   



frame = 0

def powerSet(L):
    global frame
    frame += 1
    if len(L) == 0:
        # print('\nbase case, frame is', frame)
        # print('returning [[]]')
        return [[]]
    else:
        # print('\npre-recursive, frame', frame)
        # print('list in this frame is ', L)
        # print('operator in this frame is ', L[-1:])
        base = powerSet(L[:-1])
        operator = L[-1:]
        frame -= 1
        # print('\npost-recursive, frame', frame)
        # print('base in this frame is', base)
        # print('operated on by', operator)
        r = base + [(b + operator) for b in base]
        # print('returning', r)
        return r

print('global frame is', frame)

L = ['a', 'b', 'c', 'd', 'c', 'd']
L = ['', '', '', '', '', '','', '', '', '', '', '']
L = ['a', 'b', 'c', 'd', 'f', 'g', 'j']
print('L =', L)
POWSETS=powerSet(L)
xx=0
TOTAL=[]
TOTALclusters=[]
streetno = {}
for itemx in POWSETS:
    stx='e' + str(xx)
    QA=[itemx,stx, xx,[int(n) for n in bin(xx)[2:].zfill(len(L))]]
    TOTAL.extend(QA)
    for itemx11 in L:
        if itemx11 in itemx:
            stxq=[[itemx11,stx]]
            TOTALclusters.extend(stxq)
    xx=xx+1
    
for itemx11 in TOTALclusters:
    for itemx22 in L:
        if itemx22 == itemx11[0]:
            print(itemx11)
          




































frame = 0

def powerSet(L):
    global frame
    frame += 1
    if len(L) == 0:
        # print('\nbase case, frame is', frame)
        # print('returning [[]]')
        return [[]]
    else:
        # print('\npre-recursive, frame', frame)
        # print('list in this frame is ', L)
        # print('operator in this frame is ', L[-1:])
        base = powerSet(L[:-1])
        operator = L[-1:]
        frame -= 1
        # print('\npost-recursive, frame', frame)
        # print('base in this frame is', base)
        # print('operated on by', operator)
        r = base + [(b + operator) for b in base]
        # print('returning', r)
        return r

print('global frame is', frame)
L = ['a', 'b', 'c', 'd','e']
print('L =', L)
POWSETS=powerSet(L)
Lx = ['a', 'b', 'c', 'd','e']
for itemx in Lx:
    xx=0
    for item in POWSETS:
        if itemx in item:
            xx=xx+1
            print(item)
    print(xx)



print('global frame is', frame)
L = ['a', 'b', 'c', 'd','e']
print('L =', L)
POWSETS=powerSet(L)
xx=0
TOTAL=[]
for itemx in POWSETS:
    QA=[itemx,xx,[int(n) for n in bin(xx)[2:].zfill(len(L))]]
    print(QA)
    xx=xx+1







frame = 0

def powerSet(L):
    global frame
    frame += 1
    if len(L) == 0:
        # print('\nbase case, frame is', frame)
        # print('returning [[]]')
        return [[]]
    else:
        # print('\npre-recursive, frame', frame)
        # print('list in this frame is ', L)
        # print('operator in this frame is ', L[-1:])
        base = powerSet(L[:-1])
        operator = L[-1:]
        frame -= 1
        # print('\npost-recursive, frame', frame)
        # print('base in this frame is', base)
        # print('operated on by', operator)
        r = base + [(b + operator) for b in base]
        # print('returning', r)
        return r

print('global frame is', frame)

L = ['a', 'b', 'c', 'd', 'c', 'd']
L = ['', '', '', '', '', '','', '', '', '', '', '']
L = ['a', 'b', 'c', 'd']
print('L =', L)
POWSETS=powerSet(L)
xx=0
TOTAL=[]
TOTALclusters=[]
streetno = {}
for itemx in POWSETS:
    stx='e' + str(xx)
    QA=[itemx,stx, xx,[int(n) for n in bin(xx)[2:].zfill(len(L))]]
    TOTAL.extend(QA)
    print(QA)
    for itemx11 in L:
        if itemx11 in itemx:
            stxq=[[itemx11,stx]]
            TOTALclusters.extend(stxq)
    xx=xx+1
    
for itemx11 in TOTALclusters:
    for itemx22 in L:
        if itemx22 == itemx11[0]:
            print(itemx11)
          
print(TOTALclusters)







    MOST CLEAN

    frame = 0

def powerSet(L):
    global frame
    frame += 1
    if len(L) == 0:
        # print('\nbase case, frame is', frame)
        # print('returning [[]]')
        return [[]]
    else:
        # print('\npre-recursive, frame', frame)
        # print('list in this frame is ', L)
        # print('operator in this frame is ', L[-1:])
        base = powerSet(L[:-1])
        operator = L[-1:]
        frame -= 1
        # print('\npost-recursive, frame', frame)
        # print('base in this frame is', base)
        # print('operated on by', operator)
        r = base + [(b + operator) for b in base]
        # print('returning', r)
        return r

print('global frame is', frame)

L = ['a', 'b', 'c', 'd', 'c', 'd']
L = ['', '', '', '', '', '']
print('L =', L)
POWSETS=powerSet(L)
xx=0
TOTAL=[]
for itemx in POWSETS:
    stx='e' + str(xx)
    QA=[itemx,stx, xx,[int(n) for n in bin(xx)[2:].zfill(len(L))]]
    TOTAL.extend(QA)
    print(QA)
    xx=xx+1