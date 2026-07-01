# %%
def fun():
    global x
    x=x+1
    print("[fun scope]\t x value: ",x,"x ref: ", hex(id(x)))

x=10

# %%
print("Before call [global scope]\t x value",x,"x ref: ", hex(id(x)))

# %%
fun()
print("After call [global scope]\t x value: ", x, "x ref: ", hex(id(x)))


