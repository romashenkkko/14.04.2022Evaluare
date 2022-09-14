def EvalElem():
    n = int(input("Introdu numarul de elemente: "))
    list = []
    for i in range(n):
        elem = eval(input("Elementul " + str(i) + " este:"))
        if type(elem) is int:
            list.append(int(elem))
        else:
            print("Nu e nm intreg")
    return list


lista1 = EvalElem()
print(lista1)
