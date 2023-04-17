import numpy as np
# quaternion multiplication
def qmult(x, y):
    return [
    x[0] + "*" +  y[0] +"-"+ x[1] + "*"+ y[1] +"-"+ x[2] +"*"+ y[2] +"-"+ x[3] +"*"+ y[3],
    x[0] + "*" +  y[1] +"+"+ x[1] + "*"+ y[0] +"+"+ x[2] +"*"+ y[3] +"-"+ x[3] +"*"+ y[2],
    x[0] + "*" +  y[2] +"-"+ x[1] + "*"+ y[3] +"+"+ x[2] +"*"+ y[0] +"+"+ x[3] +"*"+ y[1],
    x[0] + "*" +  y[3] +"+"+ x[1] + "*"+ y[2] +"-"+ x[2] +"*"+ y[1] +"+"+ x[3] +"*"+ y[0]]

# quaternion conjugate
def qstar(x):
    return [x[0], "(-1*" +x[1] +")" ,"(-1*" +x[2] +")", "(-1*" +x[3] +")" ]


# octonion multiplication
def omult(x, y):
# Split octonions into pairs of quaternions
    a, b = x[:4], x[4:]
    c, d = y[:4], y[4:]
    X1=qmult(a, c)
    # for i in range(len(X1)):
    #     # print(X1[i])

    X2=qmult(qstar(d), b)
    # for i in range(len(X1)):
    #     # print(X2[i])

    z = ["","","","" ,"","","","" ]
    for i in  [0, 1, 2,3]:
        z[i] = "(" +  X1[i]  +")"  +  "-1*" + "(" + X2[i] + ")"
        # print(z[i])
    X1=qmult(d, a)
    X2=qmult(b, qstar(c))
    for i in [4,5,6,7]:
        z[i] = "(" +  X1[i-4] +")"  + "+1*" +  "("+ X2[i-4] +")"
        # print(z[i])
    return z

def ostar(x):
    return [x[0], "(-1*" +x[1] +")" ,"(-1*" +x[2] +")", "(-1*" +x[3] +")" , "(-1*" +x[4] +")" ,"(-1*" +x[5] +")", "(-1*" +x[6] +")" , "(-1*" +x[7] +")"]
 # sedenion multiplication
def smult(x, y):
# Split sedenions into pairs of octonions
    a, b = x[:8], x[8:]
    c, d = y[:8], y[8:]
    X1=omult(a, c)
    # for i in range(len(X1)):
    #     # print(X1[i])
    X2=omult(ostar(d), b)
    # for i in range(len(X1)):
    #     # print(X2[i])

    z = ["","","","" ,"","","","","","","","" ,"","","","" ]
    for i in  [0, 1, 2,3,4,5,6,7]:
        z[i] = "(" +  X1[i]  +")"  +  "-1*" + "(" + X2[i] + ")"
        # print(z[i])
    X1=omult(d, a)
    X2=omult(b, ostar(c))
    for i in [8,9,10,11,12,13,14,15]:
        z[i] = "(" +  X1[i-8] +")"  + "+1*" +  "("+ X2[ i- 8 ] +")"
        # print(z[i])
    return z


def sstar(x):
    return [x[0], "(-1*" +x[1] +")" ,"(-1*" +x[2] +")", "(-1*" +x[3] +")" , "(-1*" +x[4] +")" ,"(-1*" +x[5] +")", "(-1*" +x[6] +")" , "(-1*" +x[7] +")", "(-1*" +x[8] +")" ,"(-1*" +x[9] +")", "(-1*" +x[10] +")" , "(-1*" +x[11] +")" ,"(-1*" +x[12] +")", "(-1*" +x[13] +")" , "(-1*" +x[14] +")", "(-1*" +x[15] +")"]
 # sedenion multiplication
def tmult(x, y):
# Split sedenions into pairs of octonions
    a, b = x[:16], x[16:]
    c, d = y[:16], y[16:]
    X1=smult(a, c)
    # for i in range(len(X1)):
    #     # print(X1[i])
    X2=smult(sstar(d), b)
    # for i in range(len(X1)):
    #     # print(X2[i])

    z = [ "","","","" ,"","","","","","","","" ,"","","","","","","","" ,"","","","","","","","" ,"","","","" ]
    for i in  [0, 1, 2,3,4,5,6,7,8,9,10,11,12,13,14,15]:
        z[i] = "(" +  X1[i]  +")"  +  "-1*" + "(" + X2[i] + ")"
        # print(z[i])
    X1=smult(d, a)
    X2=smult(b, sstar(c))
    for i in [16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]:
        z[i] = "(" +  X1[i-16] +")"  + "+1*" +  "("+ X2[i-16] +")"
        # print(z[i])
    return z

with open("C:/Users/faysal el khettabi/Documents/GitHub/STRINGHYPERCOMP/RESULTS/DOUBLYCONJUGATEAllhypermultps.txt", 'w') as f:

    a = ['A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7']
    b = ['G0', 'G1', 'G2', 'G3', 'E4', 'E5', 'E6', 'E7']
    cq = omult(a, b)
    a = ['A0', '-A1', '-A2', '-A3', '-A4', '-A5', '-A6', '-A7']
    c = omult(a, cq)
    f.write("OCTOS!")
    f.write("\n")
    for i in range(len(c)):
        f.write(c[i]+","+"\n")
        print(c[i])

    a = ['A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7','A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15']
    b = ['B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7','B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15']
    cq = smult(a, b)
    a = ['A0', '-A1', '-A2', '-A3', '-A4', '-A5', '-A6', '-A7','-A8', '-A9', '-A10', '-A11', '-A12', '-A13', '-A14', '-A15']
    c = smult(a, cq)
    f.write("SEDOS!")
    f.write("\n")
    for i in range(len(c)):
        f.write(c[i]+","+"\n")
        print(c[i])

    a = ['A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7','A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15','A16', 'A17', 'A18', 'A19', 'A20', 'A21', 'A22', 'A23','A24', 'A25', 'A26', 'A27', 'A28', 'A29', 'A30', 'A31']
    b = ['B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7','B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15','B16', 'B17', 'B18', 'B19', 'B20', 'B21', 'B22', 'B23','B24', 'B25', 'B26', 'B27', 'B28', 'B29', 'B30', 'B31']
    cq = tmult(a, b)
    a = ['A0', '-A1', '-A2', '-A3', '-A4', '-A5', '-A6', '-A7','A8', '-A9', '-A10', '-A11', '-A12', '-A13', '-A14', '-A15','A16', '-A17', '-A18', '-A19', '-A20', '-A21', '-A22', '-A23','A24', '-A25', '-A26', '-A27', '-A28', '-A29', '-A30', '-A31']
    cq = tmult(a, cq)
    f.write("TRIGS!")
    f.write("\n")
    for i in range(len(c)):
        f.write(c[i]+","+"\n")
        print(c[i])


f.close()