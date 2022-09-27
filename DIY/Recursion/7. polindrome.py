s=input("Enter a Polindrome: ")
i=0
n=len(s)
def is_polindrome(i, s):
    if i>=n-i-1:
        return True

    if s[i] != s[n-i-1]:
        return False

    return is_polindrome(i+1, s)

print(is_polindrome(i,s))