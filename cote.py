n, m = map(int,input().split())
k = int(input())
x = [0]*100
y = [0]*100
x[n] = 1
y[m] = 1
cur_x , cur_y = n,m
vertex_ur = []
vertex_ul = []
vertex_dr = []
vertex_dl = []
before = 'none'
for i in range(k):
    pos, cnt = input().split()
    if pos == 'R':
        if before == 'D':
            vertex_dr.append([cur_x, cur_y])
        elif before == 'U':
            vertex_ur.append([cur_x, cur_y])
        
        before = 'R'
        for go in range(int(cnt)):
            x[cur_x + go + 1] = 1
            if x[cur_x + go + 1] == 1 and y[cur_y] == 1:
                vertex_dl.append([cur_x+go+1, cur_y])
                vertex_dr.append([cur_x+go+1, cur_y])
                vertex_ul.append([cur_x+go+1, cur_y])
                vertex_ur.append([cur_x+go+1, cur_y])
        cur_x = cur_x + int(cnt)
        
    elif pos == 'L':
        
        if before == 'D':
            vertex_dl.append([cur_x, cur_y])
        elif before == 'U':
            vertex_ul.append([cur_x, cur_y])
        
        before = 'L'
        for go in range(int(cnt)):
            x[cur_x - go - 1] = 1
            if x[cur_x - go - 1] == 1 and y[cur_y] == 1:
                vertex_dl.append([cur_x - go - 1, cur_y])
                vertex_dr.append([cur_x - go - 1, cur_y])
                vertex_ul.append([cur_x - go - 1, cur_y])
                vertex_ur.append([cur_x - go - 1, cur_y])
        cur_x = cur_x - int(cnt)
    
    elif pos == 'D':
        if before == 'L':
            vertex_dr.append([cur_x, cur_y])
        elif before == 'R':
            vertex_dl.append([cur_x, cur_y])
        
        before = 'D'
        for go in range(int(cnt)):
            y[cur_y - go - 1] = 1
            if x[cur_x] == 1 and y[cur_y - go - 1]:
                vertex_dl.append([cur_x, cur_y-go-1])
                vertex_dr.append([cur_x, cur_y-go-1])
                vertex_ul.append([cur_x, cur_y-go-1])
                vertex_ur.append([cur_x, cur_y-go-1])
        cur_y = cur_y - int(cnt)
    
    else: # pos == 'U'
        if before == 'L':
            vertex_ur.append([cur_x, cur_y])
        elif before == 'R':
            vertex_ul.append([cur_x, cur_y])
        
        before = 'U'
        for go in range(int(cnt)):
            y[cur_y + go + 1] = 1
            if x[cur_x] == 1 and y[cur_y + go + 1]:
                vertex_dl.append([cur_x, cur_y+go+1])
                vertex_dr.append([cur_x, cur_y+go+1])
                vertex_ul.append([cur_x, cur_y+go+1])
                vertex_ur.append([cur_x, cur_y+go+1])
        cur_y = cur_y + int(cnt)
    print(vertex_dr, vertex_dl, vertex_ul, vertex_ur)
        
