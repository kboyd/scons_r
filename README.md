scons_r
=======



Description
-----------

[SCons](http://www.scons.org/) tool for
[R](http://www.r-project.org). Automatically identifies .r script
dependencies and outputs for use with SCons build system.


Installation
------------

scons\_r is an external tool for SCons and can most easily be
installed by checking out the scons\_r repository to either

1. /path\_to\_your\_project/site\_scons/site\_tools/scons\_r/, for one
   project only, or   
2. ~/.scons/site\_scons/site\_tools/scons\_r/, for installation for
   all your projects (SCons 2.1 or above).

See [ToolsIndex](http://www.scons.org/wiki/ToolsIndex) for more
details about installing external tools.

If the project is managed with [git](http://git-scm.com/), this can be
accomplished with
[submodules](http://git-scm.com/book/en/Git-Tools-Submodules):

```
git submodule add https://github.com/kboyd/scons_r.git site_scons/site_tools/scons_r
```


Usage
-----

In a `SConstruct` or `SConscript` file, create an environment
including the R tool and process an R script names `input.r` using

```python
env = Environment(tools=['scons_r'])

env.R('input.r')
```


See also
--------
http://www.scons.org/
http://www.scons.org/wiki/ToolsIndex

