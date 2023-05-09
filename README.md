# GS-Encryption
A Good and Simple Encryption algorism that encrypt and decrypts any file or data based on a user defined or randomly generated password
# WIP
Please note GS-Encryption is under active development and is not fully functional
## Usage Direction
### Powershell
To run encrypter:
`
python3 gs_encrypt.py [password] [target file] [*options]
`
### Supported options
- `-r`: random unicode password
- `-rn`: random ascII password
- `-d`: decrypt
- `-v`: verbose
- `-n`: name new file
# Version
0.0.0: Function WIP
### Plans
0.0.1: VIRELAY
- Encryption and decryption of files
- Invoked from command line through function arguments
- Support the following command line options
  - `-r`: random unicode password
  - `-rn`: random ascII password
  - `-d`: decrypt
  - `-v`: verbose
  - `-n`: name new file
Future:
- Check file can be decrypted
- options
  - `-s`: search file in directories
  - `-dc`: do not validate the file can be decrypted again to save time
  - `-ss`: do not include encrypter information like version in encrypted output (not suggested as currently enccrypter do not have deployment setup, one must reference commit versions)
- Basic UI for encryption and decryption
- Enhance encryption for basic file types
- Method of saving password more easily
- More encryption options
  - -v: verbose feedback
  - -s {search location}: search for file in target location
- Multi-layer encryption
- String and python basic type encryption
- Signature of encryptor version in encrypted file
- feedback on encryption strength
- generate password
- test
- validation method to make sure file is decryptable
