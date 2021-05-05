from collections import abc

class Struggle:
    def __len__(self):
        return 23


def main():
    a = Struggle()
    print(isinstance(a, abc.Sized))


if __name__ == "__main__":
    main()
