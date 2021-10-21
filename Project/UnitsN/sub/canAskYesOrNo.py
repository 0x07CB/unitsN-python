#!/usr/bin/python3
#coding: utf-8
#required (internal) library
from copy import deepcopy
# 10/09/2021
# ~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~
# Hello, everyones ! I'm Rick D-634 , AKA  0x07CB... ..And...
# Today I have write an Yes or No questions asking function !
# ~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~
#                                                                                 EN     FR    DE   ES            EN     FR    DE    ES 
def YesOrNoQuestion( asked_question="Confirmation{YN_default_choice}",yes_words=["yes","oui","ja","sí"],no_words=["no","non","nein","no"],
                     YN_default_choice="yes", ask_loop_if_unknow_reply=True, case_sensitive=False, selected_index_reply_lists=None,
                     no_input_is_default_validation=True, upper_case_forced_wanted_reply = False, full_type_forced_wanted_reply = False
                   ): # Yeah that can be use for any languages ! Enjoy !
    O_YN_default_choice = deepcopy(YN_default_choice)
    yes_char, no_char = O_YN_default_choice[0], no_words[yes_words.index(O_YN_default_choice)][0]
    while True:
        if selected_index_reply_lists != None:
            if (-1 < selected_index_reply_lists < len(yes_words)) and (-1 < selected_index_reply_lists < len(no_words)):
                if not full_type_forced_wanted_reply:
                    yes_char = yes_char[selected_index_reply_lists][0]
                    no_char = no_char[selected_index_reply_lists][0]
        if YN_default_choice == "yes":
            yes_char = yes_char.upper()
            no_char = no_char.lower()
        elif YN_default_choice == "no":
            yes_char = yes_char.lower()
            no_char = no_char.upper()
        #
        YN_default_choice = "({yes_char}/{no_char})?".format( yes_char = yes_char, no_char = no_char )
        ask_msg = asked_question.format(YN_default_choice=YN_default_choice)
        reply = input(ask_msg)
        if (no_input_is_default_validation) and (len(reply)==0): 
            if (O_YN_default_choice.lower() == "yes"):
                reply = True
            elif (O_YN_default_choice.lower() == "no"):
                reply = False
            else:
                reply = None
            break
        #
        if not case_sensitive:
            reply = reply.lower()
            YN_default_choice = YN_default_choice.lower()
        #
        elif case_sensitive:
            if upper_case_forced_wanted_reply:
                yes_words = [i.upper() for i in yes_words]
                no_words = [i.upper() for i in no_words]
                YN_default_choice = YN_default_choice.upper()
            if (selected_index_reply_lists != None):
                if (-1 < selected_index_reply_lists < len(yes_words)) and (-1 < selected_index_reply_lists < len(no_words)):
                    yes_words, no_words = list( yes_words[selected_index_reply_lists] ), list( no_words[selected_index_reply_lists] )
        if full_type_forced_wanted_reply:
            for w in yes_words:
                if w == reply:
                    return True
            for w in no_words:
                if w == reply:
                    return False
        if not full_type_forced_wanted_reply:
            for w in yes_words:
                if reply in w[0:len(reply)]:
                    return True
            for w in no_words:
                if reply in w[0:len(reply)]:
                    return False
        else:
            if not ask_loop_if_unknow_reply: 
                reply = None 
                break
    return reply