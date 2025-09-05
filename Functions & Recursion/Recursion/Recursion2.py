#Recursion

#When a fucntion call itself repeatedly.

def val(n):
    if n== 0: #Base Case.
        return
    print(n, end=" ")
    val(n-1)

val(10)