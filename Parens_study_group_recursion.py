def Parens(n):
    if n < 1:
        return ""
    if n == 1:
        return "()"
    ans = []
    ans.append("()"+Parens(n-1))
    ans.append("("+Parens(n-1)+")")
    if n > 2:
        ans.append(Parens(n-1)+"()")
    return ans
