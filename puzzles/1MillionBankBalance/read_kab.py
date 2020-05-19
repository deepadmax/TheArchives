import os
import re

from file_read_backwards import FileReadBackwards

def kab(fname):
    if os.path.exists(fname):
        with FileReadBackwards(fname, encoding="utf-8") as f:
            while True:
                line = f.readline().rstrip()

                if not line:
                    break

                if line.endswith('.'):
                    m = re.match("(\d+)\:(\-?\d+)\,(\-?\d+)\.", line)

                    if m:
                        K, A, B = map(int, m.groups())
                        return K, A, B
    return None