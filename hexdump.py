# Author: Robert Cacho
# Purpose: Library to ease file to hex manipulation
# Library: hexdump.py
import binascii
import tkinter
from tkinter import filedialog
import os


class HexDump:
    def __init__(self, file: str = None):
        self.file = file
        self.hexdump = None

    @staticmethod
    def splitAt(word: str, n: int):
        for i in range(0, len(word), n):
            yield word[i:i+n]

    def getFile(self):
        root = tkinter.Tk()
        root.withdraw()
        currdir = os.getcwd()
        file = filedialog.askopenfile(
            parent=root, initialdir=currdir, title='Please select a File')
        self.file = file.name if file else None

    def storeHex(self, file: str = None):
        file = file or self.file
        if file:
            with open(file, 'rb') as f:
                self.hexdump = binascii.hexlify(f.read())

    def dump(self, file: str = None):
        file = file or self.file
        if file:
            print("File Dump: {}".format(file))
            with open(file, 'rb') as f:
                for chunk in iter(lambda: f.read(32), b''):
                    x = binascii.hexlify(chunk)
                    print(" ".join(HexDump.splitAt(str(x.decode('utf-8')), 2)))


if __name__ == '__main__':
    # file = input("Enter File: ")
    file_dump = HexDump()
    file_dump.getFile()
    file_dump.dump()
    # file_dump.storeHex()
    # print(file_dump.hexdump)
