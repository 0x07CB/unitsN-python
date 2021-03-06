#!/usr/bin/python3
#coding: utf-8
__VERSION__ = "0.0.0 # NOT READY #"

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
        self.unitsPowerOfDictByLetters, self.unitsLettersDictByPowerOf = {}, {}
        for x in self.unitsValuePowerOf:
            # Take the index 
            _index = self.unitsValuePowerOf.index(x)
            # Units to Letters
            self.unitsPowerOfDictByLetters[
                    self.unitsLetters[
                        _index
                    ]
                ] = self.calcPowerOf(x, self.powerOf)
            # Letters to units
            self.unitsLettersDictByPowerOf[
                    self.unitsValuePowerOf[
                        _index
                    ]
                ] = _index
    

    def numToUnits(self, num, units):
        return self.calcPowerOf(num,self.unitsPowerOfDictByLetters[units],OP_MOD1="/")

    def unitsToNum(self, units, num):
        return self.calcPowerOf(num,self.unitsPowerOfDictByLetters[units],OP_MOD1="*")


    def whatIsTheUnitOfThisNumber(self, x):
        d = str(x)
        unitsMap = { 
            "": [1,2,3], 
            "K": [4,5,6],
            "M": [7,8,9],
            "G": [10,11,12],
            "T": [13,14,15],
            "P": [16,17,18]
        }
        #
        for k,v in unitsMap.items():
            if len(d) in v:
                return k
        return None 
    
    def calcPowerOf(self, x, uPow, OP_MOD1="*"):
        try:
            if OP_MOD1 == "*":
                return x * ( self.powerOf ** uPow ) 
            elif OP_MOD1 == "/":
                return x / ( self.powerOf ** uPow )
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
        if args.full_numbers_to_unit():
            uNum.numToUnits(num,units)

        if args.unit_to_full_numbers():
            uNum.unitsToNum(units,num)

    # maybe U2U
    elif (len(units) == 2):
        if args.unit_to_unit:
            uNum.unitsToUnits(units1,units2)

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
#         yes_words=["yes","oui","ja","s??"]
#         ,no_words=["no","non","nein","no"],
#         YN_default_choice="yes", 
#         ask_loop_if_unknow_reply=True, 
#         case_sensitive=False, selected_index_reply_lists=None,
#         no_input_is_default_validation=True, upper_case_forced_wanted_reply = False, 
#         full_type_forced_wanted_reply = False



