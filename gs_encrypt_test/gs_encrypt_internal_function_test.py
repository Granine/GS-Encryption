import sys
import copy
sys.path.append(f"{__file__}/../..")
import gs_encrypt as encrypter

''' Information:
Note for data in each test is hard coded as translated results are hand calculated
One should not fetch data other ways (like fixture) as it will cause calculated correct solution be to off
TODO:
- Test input array is not modified in function
'''
def test_shift_data_location_right():
    '''basic tests for _shift_data_location for shifting right
    '''
    data = "12345"
    raw_data = str.encode(data)
    raw_data = bytearray(raw_data)
    assert encrypter._shift_data_location(raw_data, 0, "r").decode() == "12345"
    assert encrypter._shift_data_location(raw_data, 1, "r").decode() == "51234"
    assert encrypter._shift_data_location(raw_data, 5, "r").decode() == "12345"
    assert encrypter._shift_data_location(raw_data, 6, "r").decode() == "51234"
    
def test_shift_data_location_left():
    '''basic tests for _shift_data_location for shifting left
    '''
    data = "12345"
    raw_data = str.encode(data)
    assert encrypter._shift_data_location(raw_data, 0, "l").decode() == "12345"
    assert encrypter._shift_data_location(raw_data, 3, "l").decode() == "45123"
    assert encrypter._shift_data_location(raw_data, 5, "l").decode() == "12345"
    assert encrypter._shift_data_location(raw_data, 6, "r").decode() == "23451"
    
def test_swap_data_location():
    '''basic tests for _swap_data_location
    WIP:
    need to test size above limit
    need to test fail case (index out of bound)
    need to test case where wrapping happen
    need to test where swap location overlapped (12345)swap 0, 2, 3
    '''
    data = "12345"
    raw_data = str.encode(data)
    raw_data = bytearray(raw_data)
    assert encrypter._swap_data_location(raw_data, 0, 0).decode() == "12345"
    assert encrypter._swap_data_location(raw_data, 0, 3, 0).decode() == "12345"
    assert encrypter._swap_data_location(raw_data, 0, 1).decode() == "21345"
    assert encrypter._swap_data_location(raw_data, 1, 0).decode() == "21345"
    assert encrypter._swap_data_location(raw_data, 0, 2, 2).decode() == "34125"
    