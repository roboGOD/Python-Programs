def formingMagicSquare(s):
    m1 = [[8,3,4],[1,5,9],[6,7,2]]
    m2 = [[4,9,2],[3,5,7],[8,1,6]]
    m3 = [[2,7,6],[9,5,1],[4,3,8]]
    m4 = [[6,1,8],[7,5,3],[2,9,4]]
    
    c1,c2,c3,c4 = 0,0,0,0
    
    for i in range(3):
        for j in range(3):
            c1 += abs(m1[i][j] - s[i][j])
            c2 += abs(m2[i][j] - s[i][j])
            c3 += abs(m3[i][j] - s[i][j])
            c4 += abs(m4[i][j] - s[i][j])

    if c1 < c2:
        if c1 < c3:
            if c1 < c4:
                return c1
            else:
                return c4
        else:
            if c3 < c4:
                return c3
            else:
                return c4
    else:
        if c2 < c3:
            if c2 < c4:
                return c2
            else:
                return c4
        else:
            if c3 < c4:
                return c3
            else:
                return c4

if __name__ == '__main__':

    s = []

    for _ in xrange(3):
        s.append(map(int, raw_input().rstrip().split()))

    result = formingMagicSquare(s)
    print result