from fractions import Fraction
import numpy as np

def solution(m):
    if len(m) < 2:
        return [1,1]
    r, q = split1(m)
    f = find_f(q)
    fr = np.dot(f, r)
    return convert(fr[0])

def split1(m):
    r, q = [], []
    absorbing = set()
    for row in range(len(m)):
        if sum(m[row]) == 0:
            absorbing.add(row)

    for row in range(len(m)):
        if row not in absorbing:
            total = float(sum(m[row]))
            temp_r, temp_q = [], []
            for col in range(len(m[row])):
                if col in absorbing:
                    temp_r.append(m[row][col]/total)
                else:
                    temp_q.append(m[row][col]/total)
            r.append(temp_r)
            q.append(temp_q)
    return r, q

def find_f(q):
    return np.linalg.inv(np.subtract(np.identity(len(q)), q))

def convert(fr):
    numerators, denominators = [], []
    for num in fr:
        fraction = Fraction(num).limit_denominator()
        numerators.append(fraction.numerator)
        denominators.append(fraction.denominator)
    lcd = 1
    for num in denominators:
        lcd = least_common_multiple(lcd,num)
    for num in range(len(numerators)):
        numerators[num] *= int(lcd/denominators[num])
    numerators.append(lcd)
    return numerators

def least_common_multiple(a,b):
    return a // greatest_common_denominator(a,b) * b

def greatest_common_denominator(a,b):
    while b:
        a, b = b, a % b
    return a
