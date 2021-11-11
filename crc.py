import struct
import sys

val1 = "10100100101010001111010110011010"
val2 = "10011"


if (len(sys.argv) > 1):
    val1 = str(sys.argv[1])

if (len(sys.argv) > 2):
    val2 = str(sys.argv[2])


def showpoly(a):
    str1 = ""
    nobits = len(a)

    for x in range(0, nobits-2):
        if (a[x] == '1'):
            if (len(str1) == 0):
                str1 += "x**"+str(nobits-x-1)
            else:
                str1 += "+x**"+str(nobits-x-1)

    if (a[nobits-2] == '1'):
        if (len(str1) == 0):
            str1 += "x"
        else:
            str1 += "+x"

    if (a[nobits-1] == '1'):
        str1 += "+1"

    print(str1)


def toList(x):
    l = []
    for i in range(0, len(x)):
        l.append(int(x[i]))
    return (l)


def toString(x):
    str1 = ""
    for i in range(0, len(x)):
        str1 += str(x[i])
    return (str1)


def divide(val1, val2):
    a = toList(val1)
    b = toList(val2)
    working = toString(val1)+"\n"

    res = ""
    addspace = ""

    while len(b) <= len(a) and a:
        if a[0] == 1:
            del a[0]
            for j in range(len(b)-1):
                a[j] ^= b[j+1]
            if (len(a) > 0):
                working += addspace+toString(b)+"\n"
                working += addspace+"-" * (len(b))+"\n"
                addspace += " "
                working += addspace+toString(a)+"\n"
                res += "1"

        else:
            del a[0]
            working += addspace+"0" * (len(b))+"\n"
            working += addspace+"-" * (len(b))+"\n"
            addspace += " "
            working += addspace+toString(a)+"\n"

            res += "0"

    print("Result is\t", res)
    print("Remainder is\t", toString(a))

    print("Working is\t\n\n", res.rjust(len(val1)), "\n",)
    print("-" * (len(val1)), "\n", working)

    return toString(a)


print("Binary form:\t", val1, " divided by ", val2)
print("")
showpoly(val1)
showpoly(val2)

strzeros = ""
strzeros = strzeros.zfill(len(val2)-1)
val3 = val1+strzeros

print("")
print("Binary form (added zeros):\t", val3, " divided by ", val2)

res = divide(val3, val2)
print("Transmitted value is:\t", val1+res)
