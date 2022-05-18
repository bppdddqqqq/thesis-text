import typing
import Compilator.folders as fold
import argparse
from Compilator.state import State
from Compilator.categories import get_category_info

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Tool for compilation of .c.yaml data')
    parser.add_argument('-c', dest='compile', action='count', default=0, help='Compile data')
    parser.add_argument('-d', dest='dry', action='count', default=0, help='Validate data')
    parser.add_argument('-f', dest='force', action='count', default=0, help='Force compilation')
    parser.add_argument('--catalogue', dest='catalogue', action='count', default=0, help='Export device catalogue')
    parser.add_argument('--trans', dest='trans', action='count', default=0, help='Export device transaction method support catalogue')
    parser.add_argument('--info', dest='category', action='append', help='Print out information about said category')
    args = vars(parser.parse_args())
    State.dry_run = 0
    State.force = args['force']

    if args.get('category') and len(args['category']) > 0:
        for i in args['category']:
            print(get_category_info(i))
    elif args['catalogue'] == 1:
        fold.get_device_catalogue()
    elif args['trans'] == 1:
        fold.get_bip_support()
    elif args['compile'] == 1:
        fold.compile()
    elif args['dry'] == 1:
        fold.dryrun()
