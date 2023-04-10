import sys
import os
import copy
from tempfile import TemporaryDirectory
sys.path.append(f"{__file__}/../..")
import gs_encrypt as encrypter

# in some test:
d = TemporaryDirectory()
temp_file_name = os.path.join(d.name, 'name.txt')
with open(temp_file_name, "w") as t:
    t.write("abc")
    
def test_encrypt_file():
    '''basic tests for encrypting a file
    '''
    data = "12345"
    password = 12345
    raw_data = str.encode(data)
    raw_data = bytearray(raw_data)
    assert encrypter.gs_encrypt_file(password, raw_data).decode() != "12345"
def test_decrypt_file():
    '''basic tests for encrypting a file
    '''
    data = "12345"
    password = 12345
    raw_data = str.encode(data)
    raw_data = bytearray(raw_data)
    assert encrypter.gs_encrypt_file(raw_data, 0, "r").decode() != "12345"