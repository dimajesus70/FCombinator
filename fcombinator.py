'''
  * Program: FCombinator ;
  * File: fcombinator.py ;
  * Author: F0r3bod1n5 ;
  * Version: v0.1 ;
'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import codecs
import argparse
import colorama

colorama.init()

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", dest = "inputfiles", type = str, required = True, help = "Input files (comma separated).")
parser.add_argument("-o", "--output", dest = "outputfile", type = str, required = True, help = "Output file.")
_args = parser.parse_args()

_inputs = _args.inputfiles.split(",")
fores = colorama.Fore
backs = colorama.Back
styles = colorama.Style

def check_args():
  if len(_inputs) == 1:
    print(fores.RED + "[-] Error, the second input file was not found." + styles.RESET_ALL)
    sys.exit(0)
  main()


def main():
  try:
    inp1 = codecs.open(_inputs[0], "r+", encoding = "cp1251")
    inp2 = codecs.open(_inputs[1], "r+", encoding = "cp1251")
    out = codecs.open(_args.outputfile, "a+", encoding = "cp1251")
  except:
    print(fores.RED + "[-] Unknown error..." + styles.RESET_ALL)
    sys.exit(0)

  lines_arr = []

  for line in inp1.readlines():
    lines_arr.append(line)
    del line

  for line in inp2.readlines():
    lines_arr.append(line)
    del line

  for line in lines_arr:
    out.write(line)
    del line

  print(fores.GREEN + "[+] Done! Files success combinated." + styles.RESET_ALL)

if __name__ == "__main__":
  check_args()