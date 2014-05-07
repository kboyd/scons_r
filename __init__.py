# A SCons tool for R scripts
#
# Copyright (c) 2014 Kendrick Boyd. This is free software. See LICENSE
# for details.

import re
import os

import SCons.Action
import SCons.Builder

## TODO - improve these regular expressions
output_re = [
        re.compile(r'''png\('([^']+)'\)''', re.M)
        , re.compile(r'''save\(.*file\s*=\s*'([^']+)'\s*[),]''', re.M)
        , re.compile(r'''sink\(.*file\s*=\s*'([^']+)'\s*[),]''', re.M)
        , re.compile(r'''ggsave\(.*filename\s*=\s*['"]([^'"]+)['"]\s*[),]''', re.M)
        ]

## TODO - improve these regular expressions
source_re = [
        re.compile(r'''source\('([^']+)'\)''', re.M)
        , re.compile(r'''load\(['"]([^'"]+)['"]\)''', re.M)
        , re.compile(r'''read\.table\(['"]([^'"]+)''', re.M)
        ]

def emit_r(target, source, env):
    for s in source:
        print('{0}'.format(str(s)))
        sdir = os.path.dirname(str(s))
        contents = s.get_contents()
        for r in output_re:
            for t in r.findall(contents):
                target.append(os.path.join(sdir, t))
    return target, source


def search_deps_r(node, env):
    contents = node.get_contents()
    deps = []
    for r in source_re:
        for d in r.findall(contents):
            dep_path = os.path.join(os.path.dirname(str(node)), d)
            dep_file = env.File(dep_path)
            deps.append(dep_file)
            deps.extend(search_deps_r(dep_file, env))
    return deps

def scan_r(node, env, path):
    return search_deps_r(node, env)

scanner_r = SCons.Scanner.Base(
    name = 'R Scanner',
    function = scan_r,
    skeys = ['.r', '.R'],
    path_function = SCons.Scanner.FindPathDirs('RPATH'),
    recursive = True)

builder_r = SCons.Builder.Builder(
    action = SCons.Action.Action('$RCOM', chdir=1),
    src_suffix = ['.r','.R'],
    emitter = emit_r,
    source_scanner = scanner_r)


def generate(env):
    env['BUILDERS']['R'] = builder_r
    env['R'] = ['R']
    env['RPATH'] = ['.']
    env['RFLAGS'] = SCons.Util.CLVar('--vanilla')
    env['RCOM'] = '$R $RFLAGS < ${SOURCE.file}'


def exists(env):
    return env.Detect('R')


    
