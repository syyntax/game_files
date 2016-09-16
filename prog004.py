#####################################################
#                                                   #
#                       PROG 20                     #
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

my_list = []

# ENTER YOUR CODE HERE; DO NOT DELETE OR MOVE THE CODE THAT HAS ALREADY BEEN WRITTEN


m = ha.sha1()
m.update(str(my_list))

print(m.hexdigest())
