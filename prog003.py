#####################################################
#                                                   #
#                       PROG 15                     #
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

flag = ['50', '53', '4f', '41', '47', '49', '45', '4c']


for i in flag:
    d += i

print ba.unhexlify(b"{}".format(d))