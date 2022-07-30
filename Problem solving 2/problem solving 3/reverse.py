def flip(d, a):
    if d=='R':
        return sorted(a)
    elif d=='L':
        return a.sort()
print(flip('L', [1, 4, 5, 3, 5]))