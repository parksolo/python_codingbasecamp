def one(n):
    def two(value):
        sq = value ** n
        return sq

    return two


a = one(2)
b = one(3)
c = one(4)
print(a(10))
print(b(10))
print(c(10))
