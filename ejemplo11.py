def mayor(h1,h2,h3):
    max = 0
    for x in h1,h2,h3:
        if x> max:
            max=x
    return max

print(mayor(2,3,1))