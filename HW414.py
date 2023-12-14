import sys


def parse_args():
    result = ""
    for arg in sys.argv:
        result = ' '.join(sys.argv[1:])           
        
    return result