test = {'name': 'q1',
 'points': 10,
 'suites': [{'cases': [{'code': '>>> put1 = kv()\n'
                                '\n'
                                ">>> get2, put2 = put1('cat', 'animal')\n"
                                '\n'
                                ">>> get3, put3 = put2('table', 'furniture')\n"
                                '\n'
                                ">>> get4, put4 = put3('cup', 'utensil')\n"
                                '\n'
                                ">>> get5, put5 = put4('thesis', 'paper')\n"
                                '\n'
                                ">>> get5('thesis')\n"
                                "'paper'\n"
                                '\n'
                                ">>> get5('cup')\n"
                                "'utensil'\n"
                                '\n'
                                ">>> get5('table')\n"
                                "'furniture'\n"
                                '\n'
                                ">>> get5('cat')\n"
                                "'animal'\n"
                                '\n'
                                ">>> get3('cup')\n"
                                '0\n'}],
             'scored': True,
             'setup': 'from q1 import *',
             'type': 'doctest'}]}