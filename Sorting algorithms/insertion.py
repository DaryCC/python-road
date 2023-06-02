def insertion_sort(A):
    for  i in range(1,len(A)):
        print(i)
        for j in range(i-1,0,-1):
            print(j)
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]
            else:
                break

        print(A);


insertion_sort([1,7,4,3]);
