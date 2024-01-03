"""Call this with python -m sql"""
# pylint: disable=import-error
from . import build_db

if __name__ == "__main__":
    build_db(verbose=True)
