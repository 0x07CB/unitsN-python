#!/usr/bin/python3
#coding: utf-8
__VERSION__ = "0.0.0. # NOT READY #"

# unitsN.py
# Author: Rick Sanchez [ D-634 ]

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
parser.add_argument("-u", "--units", type=str,
        help="The Units.(comma-separated)", required=True)

# execute the parsing function and get the object with results of args in input inside...
args = parser.parse_args()

# ACCUMULATION OF UNITS (MAX 2 UNITS)
units = args.units
if "," in units:
    units = units.split(",")
else:
    units = [ "{unit}".format(
            unit = units
            ) ]






# ============= CLASS =============
#
class unitsN(object):
    def __init__(self):
        self.powerOf = 10
        self.strUnitNum = "0"
        # Units data prepared for the computes
        self.unitsLetters = ["","K","M","G","T","P"]
        self.unitsValuePowerOf = [0,3,6,9,12,15]
        # Units data for conversion and compute 





    
    def calcPowerOf(self, x, uPow):
        try:
            return x * ( self.powerOf ** uPow ) 
        except Exception as e:
            print("Exception is : {e}".format(
                e = e
                ))
            exit(-1)


    def callErrorShowFunction(self, TYPE_ERR_DESC, ARG_ERR_NAME=""):
        print("Error: {typeErr} {argName}".format(
            typeErr = TYPE_ERR_DESC,
            argName = ARG_ERR_NAME
            ))
        exit(-1)

# 
# ============ DEFINE VARS FROM ARGS ============
#


uNum = unitsN()

if args.units:
    # just N2U/U2N
    if (len(units) == 1):
        uNum.numToUnits(num,units)

        uNum.unitsToNum(units,num)

    # maybe U2U
    elif (len(units) == 2):
        pass

    # errors managed...
    elif (len(units) > 2):
        uNum.callErrorShowFunction("TOO MANY UNITS ON ARGS:", "'--units'")
    elif (len(units) < 1):
        uNum.callErrorShowFunction("NO ONE UNITS ON ARGS:", "'--units'")
    else:
        uNum.callErrorShowFunction("UNKNOWN ERROR ON ARGS:", "'--units'")


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



