from __future__ import print_function
from os import urandom
from binascii import b2a_hex


def main():
    key = b2a_hex(urandom(32))
    print('/key/swarm/psk/1.0.0/')
    print('/base16/')
    print(key)


if __name__ == "__main__":
    main()
