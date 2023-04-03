import sys
def gs_encrypt(password:str, file:str):
    print(f"{file} decrypted")

def gs_decrypt(password:str, file:str):
    print(f"{file} encrypt")   

if __name__ == "__main__":
    # Checking python parameter when file is directly provoked
    if len(sys.argv) <= 2:
        raise AttributeError("Number of argument under requirement, please read documentation")
    
    password:str = sys.argv[1]
    file:str = sys.argv[2]
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
                new_name:str = options[i + 1]
            else:
                raise AttributeError("No name provided after -n")
        else:
            raise AttributeError(f"Unknown option {option}")
    
    # Pass result to calculator class
    if decrypt_q:
        gs_decrypt(password, file)
    else:
        gs_encrypt(password, file)
    