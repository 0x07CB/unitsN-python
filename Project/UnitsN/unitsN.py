#!/usr/bin/python3
#coding: utf-8
__VERSION__ = "0.1.0"

# unitsN.py
# Author: Rick Sanchez [ D-634 ]


# THIS CODE IS ... SIMPLE...
# GUIDE (to read fast): 
#
# Library import start here and, arg parsing just after,
# Class after the parsing and function. 
#
# ============ LIB ============
import os, argparse, hashlib, json
#from base64 import b64encode as benc
#from base64 import b64decode as bdec
#from multiprocessing import Process, Pool
#
# ============ VAR ============
unitsAllow = [None,"K","M","G","T","P"]

# ============ ARG ============
parser = argparse.ArgumentParser("unitsN.py is an module to convert easy numerical value into string (with units indication).\nexemple: '40K' , can be out in 40000 ... or in 0.04M ... etc... \nWrite by Rick Sanchez.".format(
    version = __VERSION__
    ))
#
# ===============ARG================
# ============ PARSING =============

parser.add_argument("-s", "--size", type=int, 
        help="size of valid block repetitions")

# execute the parsing function and get the object with results of args in input inside...
args = parser.parse_args()

# ============= CLASS =============
#
class unitsN(object):
    def __init__(self):
        self.strUnitNum = "0"


    def callErrorShowFunction(self, TYPE_ERR_DESC):
        print("Error: {typeErr}".format(
            typeErr = TYPE_ERR_DESC
            ))
        exit(-1)

# 
# ============ DEFINE VARS FROM ARGS ============
#


# ¨¨¨¨¨¨�PROGRAM NOW¨¨¨¨¨¨¨¨¨¨¨¨



