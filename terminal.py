#!/usr/bin/python

import sys

SCREEN_WIDTH = SCREEN_HEIGHT = 10


class Cursor(object):
    def __init__(self):
        self.x = self.y = 0


class Screen(object):
    def __init__(self):
        self._screen = [[" " for j in range(SCREEN_WIDTH)]
                        for i in range(SCREEN_HEIGHT)]
        self._cursor = Cursor()
        self._insert_mode = False

    def __str__(self):
        out = ""
        for i, row in enumerate(self._screen):
            for el in row:
                out += el
            if i != SCREEN_HEIGHT-1:
                out += "\n"
        return out

    def _clear(self):
        self._screen = [[" " for j in range(SCREEN_WIDTH)]
                        for i in range(SCREEN_HEIGHT)]

    def handle_escape_sequence(self, ch):
        if ch == 'c':
            self._clear()
        elif ch == 'h':
            self._cursor.x = self._cursor.y = 0
        elif ch == 'b':
            self._cursor.x = 0
        elif ch == 'd':
            if self._cursor.y < SCREEN_HEIGHT-1:
                self._cursor.y += 1
        elif ch == 'u':
            if self._cursor.y > 0:
                self._cursor.y -= 1
        elif ch == 'l':
            if self._cursor.x > 0:
                self._cursor.x -= 1
        elif ch == 'r':
            if self._cursor.x < SCREEN_WIDTH-1:
                self._cursor.x += 1
        elif ch == 'e':
            for i in range(self._cursor.y, SCREEN_WIDTH):
                self._screen[self._cursor.x][i] = ""
        elif ch == 'i':
            self._insert_mode = True
        elif ch == 'o':
            self._insert_mode = False
        elif ch[0].isdigit():
            assert(len(ch) % 2 == 0)
            pos = ch[-2:]
            self._cursor.x = int(pos[1])
            self._cursor.y = int(pos[0])

    def write(self, ch):
        if not self._insert_mode:
            # owerwrite mode
            self._screen[self._cursor.y][self._cursor.x] = ch
        else:
            # insert mode
            i = self._cursor.x
            while i < SCREEN_WIDTH-1:
                self._screen[self._cursor.y][i+1] =\
                    self._screen[self._cursor.y][i+1]
                i += 1
            self._screen[self._cursor.y][self._cursor.x] = ch

        if self._cursor.x < SCREEN_WIDTH-1:
            self._cursor.x += 1

if __name__ == "__main__":
    screen = Screen()
    escape_digits = ""
    with open(sys.argv[1], 'r') as f:
        for line in f:
            chars = line.strip()
            i = 0
            while i < len(chars):
                if (not chars[i].isdigit()) and escape_digits:
                    screen.handle_escape_sequence(escape_digits)
                    escape_digits = ""
                if chars[i] == '^' and chars[i+1] != '^':
                    if chars[i+1].isdigit():
                        escape_digits += chars[i+1]
                        i += 2
                    else:
                        screen.handle_escape_sequence(chars[i+1])
                        i += 2
                elif chars[i].isdigit() and escape_digits:
                    escape_digits += chars[i]
                    i += 1
                elif (chars[i] == '^' and i < SCREEN_WIDTH-1 and
                        chars[i+1] == '^'):
                    screen.write('^')
                    i += 2
                else:
                    screen.write(chars[i])
                    i += 1
    sys.stdout.write(str(screen))
