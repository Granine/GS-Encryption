import sys
import os
#TODO mode for array manipulation versus return new array
import copy

def gs_encrypt_file(password:str, file_path:str, file_new_path:str=""):
    '''Encrypt `file_path` with `password` with a new name `file_new_path` or auto generate one
    @param `password:str` password to encrypt file
    @param `file_path:str` path of the file to encrypt
    @param `file_new_path:str` is a path is provide, save to new location, if only name is provided, name the resulting encrypted file as such
    @return `:str` actual password used for encrypting
    '''
    with open(file_path, "rb") as f_original:
        data = f_original.read()
    #print (data)
    print (bytes(data)[0:10])
    print(f"{file_path} encrypted")
    #sys.stdout.buffer.write(bytes(data))
    #print(hex(123))
    encrypted_data = gs_encrypt_data(password, data)
    with open(file_new_path, "wb") as f_encrypted:
        f_encrypted.write(encrypted_data[0])
    return encrypted_data[1]

def gs_decrypt_file(password:str, file_path:str, file_new_path:str=""):
    '''Decrypt `file_path` with `password` with a new name `file_new_path`
    @param `password:str` password to decrypt file
    @param `file_path:str` path of the file to decrypt
    @param `file_new_path:str` is a path is provide, save to new location, if only name is provided, name the resulting decrypted file as such
    @return `:str` actual password used for decrypting
    '''
    print(f"{file_path} decrypted")   
    return password

def gs_encrypt_data(password:str, data)->bytes:
    '''Encrypt `file_path` with `password` with a new name `file_new_path` or auto generate one
    @param `password:str` password to encrypt file
    @param `data:bytes` (or any type that can be converted to bytes) data to be encrypted ()
    @return `:tuple of (bytes, str)` encrypted data and actual password used for decrypting
    '''
    data = _shift_data_location(data, 1, "r")
    return (data, password)

def gs_decrypt_data(password:str, data:bytes)->bytes:
    '''Decrypt `file_path` with `password` with a new name `file_new_path`
    @param `password:str` password to decrypt file
    @param `data:bytes` data to be decrypted
    @return `:tuple of (bytes, str)` decrypted data and actual password used for decrypting
    '''  
    return (data, password)

def _shift_data_location(data:bytearray, shift_count:int, direction:str):
    ''' Shift hex location left or right with wrapping
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

def _swap_data_location(data:bytearray, index_1, index_2, swap_length=1):
    data = copy.deepcopy(data)
    if index_1 < 0 or index_1+swap_length >= len(data) or index_2 < 0 or index_2+swap_length >= len(data):
        raise Exception("Invalid index")
    print(str(data[index_2:index_2+swap_length])+ "="+str( data[index_1:index_1+swap_length]))
    data[index_1:index_1+swap_length], data[index_2:index_2+swap_length] = data[index_2:index_2+swap_length], data[index_1:index_1+swap_length]
    return data


if __name__ == "__main__":
    # Checking python parameter when file is directly provoked
    if len(sys.argv) <= 2:
        raise AttributeError("Number of argument under requirement, please read documentation")
    
    password:str = sys.argv[1]
    file_path:str = os.path.realpath(sys.argv[2])
    # TODO check path exsist
    # option tracking
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
    
    # normalize file new path
    if not file_new_path:
        # auto generate new path
        file_new_path_pre = os.path.dirname(file_path) + "\\" + os.path.basename(file_path).split(".")[0]
        file_new_path_type = "." + os.path.basename(file_path).split(".")[1] 
        file_new_path =  f"{file_new_path_pre}_encrypted{file_new_path_type}"
        base_index = 1
        while os.path.exists(file_new_path):
            file_new_path = f"{file_new_path_pre}_encrypted_{base_index}{file_new_path_type}"
            base_index += 1
    elif ":\\" not in file_new_path:
        # if user provided only name
        file_new_path_pre = os.path.dirname(file_path) + "\\"
        file_new_path_type = "." + os.path.basename(file_path).split(".")[1] 
        file_new_path =  f"{file_new_path_pre}{file_new_path}{file_new_path_type}"
        if os.path.exists(file_new_path):
            raise AttributeError(f"Save path already have file named {file_new_path}")
    else:
        # if user provided relative path, if bad path will error out here
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
    
    # Pass result to calculator class
    if decrypt_q:
        password = gs_decrypt_file(password, file_path, file_new_path)
    else:
        password = gs_encrypt_file(password, file_path, file_new_path)
    print(f"Your full password for this task is {password}")
    