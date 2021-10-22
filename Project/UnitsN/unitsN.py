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

parser.add_argument("-U2N", "--unit-to-full-numbers", action="store_true",
        help="Convert an Unit signed number string to complete representation of this number.")
parser.add_argument("-U2U","--unit-to-unit-numbers", action="store_true",
        help="Convert an Unit signed to other Unit numbers")
parser.add_argument("-N2U","--full-to-unit-numbers", action="store_true",
        help="Convert an Number to Unit signed numbers")

parser.add_argument("number", type=str, 
        help="The number.")
parser.add_argument("--units", type=str, metavar="XX",
        help="The Units.", required=True)

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






#reference to remind for construct that...


# YesOrNoQuestion( 
#         asked_question="Confirmation{YN_default_choice}",
#         yes_words=["yes","oui","ja","sí"]
#         ,no_words=["no","non","nein","no"],
#         YN_default_choice="yes", 
#         ask_loop_if_unknow_reply=True, 
#         case_sensitive=False, selected_index_reply_lists=None,
#         no_input_is_default_validation=True, upper_case_forced_wanted_reply = False, 
#         full_type_forced_wanted_reply = False



