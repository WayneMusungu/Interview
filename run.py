A = [25,2,3,57,38,41]
b = []
number = {
  '0': 0,
  '1': 0,
  '2': 0,
  '3': 0,
  '4': 0,
  '5': 0,
  '6': 0,
  '7': 0,
  '8': 0,
  '9': 0
}

results = []

def getMax(arr):
  max  = 0
  for i in arr:
    if (max > i):
      max = i
  return max
  
    
def sol(a):
  for e in A:
    if e > 10:
      x = int(e/10)
  
      b.append(x)
      y = int(e%10)
  
      b.append(y)
    else:
      b.append(e)

  max = getMax(a) 
  for ele in b: 
   
    if (number[ele] == ele):
      number[ele] += 1

  # Loop through object and get keys with max val
  for k, v in number:
    if v == max:
      results.append(k)
      
    results.sort()      
  return results


sol(A)
        
print(number.keys())