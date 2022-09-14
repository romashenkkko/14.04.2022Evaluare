def EvalElem():
    n = int(input("Introdu numarul de elemente: "))
    list = []
    for i in range(n):
        elem = input("Introdu elemente")
        if type(elem) is int:
            list.append(elem)
        else:
            print("Nu e nm intrg")
    return list

lista1 = EvalElem()
print(lista1)
