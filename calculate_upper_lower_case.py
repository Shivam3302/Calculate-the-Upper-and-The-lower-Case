# sample= 'The quick Brow Fox'
string= str(input("enter the string : "))
def count_lower_upper(n):
    lower=0
    upper=0
    for i in n:
        if i.islower():
            lower+=1
        elif i.isupper():
            upper+=1
    return (f"The count of lower alphabet is {lower} and upper alphabet is {upper}")
    
print(count_lower_upper(string))
output:
Enter the string: The quick Brow Fox
No. of Upper case characters : 3
No. of Lower case Characters : 12
