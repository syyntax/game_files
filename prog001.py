#####################################################
#                                                   #
#                       PROG 05                     #
#               Written by Jason Scott              #
#               jason.scott@mcpa-stl.org            #
#                                                   #
#                 Cyber Patriot 2016                #
#                                                   #
#              Composed in Python 2.7.12            #
#                   PEP 8 Compliant                 #
#                                                   #
#####################################################

import binascii as ba

flag = ba.unhexlify('507974686f6e20726f636b7321')


def show_flag():
    return flag
