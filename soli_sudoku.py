#unique in list
candidates=['12459','1249','1247','12','29','19','1234','6','8']
print (candidates)
for i in '123456789':
    n=0
    for j in range(len(candidates)):        
        if i in candidates[j]:
            n += 1
            j1 = j
            #print (i,n,candidates[j])
    if n==1 :
        #i1 = i
        candidates[j1]=i
print(candidates)

# double unique
candidates=['29','12459','1247','23','29','139','12345','6','8']
duo = []
for i in range(len(candidates)):
    if len(candidates[i]) == 2:
        #print(i,candidates[i])        
        if candidates[i] in duo:
            #print('duo')
            criter = candidates[i]
        duo.append(candidates[i])
        #print(duo)        
print (candidates)           
for i in range(len(candidates)):
    if candidates[i] != criter:
        #print(candidates[i])
        new = ''
        for j in candidates[i]:
            if j not in criter : new += j
        candidates[i] = new    
print (candidates)    