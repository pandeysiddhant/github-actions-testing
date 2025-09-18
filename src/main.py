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

def check_prime(num):
    flag = True
    for i in range(2,num-1):
        if num%i == 0:
            flag = False
            return "Not Prime"
    if flag == True:
        return "Prime"
    
def check_string(a):
    vowels = ['a','e','i','o','u']
    string = ""
    longest = ""
    for i in a:
        if i not in vowels:
            string += i
        else:
            if len(string) > len(longest):
                longest = string
            string = ""
    return f"The longest sub-string is: {longest}"