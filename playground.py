def funkcja():
    global Zmienna
    Zmienna = 0
    print(Zmienna)
    Zmienna += 1
    print(Zmienna)
    return Zmienna



print(funkcja())

print(Zmienna)