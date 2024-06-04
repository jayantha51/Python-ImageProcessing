def main():
    # source https://www.google.com/search?client=safari&rls=en&q=optics+analysis+program+with+python+example&ie=UTF-8&oe=UTF-8#fpstate=ive&ip=1&vld=cid:4b5eef31,vid:o2y5igJvSRI,st:0
    l1 = [1, 2,"Lens"]
    print (l1)
    l2 = [l1, "Focus"]
    lx = ["test"]
    print(l2)
    tl3 = l1 + l2
    print(tl3)
    l4 = l1 + lx
    print(l4)
    print((l1+lx)[1])
    l4.append(10)
    print (l4)




if __name__ == '__main__':
    main()