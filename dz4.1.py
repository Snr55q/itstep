
class MyIterator:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        if self.current <= self.n:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration

    def count_down(self):
        def generator():
            for n in range(self.n):
                yield n
            return generator()

    def multiplier(self, n):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            return result
        return wrapper

myiterator = MyIterator(333)
for i in myiterator:
    print(i)

count_down_generator = myiterator.count_down()
for i in count_down_generator:
    print(i)

def ex(x):
    return x * x

ex(161)

multiply_b = myiterator.multiplier(2)
print(multiply_b)


