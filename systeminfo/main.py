"""
Created on 28 Jan 2018

@author: philip
"""

import platform
import socket


def main():
    print('Machine name:', platform.uname()[1])
    print('OS name:', platform.uname()[0])
    print('OS version:', platform.uname()[3])
    print('IP address:', socket.gethostbyname(socket.gethostname()))
    return


if __name__ == '__main__':
    main() 