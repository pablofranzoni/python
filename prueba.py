ant=''
count = 0
str = "aaaabbbcca"
list_elem = list()

ant = str[1:2]
for s in str:
    if ant != s:
        t = (ant, count)
        list_elem.append(t)
        count = 0
        ant = s
    count += 1

t = (ant, count)
list_elem.append(t)
print(tuple(list_elem))    
    
      
