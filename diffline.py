#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import colorama

RED = '\033[31m'
RESET = '\033[0m'


class LineDiff:
    def __init__(self):
        self._previous_line = ""
        self._previous_line_len = 0
        self.is_color = False

    def _color_set(self, is_color):
        if self.is_color != is_color:
            if is_color is False:
                print(RESET, end="")
            elif is_color is True:
                print(RED, end="")
            self.is_color = is_color

    def _print_with_diff(self, new_line):
        for i in range(len(new_line)):
            if i < self._previous_line_len:
                if new_line[i] == self._previous_line[i]:
                    self._color_set(False)
                else:
                    self._color_set(True)
            else:
                self._color_set(True)

            print(new_line[i], end="")

        self._color_set(False)
        print()

    def feed_line(self, new_line):
        self._print_with_diff(new_line)
        self._previous_line = new_line
        self._previous_line_len = len(new_line)


def main():
    import signal

    # handle Ctrl+C
    def signal_handler(sig, frame):
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    colorama.init()
    differ = LineDiff()

    for line in sys.stdin:
        differ.feed_line(line[:-1])


if __name__ == "__main__":
    main()
