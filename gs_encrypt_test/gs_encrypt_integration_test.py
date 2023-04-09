import sys
import os
import copy
from tempfile import TemporaryDirectory
sys.path.append(f"{__file__}/../..")
import gs_encrypt as encrypter

# in some test:
d = TemporaryDirectory()
temp_file_name = os.path.join(d.name, 'name.txt')
with open(temp_file_name) as t:
    t.write("abc")