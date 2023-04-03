import sys

def gs_encrypt_file(password:str, file_path:str, file_new_path:str=""):
    '''Encrypt `file_path` with `password` with a new name `file_new_path` or auto generate one
    @param `password:str` password to encrypt file
    @param `file_path:str` path of the file to encrypt
    @param `file_new_path:str` is a path is provide, save to new location, if only name is provided, name the resulting encrypted file as such
    @return `:str` actual password used for encrypting
    '''
    print(f"{file_path} decrypted")

def gs_decrypt_file(password:str, file_path:str, file_new_path:str=""):
    '''Decrypt `file_path` with `password` with a new name `file_new_path`
    @param `password:str` password to decrypt file
    @param `file_path:str` path of the file to decrypt
    @param `file_new_path:str` is a path is provide, save to new location, if only name is provided, name the resulting decrypted file as such
    @return `:str` actual password used for decrypting
    '''
    print(f"{file_path} encrypt")   

if __name__ == "__main__":
    # Checking python parameter when file is directly provoked
    if len(sys.argv) <= 2:
        raise AttributeError("Number of argument under requirement, please read documentation")
    
    password:str = sys.argv[1]
    file_path:str = sys.argv[2]
    # option tracking
    pass_count:int = 0
    options:str = sys.argv[3:]
    for i, option in enumerate(options):
        if pass_count:
            pass_count -= 1
            continue
        # decrypt option
        if "-d" in option:
            decrypt_q:bool = True
        # verbose?
        elif "-v" in option:
            verbose_q:bool = True
        # new name?
        elif "-s" in option:
            if "-" not in options[i + 1]:
                pass_count = 1
                search_location:str = options[i + 1]
                # TODO file = search(file, search_location)
            else:
                raise AttributeError("No name provided after -n")
        # new name?
        elif "-n" in option:
            if "-" not in options[i + 1]:
                pass_count = 1
                file_new_path:str = options[i + 1]
            else:
                raise AttributeError("No name provided after -n")
        else:
            raise AttributeError(f"Unknown option {option}")
        
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
        gs_decrypt_file(password, file_path, file_new_path)
    else:
        gs_encrypt_file(password, file_path, file_new_path)
    