

# the formingMagicSquare function below.
def formingMagicSquare(s):
    model = [
         [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
         [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
         [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
         [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
         [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
         [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
         [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
         [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
         ]

    dif=[0,0,0,0,0,0,0,0];
    count=0;
    for m in model:
        for i,j in zip(m,s):
            for k,l in zip(i,j):
                dif[count]+=abs(k-l);
        count+=1;
    return(min(dif))



s = []

for _ in range(3):
    s.append(list(map(int, input().rstrip().split())))

result = formingMagicSquare(s)

print(result)
