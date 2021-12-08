def insertsort(inl):
    for i in range(0,len(inl)):
        for j in range(i,0,-1):
            if (inl[j]<=inl[i] or j==0) and inl[j+1]>=inl[i]:
                inl.insert(j,inl[i])
                inl.pop(i+1)
                break
    return inl

inl=[58,28,4020,9,28,114514,88]
print(insertsort(inl))
