import sys

def gs_encrypt_file(password:str, file_path:str, file_new_path:str=""):
    '''Encrypt `file_path` with `password` with a new name `file_new_path` or auto generate one
    @param `password:str` password to encrypt file
    @param `file_path:str` path of the file to encrypt
    @param `file_new_path:str` is a path is provide, save to new location, if only name is provided, name the resulting encrypted file as such
    @return `:str` actual password used for encrypting
    '''
    print(f"{file_path} decrypted")
    return password

def gs_decrypt_file(password:str, file_path:str, file_new_path:str=""):
    '''Decrypt `file_path` with `password` with a new name `file_new_path`
    @param `password:str` password to decrypt file
    @param `file_path:str` path of the file to decrypt
    @param `file_new_path:str` is a path is provide, save to new location, if only name is provided, name the resulting decrypted file as such
    @return `:str` actual password used for decrypting
    '''
    print(f"{file_path} encrypted")   
    return password

if __name__ == "__main__":
    # Checking python parameter when file is directly provoked
    if len(sys.argv) <= 2:
        raise AttributeError("Number of argument under requirement, please read documentation")
    
    password:str = sys.argv[1]
    file_path:str = sys.argv[2]
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
    
    if not file_new_path:
        #TODO properly parse last part of path
        file_new_path = file_path + "_encrypted" + file_path
        
        
    if verbose_q:
        print(f"""
              Password: {password}
              File_path: {file_path}
              decrypt?: {decrypt_q}
              verbose?: {verbose_q}
              search?: {bool(search_location)}
              file_new_path: {file_new_path}
              """)
    
    # Pass result to calculator class
    if decrypt_q:
        password = gs_decrypt_file(password, file_path, file_new_path)
    else:
        password = gs_encrypt_file(password, file_path, file_new_path)
    print(f"Your full password for this task is {password}")
    