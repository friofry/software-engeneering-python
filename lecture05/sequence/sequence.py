import collections.abc

class Foo:
    def __getitem__(self, pos):
        return range(0, 30, 10)[pos]


def main():
    f = Foo()
    print(f[1]) # __getitem__
    for i in f: # __iter__ ?
        print(i)

    print (20 in f)
    print (15 in f) # __contains__  ?


if __name__ == "__main__":
    main()