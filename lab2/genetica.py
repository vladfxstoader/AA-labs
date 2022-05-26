class cromozom:
    def __init__(self, a, b, n):
        self.a = a
        self.b = b
        # self.n = n
        # self.bits = [False for i in range(n)]
        self.p = (b-a)/(2**n)
        self.n = 4
        self.bits = [1, 1, 1, 1]

    def transform(self):
        number = 0
        pow = 1
        for i in range(self.n-1,-1,-1):
            number = number + self.bits[i]*pow
            pow = pow*2
        number = number * self.p
        self.a = self.a + number

crom = cromozom(1,2,3)
print(crom.a)
crom.transform()
print(crom.a)


