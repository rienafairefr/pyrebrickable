import os

from patch_swagger import generate_swagger


def main():
    generate_swagger()
    os.system('./generate_api.sh')


if __name__ == '__main__':
    main()