import sys
sys.path.append(f"{__file__}/../..")
import gs_encrypt as encrypter

def test_shift_data_location_right():
    '''basic tests for _shift_data_location for shifting right
    data is hard coded as shifted results are hand calculated
    '''
    data = "12345"
    raw_data = str.encode(data)
    raw_data = bytearray(raw_data)
    assert encrypter._shift_data_location(raw_data, 0, "r").decode() == "12345"
    assert encrypter._shift_data_location(raw_data, 1, "r").decode() == "51234"
    assert encrypter._shift_data_location(raw_data, 5, "r").decode() == "12345"
    
def test_shift_data_location_left():
    '''basic tests for _shift_data_location for shifting left
    data is hard coded as shifted results are hand calculated
    '''
    data = "12345"
    raw_data = str.encode(data)
    assert encrypter._shift_data_location(raw_data, 0, "l").decode() == "12345"
    assert encrypter._shift_data_location(raw_data, 1, "l").decode() == "23451"
    assert encrypter._shift_data_location(raw_data, 5, "l").decode() == "12345"
    
def test_swap_data_location():
    '''basic tests for _swap_data_location for shifting right
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
    assert encrypter._swap_data_location(raw_data, 0, 2, 2).decode() == "34125"
    