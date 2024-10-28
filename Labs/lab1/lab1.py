import sys
import math

def get_coef(index, prompt):
    try:
        coef_str = sys.argv[index]
    except:
        print(prompt)
        coef_str = input()
    coef = float(coef_str)
    return coef

def get_roots(a, b, c):
    result = []
    D = b*b - 4*a*c
    if D == 0.0:
        y = -b / (2.0*a)
        result.append(y)
    elif D > 0.0:
        sqD = math.sqrt(D)
        y1 = (-b + sqD) / (2.0*a)
        y2 = (-b - sqD) / (2.0*a)
        result.append(y1)
        result.append(y2)
    Result = []
    for i in range (len(result)):
        if result[i]>=0:
            Result.append(math.sqrt(result[i]))
            Result.append(-math.sqrt(result[i]))
    return Result
def main():
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    roots=get_roots(a,b,c)
    print("Корни: ",roots)
if __name__ == "__main__":
    main()
