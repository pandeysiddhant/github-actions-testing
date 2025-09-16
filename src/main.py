def odd_even(num):
    if num%2 == 0:
        return "Even"
    else:
        return "odd"
    
def addition(x,y):
    return x+y

def pallindrome(a):
    if a == a[::-1]:
        return "Pallindrome"
    else:
        return "Not Pallindrome"