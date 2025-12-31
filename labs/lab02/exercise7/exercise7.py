def check_collision(x1, y1, w1, h1, x2, y2, w2, h2):
    if x1 < x2 + w2 and x1 + w1 > x2 and y1 < h2 + y2 and h1 + y1 > y2 :
        return True
    else:
        return False
