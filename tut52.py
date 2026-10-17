def fn (fx,*args):
    return 4+fx(*args)

cube= lambda x : x*x*x
square= lambda x:x*x
avg = lambda x,y: (x+y)/2

print(fn(cube,3))
print(fn(square, 3))
print(fn(avg, 3, 5 ))