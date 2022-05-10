import typing
import Compilator.folders as fold
import argparse
from Compilator.state import State

import sys
from pprint import pprint
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-c', dest='compile', action='count', default=0)
#    parser.add_argument('-p', dest='populate', action='count', default=0)
    parser.add_argument('-d', dest='dry_run', action='count', default=0)
    parser.add_argument('-f', dest='force', action='count', default=0)
    parser.add_argument('--info', dest='category', action='append')
    args = vars(parser.parse_args())
    State.dry_run = args['dry_run']
    State.force = args['force']

    if args.get('category') and len(args['category']) > 0:
        for i in args['category']:
            pprint(get_category_info(i))
        sys.exit(0)        

    if args['compile'] == 1:
        fold.compile()
#    if args['populate'] == 1:
#        fold.populate_fields()

