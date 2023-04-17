import sys
import os
import copy
import random # random password generation
import secrets

'''
TODO: mode for array manipulation versus return new array
TODO: consider collecting like function and place in separate file (maybe as a function)
'''

def gs_encrypt_file(password:str, file_path:str, file_new_path:str="")->str:
    '''Encrypt `file_path` with `password` with a new name `file_new_path` or auto generate one
    @param `password:str` password to encrypt file
    @param `file_path:str` path of the file to encrypt
    @param `file_new_path:str` is a path is provide, save to new location, if only name is provided, name the resulting encrypted file as such
    @return `:str` actual password used for encrypting
    '''
    with open(file_path, "rb") as f_original:
        data = f_original.read()
    #WIP
    #print (data)
    print (bytes(data)[0:10])
    print(f"{file_path} encrypted")
    #sys.stdout.buffer.write(bytes(data))
    encrypted_data = gs_encrypt_data(password, data)
    with open(file_new_path, "wb") as f_encrypted:
        f_encrypted.write(encrypted_data[0])
    return encrypted_data[1]

def gs_decrypt_file(password:str, file_path:str, file_new_path:str="")->str:
    '''Decrypt `file_path` with `password` with a new name `file_new_path`
    @param `password:str` password to decrypt file
    @param `file_path:str` path of the file to decrypt
    @param `file_new_path:str` is a path is provide, save to new location, if only name is provided, name the resulting decrypted file as such
    @return `:str` actual password used for decrypting
    '''
    #WIP
    print(f"{file_path} decrypted")   
    return password

def gs_encrypt_data(password:str, data)->tuple:
    '''Encrypt `file_path` with `password` with a new name `file_new_path` or auto generate one
    @param `password:str` password to encrypt file
    @param `data:bytes or bytearray` (or any type that can be converted to bytes) data to be encrypted ()
    @return `:tuple of (bytes, str)` encrypted data and actual password used for decrypting
    '''
    #WIP
    data = _shift_data_location(data, 1, "r")
    return (data, password)

def gs_decrypt_data(password:str, data:bytes)->tuple:
    '''Decrypt `file_path` with `password` with a new name `file_new_path`
    @param `password:str` password to decrypt file
    @param `data:bytes or bytearray` data to be decrypted
    @return `:tuple of (bytes, str)` decrypted data and actual password used for decrypting
    '''  
    #WIP
    return (data, password)

def _shift_data_location(data:bytearray, shift_count:int, direction:str)->bytearray:
    ''' Shift hex location left or right with wrapping
    '''
    '''
    TODO: if shift count is over a cycle, handle properly
    '''
    data = copy.deepcopy(data)
    if direction.lower() == "r":
        last_bytes = data[-shift_count:]
        output_bytes = bytearray()
        output_bytes.extend(last_bytes)
        output_bytes.extend(data[:-shift_count])
    elif direction.lower() == "l":
        first_bytes = data[:shift_count]
        output_bytes = bytearray()
        output_bytes.extend(data[shift_count:])
        output_bytes.extend(first_bytes)
    else:
        raise Exception("Unknown direction")
    return output_bytes

def _swap_data_location(data:bytearray, index_1:int, index_2:int, swap_length=1)->bytearray:
    ''' Swap the data of size swap_length(bytes) between index_1 and index_2
    '''
    data = copy.deepcopy(data)
    if index_1 < 0 or (index_1+swap_length) >= len(data) or index_2 < 0 or (index_2+swap_length) >= len(data):
        raise Exception("Invalid index")
    
    data[index_1:index_1+swap_length], data[index_2:index_2+swap_length] = data[index_2:index_2+swap_length], data[index_1:index_1+swap_length]
    
    return data

def _invert_data_order(data:bytearray, index_from:int, index_to:int, chunk_size:int=1)->bytearray:
    ''' invert the data from index_from to index_to with chunksize per invert
    
    example: (bytes:"123456", 0, 4, 2) -> (563412)
    '''
    data = copy.deepcopy(data)
    if index_from < 0 or index_from > index_to or index_to > len(data) or chunk_size > (index_to-index_from):
        raise Exception("Invalid index")
    #wip
    return data

