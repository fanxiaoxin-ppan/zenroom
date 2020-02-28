# -*- coding: utf-8 -*-

import binascii

data = u"55AA08060100024D5E77"
print data

x = binascii.hexlify(data)
print 'x = {}' .format(x)
print type(x)

y = binascii.unhexlify(x)
print 'y = {}' .format(y)

s = "hello"
b = binascii.b2a_hex(s)
print "1 ,b2a_hex --> b = {}" .format(b)
c = binascii.a2b_hex(b)
print "1, a2b_hex --> c = {}" .format(c)

b = binascii.hexlify(s)
print "2, hexlify --> b = {}" .format(b)
c = binascii.unhexlify(b)
print "2, unhexlify --> c = {}" .format(c)