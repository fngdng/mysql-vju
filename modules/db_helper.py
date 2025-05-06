# modules/utils/db_helper.py
import os
import sys

def get_db_path():
    if getattr(sys, 'frozen', False):
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.abspath("DB")
    return os.path.join(base_path, "japanese.db")