def random_unicode_char(max_unicode:int=0x1fbff):
    '''Generate a random unicode char, securely, attempt to remove non-printable chars
    Note this function if not efficient as not all unicode is printable, and such value must be iterated out
    '''
    # 0x10FFFF = Max unicode range
    if max_unicode > 0x10FFFF:
        raise AttributeError("max_unicode exceeded allowed unicode size (<=0x10FFFF)")
    elif max_unicode <= 0:
        raise AttributeError("max_unicode cannot be <= 0")
    
    # iterate until a char that can be printed is generated
    while True:
        random_value = secrets.randbelow(max_unicode + 1) # above 0
        char = chr(random_value)
        if char.isprintable():
            return char

if __name__ == "__main__":
    ''' Command line request format
    path_to_this_file  password    file_path     [options]
    password can be any string, if random password is desired, pass in -r at password location
    '''
    # Checking python parameter when file is directly provoked
    if len(sys.argv) <= 2:
        raise AttributeError("Number of argument under requirement, please read documentation")
    password:str = sys.argv[1]
    if password == "-r":
        password_length = random.randrange(1, 100)
        password:str = ""
        for index in range (password_length):
            # generate utf-8 bytes
            random_char =  random_unicode_char()
            password += random_char
        print(password)
    file_path:str = os.path.realpath(sys.argv[2])
    # commandline option tracking
    pass_count:int = 0
    options:str = sys.argv[3:]
    
    # default value
    decrypt_q:bool = False
    verbose_q:bool = False
    search_location:str = "."
    file_new_path:str = "" # given default value XXX_encrypted.XXX later
    for i, option in enumerate(options):
        if pass_count > 0:
            pass_count -= 1
            continue
        # decrypt option
        if "-d" in option:
            decrypt_q = True
        # verbose?
        elif "-v" in option:
            verbose_q = True
        # new name?
        elif "-s" in option:
            if "-" not in options[i + 1]:
                pass_count += 1
                search_location = options[i + 1]
            # TODO file = search(file, search_location)
        # new name?
        elif "-n" in option:
            if "-" not in options[i + 1]:
                pass_count += 1
                file_new_path = options[i + 1]
            else:
                raise AttributeError("No name provided after -n")
        else:
            raise AttributeError(f"Unknown option {option}")
    
    # init default file_new_path if -n option not set
    if not file_new_path:
        # user provided nothing: auto generate new path
        file_new_path_pre = os.path.dirname(file_path) + "\\" + os.path.basename(file_path).split(".")[0]
        file_new_path_type = "." + os.path.basename(file_path).split(".")[1] 
        file_new_path =  f"{file_new_path_pre}_encrypted{file_new_path_type}"
        base_index = 1
        # While file exist, keep adding index to base name until the file name cannot be found at destination
        while os.path.exists(file_new_path):
            file_new_path = f"{file_new_path_pre}_encrypted_{base_index}{file_new_path_type}"
            base_index += 1
    elif ":\\" not in file_new_path:
        # if user provided only name: add to same location as source file
        file_new_path_pre = os.path.dirname(file_path) + "\\"
        file_new_path_type = "." + os.path.basename(file_path).split(".")[1] 
        file_new_path =  f"{file_new_path_pre}{file_new_path}{file_new_path_type}"
        # if user provided path already have a file, error out here
        if os.path.exists(file_new_path):
            raise AttributeError(f"Save path already have file named {file_new_path}")
    else:
        # if user provided path already have a file, error out here
        file_new_path = os.path.realpath(file_new_path)
        if os.path.exists(file_new_path):
            raise AttributeError(f"Save path already have file named {file_new_path}")
        
    if verbose_q:
        print(f"""
-------------Parameters------------------
Password: {password}
file_path: {file_path}
decrypt?: {decrypt_q}
verbose?: {verbose_q}
file_new_path: {file_new_path}
---------------------------------------
              """)
    
    # start encrypt or decryption
    if decrypt_q:
        password = gs_decrypt_file(password, file_path, file_new_path)
    else:
        password = gs_encrypt_file(password, file_path, file_new_path)
    print(f"Your full password for this task is {password}")
    