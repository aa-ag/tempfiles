############------------ IMPORTS ------------############
import tempfile

############------------ CREATE SELFDESTRUCTING FILE ------------############
def self_destructing_file():
    '''
     (i) create a temporary file 
     (ii) write some data to it,
     (iii) then read it, (iv) close it and
     (v) delete it
    '''
    # (i)
    temporary_file = tempfile.TemporaryFile()
    print(temporary_file.read())

    # (ii)
    input_from_user = input("Enter text: ")
    temporary_file.write(input_from_user.encode())

    # (iii)
    temporary_file.seek(0)

    print(temporary_file.read().decode())

    # (iv)
    temporary_file.close()
    try:
        # (v)
        print(temporary_file.read())
    except:
        print("File no longer exists")

    print(tempfile.gettempdir())
    
############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    self_destructing_file()
    '''
     b''
     b'Hello World'
     File no longer exists
    '''