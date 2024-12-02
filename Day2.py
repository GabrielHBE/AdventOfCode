inp = [[7, 6, 4, 2, 1],
       [1, 2, 7, 8, 9],
       [9, 7, 6, 2, 1],
       [1, 3, 2, 4, 5],
       [8, 6, 4, 4, 1],
       [1, 3, 6, 7, 9]
]

i=1
result=0

for line in inp:
    for i in range(len(line)):
        result = line[i] - line[i-1]
        
        if -2 <= result <= 2:
            print('safe')
        else:
            print('Unsafe')

        print(f'{result}\n')