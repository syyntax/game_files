#####################################################
#                                                   #
#                       PROG 25                     #
#               Written by Jason Scott              #
#               jason.scott@mcpa-stl.org            #
#                                                   #
#                 Cyber Patriot 2016                #
#                                                   #
#              Composed in Python 2.7.12            #
#                   PEP 8 Compliant                 #
#                                                   #
#####################################################

import hashlib as ha

prog_string = '''The choral resigns a closure within a
ruling inhabitant. The life overflows the
fantastic advantage over the seventh. Beneath
the proved lemon shines the constraining
hypothesis. An atmospheric inverse acquires
a sound doubt. The generator dismisses the
base bench. How can the vendor serve the
elitist?'''

my_dict = {'a': '4', 'e': '3', 'l': '1', 'o': '0', 's': '5', 't': '7'}


def convert(my_string):
    # ENTER YOUR CODE HERE; DO NOT DELETE OR MOVE THE CODE THAT HAS ALREADY BEEN WRITTEN


m = ha.sha1()
m.update(convert(prog_string))

print("FLAG:  {}".format(m.hexdigest()))
