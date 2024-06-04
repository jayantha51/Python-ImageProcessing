# Reference: https://numpy.org/doc/stable/user/quickstart.html
# import numpy as np
from numpy import pi
def main():
    x = np.linspace(0, 2, 9)
    print(x)
    y = np.linspace(0, 2 * pi, 100)
    print(y)
    print("Basic operations____________")
    a1 = np.array([20, 30, 40, 50])
    a2 = np.arange(4)
    a3 = a1 - a2
    print(a3)
    print(a2**2) # power two
    print(10*np.sin(a1))
    print(a1 < 35)

    print("let;s check product_____________")
    A1 = np.array([[1, 1],
                   [0, 1]])
    B1 = np.array([[2, 0],
                   [3, 4]])
    print(A1 * B1) # elementwise product
    print(A1 @ B1) # matrix product
    print(A1.dot(B1)) # another matrix product

    rg = np.random.default_rng(1) # create instance of default random number generator
    a = np.ones((2, 3), dtype=int)
    a = np.ones((2, 3), dtype=int)
    b = rg.random((2, 3))
    a *= 3 # modify existing value
    print(a)
    b += a
    print(b)

    a4 = np.ones(3, dtype=np.int32)
    a5 = np.linspace(0, pi, 3)
    c4 = a4 + a5
    print(c4.dtype.name)
    xx = np.exp(c4*1j)
    print(xx)
    print(xx.dtype.name)

    abc = rg.random((2, 3))
    print("abc", abc)
    print(abc.sum())
    print(abc.min())
    print(abc.max())

    print("next__________")
    ff = np.arange(12).reshape(3, 4)
    print(ff)
    print(ff.sum(axis=0)) # sum of each column
    print(ff.min(axis=0)) # min of each column
    print(ff.max(axis=0)) # max of each column



if __name__ == '__main__':
    main()