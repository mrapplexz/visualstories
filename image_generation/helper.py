import os
import sys


def import_stuff():
    basedir = os.path.dirname(__file__)
    sys.path.append(f'{basedir}/CLIP')
    sys.path.append(f'{basedir}/pixray')
    sys.path.append(f'{basedir}/diffvg')
    sys.path.append(f'{basedir}/taming-transformers')
