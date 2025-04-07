def solution(wallpaper):
    lux, luy, rdx, rdy = 51, 51, 0, 0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                lux = i if i < lux else lux
                luy = j if j < luy else luy
                rdx = i if i > rdx else rdx
                rdy = j if j > rdy else rdy
    
    answer = [lux, luy, rdx+1, rdy+1]
    return answer