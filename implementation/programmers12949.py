def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    a=[]
    b=[]
    for i in range(len(arr1)):
        a=arr1[i]
        for j in range(len(arr2[0])):
            for k in range(len(arr2)):
                b.append(arr2[k][j])
            for x in range(len(a)):
                answer[i][j]+=(a[x]*b[x])
            b=[]
        
    return answer