def bresenham(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    aux = 2 * dy - dx
    aux2 = 2* dy

    yx2 = 2 * (dy - dx)

    if x1 > x2:
        x = x2
        y = y2
        xf = x1
    else:
        x = x1
        y = y1
        xf = x2

    print('(' + str(x) + ',' + str(y) + ')')

    while x < xf:
        x += 1
        if aux < 0:
            aux += aux2
        else:
            y += 1
            aux += yx2
        print('(' + str(x) + ',' + str(y) + ')')


if __name__ == '__main__':
    x1 = 1
    y1 = 1
    x2 = 8
    y2 = 5
    bresenham(x1, y1, x2, y2)
