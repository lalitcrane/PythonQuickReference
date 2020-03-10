

# Reload a package after changes

import imp  #imp is a standard package in python
imp.reload(MyPackage)

or 

import importlib
importlib.reload(MyPackage)


# Print statements
foo = 'foo'
bar = 'bar'

foobar = '%s%s' % (foo, bar) # It is OK
foobar = '{0}{1}'.format(foo, bar) # It is better
foobar = '{foo}{bar}'.format(foo=foo, bar=bar) # It is best

