from even import Even
from prime import Prime


def main():
    e = Prime(1, 30)
    for item in e:
        print(item)


if __name__ == '__main__':
    main()
