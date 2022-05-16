import typing
import Compilator.folders as fold
import argparse
from Compilator.state import State

import sys
from pprint import pprint
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Tool for compilation of .c.yaml data')
    parser.add_argument('-c', dest='compile', action='count', default=0, help='Compile data')
#    parser.add_argument('-p', dest='populate', action='count', default=0)
    parser.add_argument('-d', dest='dry', action='count', default=0, help='Validate data')
    parser.add_argument('-f', dest='force', action='count', default=0, help='Force compilation')
    parser.add_argument('--info', dest='category', action='append', help='Print out information about said category')
    args = vars(parser.parse_args())
    State.dry_run = 0
    State.force = args['force']

    if args.get('category') and len(args['category']) > 0:
        for i in args['category']:
            pprint(get_category_info(i))
    elif args['compile'] == 1:
        fold.compile()
    elif args['dry'] == 1:
        fold.dryrun()
#    if args['populate'] == 1:
#        fold.populate_fields()

