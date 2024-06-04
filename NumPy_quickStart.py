# Reference: https://numpy.org/doc/stable/user/quickstart.html
import numpy as np
from numpy import pi

def main():
    a = np.arange(15).reshape(3, 5)
    print(a)
    print(a.shape) # dimension
    print(a.ndim) # number of axes: axes = dimensions
    print(a.dtype.name)
    print(a.itemsize) # the size in bytes of each element of the array
    print(a.size) #the total number of elements of the array
    print(type(a))
    b = np.array([6.2, 7.21, 8.545])
    print(b)
    print(b.dtype)

    d = np.zeros((3, 4))
    print(d)

    e = np.ones((2, 3, 4))
    print(e)

    f = np.empty((2, 3)) # function empty creates an array whose initial content is random and depends on the state of the memory.
    print("next_____________")
    print(f)
# To create sequences of numbers, NumPy provides the
# arange function which is analogous to the Python built-in range, but returns an array
    g = np.arange(10 ,30, 5)
    print("g", g)
    h = np.arange(0, 2, 0.3)
    print("h", h)

    j = np.linspace(0, 2, 9)
    print("j", j)
    # When arange is used with floating point arguments, it is generally not possible
    # to predict the number of elements obtained, due to the finite floating point precision.
    # For this reason, it is usually better to use the function linspace
    # that receives as an argument the number of elements that we want, instead of the step:
    print("very long array")
    # If an array is too large to be printed, NumPy automatically
    # skips the central part of the array and only prints the corners:
    print(np.arange(10000))
    # To disable this behaviour and force NumPy to print the entire array, you can change
    # the printing options using set_printoptions. (np.set_printoptions(threshold=sys.maxsize))


if __name__ == '__main__':
    main()