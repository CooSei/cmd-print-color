#-*- coding:utf-8 -*-#

#filename: prt_cmd_color.py

import ctypes,sys
STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12
#字体颜色定义 text colors
f_black = 0x00 # black.
f_darkblue = 0x01 # dark blue.
f_darkgreen = 0x02 # dark green.
f_darkskyblue = 0x03 # dark skyblue.
f_darkred = 0x04 # dark red.
f_darkpink = 0x05 # dark pink.
f_darkyellow = 0x06 # dark yellow.
f_darkwhite = 0x07 # dark white.
f_darkgray = 0x08 # dark gray.
f_blue = 0x09 # blue.
f_green = 0x0a # green.
f_skyblue = 0x0b # skyblue.
f_red = 0x0c # red.
f_pink = 0x0d # pink.
f_yellow = 0x0e # yellow.
f_white = 0x0f # white.

# Windows CMD命令行 背景颜色定义 b colors
b_darkblue = 0x10 # dark blue.
b_darkgreen = 0x20 # dark green.
b_darkskyblue = 0x30 # dark skyblue.
b_darkred = 0x40 # dark red.
b_darkpink = 0x50 # dark pink.
b_darkyellow = 0x60 # dark yellow.
b_darkwhite = 0x70 # dark white.
b_darkgray = 0x80 # dark gray.
b_blue = 0x90 # blue.
b_green = 0xa0 # green.
b_skyblue = 0xb0 # skyblue.
b_red = 0xc0 # red.
b_pink = 0xd0 # pink.
b_yellow = 0xe0 # yellow.
b_white = 0xf0 # white.

# get handle
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

def set_cmd_text_color(color, handle=std_out_handle):
    Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return Bool
#reset white
def resetColor():
    set_cmd_text_color(f_red | f_green | f_blue)
def mprint(write,color):
    set_cmd_text_color(color)
    sys.stdout.write(write)
    resetColor()


if __name__=='__main__':
    mprint('\t\t this is colorful print \t\t\t\n',0xcf)
    for i in range(256):
        w = str(i)+'\n'
        mprint(w,i)
    a = input()
