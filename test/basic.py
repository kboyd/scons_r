# A SCons tool for R scripts
#
# Copyright (c) 2014 Kendrick Boyd. This is free software. See LICENSE
# for details.

"""
Basic test of producing output using save.
"""

import TestSCons

test = TestSCons.TestSCons()

# Add scons_r tool to test figure.
test.file_fixture('../__init__.py', 'site_scons/site_tools/scons_r/__init__.py')

test.write(['SConstruct'], """\
import os

env = Environment(TOOLS = ['scons_r'])

env.R('basic.r')
""")

test.write(['basic.r'], """\
x=rnorm(100)
save(x, file='x.rdata')
""")

test.run(arguments='.', stderr=None)

test.must_exist('x.rdata')

test.pass_test()
