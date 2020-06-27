from distutils.core import setup

setup(
    name            = 'nester',
    version         ='1.3.0',
    py_modules      =['nester'],
    author          ='zenon',
    author_email    = 'zenon.kiter@gmail.com',
    description     ='Contains one function to print content of list that may or may not contain nested lists.\
                        It takes 3 arguments. 1st argument is the list and is mandatory. Next two args are\
                        optional. Arg 2 defines if content of nested list is to be indented. Arg 3 defines level\
                        of indentation and is set authomaticaly using recursion',
    )
