def greet(fx):
    def mfx(*args , **kwargs):
        print ("good morning")
        fx(*args , **kwargs)
        print("thanks for using program")

    return mfx


@greet
def add(a ,b):
    print(a+b)  

# @greet(add)(3,4)      
add(3 , 5)