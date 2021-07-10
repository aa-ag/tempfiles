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
    temporary_file.write(b'Hello World')

    # (iii)
    temporary_file.seek(0)

    # (iv)
    print(temporary_file.read())

    # (v)
    temporary_file.close()
    try:
        print(temporary_file.read())
    except:
        print("File no longer exists")


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    self_destructing_file()
    '''
     b''
     b'Hello World'
     File no longer exists
    '''