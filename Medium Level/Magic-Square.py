def modulous(a):
    if a < 0:
        a = a * -1
    return a

def AnyGreaterStd2(rs, cs, ds):
    n = len(s)
    std = (n*(n**2 + 1))//2
    diff = 0
    if rs > std :
        diff = std - rs
    if cs > std:
        diff = std - cs
    if ds > std:
        diff = std - cs
    if diff == 0:
        return True
    else:
        return diff
    
def AnyGreaterStd1(rs, cs):
    n = len(s)
    std = (n*(n**2 + 1))//2
    diff = 0
    if rs > std :
        diff = std - rs
    if cs > std:
        diff = std - cs
    if diff == 0:
        return True
    else:
        return diff
    
def value(s, row, col):
    col_sum = 0
    row_sum = 0
    for i in range(len(s)):
        col_sum += s[row][i]
        row_sum += s[i][col]
    
    return row_sum, col_sum

def value2(s, row, col):
    col_sum = 0
    row_sum = 0
    dia_sum = 0
    for i in range(len(s)):
        col_sum += s[row][i]
        row_sum += s[i][col]
        dia_sum += s[i][i]
    return row_sum, col_sum, dia_sum

def formingMagicSquare(s):
    n  = len(s)
    std = (n*(n**2 + 1))//2
    cost = 0
    for i in range(len(s)):
        for j in range(len(s)):
            if i != j:
                consider = s[i][j]
                row_sum, col_sum = value(s, i, j)
                if AnyGreaterStd1(row_sum, col_sum) == True:
                    if row_sum == col_sum :
                        row_diff, col_diff  = std - row_sum, std - col_sum
                        if row_sum != std:
                            consider += row_diff
                            cost += modulous(row_diff)
                            s[i][j] = consider
                else:
                    diff = AnyGreaterStd1(row_sum, col_sum)
                    consider += diff
                    cost += modulous(diff)
                    s[i][j] = consider
                    
                s[i][j] = consider
                
            if i == j:
                consider = s[i][j]
                row_sum, col_sum, dia_sum = value2(s, i, j)
                if AnyGreaterStd2(row_sum, col_sum, dia_sum) == True:
                    if row_sum == col_sum == dia_sum:
                        row_diff, col_diff, dia_diff  = std - row_sum, std - col_sum, std - dia_sum
                        if row_sum != std:
                            consider += row_diff
                            cost += modulous(row_diff)
                            s[i][j] = consider
                else:
                    diff = AnyGreaterStd2(row_sum, col_sum, dia_sum)
                    consider += diff
                    cost += modulous(diff)
                    s[i][j] = consider
    print(s)
    return cost
        
    
            
s = [[4, 8, 2],[4, 5, 7],[6, 1, 6]]
print(s)
result = formingMagicSquare(s)
print(result)
