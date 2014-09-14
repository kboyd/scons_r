# A SCons tool for R scripts
#
# Copyright (c) 2014 Kendrick Boyd. This is free software. See LICENSE
# for details.

import unittest

from scons_r import *

# Tests of regular expressions for scons_r scanner and output
# detection.

class RegularExpressionTest(unittest.TestCase):
    '''Test regular expressions for scanner and output detection of
    scons_r.
    '''
    
    # TODO test_save1 and test_save2 have identical contents except the
    # last two lines are flipped, and the failure always misses the
    # 5th line ... absolutely no idea why
    def test_save1(self):
        contents = r"""
save(file='main.r',x)
# save(file='commentbefore.r',x)
save(file='commentafter.r',x)# a comment
save(fil='mispell.rdata',x)
save(x, ascii=TRUE, file='args.rdata',precheck=FALSE)
save(file="quoted.rdata",x)
        """
        print(contents)
        expected = ['main.r','commentafter.r','quoted.rdata', 'args.rdata']
        received = findall(contents,output_re)
        print(received)
        self.assertEqual(set(received),set(expected))
        
    def test_save2(self):
        contents = r"""
save(file='main.r',x)
# save(file='commentbefore.r',x)
save(file='commentafter.r',x)# a comment
save(fil='mispell.rdata',x)
save(file="quoted.rdata",x)
save(x, ascii=TRUE, file='args.rdata',precheck=FALSE)
        """
        print(contents)
        expected = ['main.r','commentafter.r','quoted.rdata', 'args.rdata']
        received = findall(contents,output_re)
        print(received)
        self.assertEqual(set(received),set(expected))
        
        
if __name__ == '__main__':
    unittest.main()
