# Statistics Formulas:
# Mean = sum of items/ no.of items
l = [1,2,3,4,5,6,7,8]
x = sum(l)       # Sum = sum of items
y = len(l)      # len = no. of items
mean = x / y 
print(mean)

# Median =  number of items divided by 2 in the list, if even n+1 /2 , if it odd n/2, n is no.of items
l = [1,2,3,4,5,6,7,8]
median = (len(l)+1)/ 2
print(median)
# Mode = most frequent number in data
from collections import Counter
def mode(sample):
    c = Counter(sample)
    return [k for k, v in c.items() if v==c.most_common(1)[0][1]]
mode([4,1,2,2,3,5])

# Variance & Standard Deviation
list = [1,2,4,6,7,8,9]
avg = sum(list)/len(list)
var = sum((x-avg)**2 for x in list) / len(list)
print(var)                 # var-Variance

stad = var**0.5            # Stad - Standard deviation
print(stad)        

