from tombola import Tombola


class Fake(Tombola):
    def pick(self):
        return 13


def main():
    print(Fake)
    f = Fake()


if __name__ == "__main__":
    main()
