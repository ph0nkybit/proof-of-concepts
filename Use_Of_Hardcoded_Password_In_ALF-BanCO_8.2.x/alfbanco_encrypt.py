def encryptSystemDataSQLite(file, password):

    from Crypto.Hash import SHA 
    from Crypto.Cipher import ARC4
    from struct import unpack
    from tempfile import NamedTemporaryFile
    from shutil import copyfile
    from os import remove
    ret = None
    with open(file,'rb') as f:
        key = SHA.new(password).digest()[:16]
        header = (f.read(1024))
        declared_ps = unpack('>H',header[16:18])[0]
        if declared_ps == 1:
            declared_ps = 65536
        t = NamedTemporaryFile(delete=False,suffix='.alfdb8')
        f.seek(0)
        while True:
            block = f.read(declared_ps)
            if not block:
                break
            t.write(ARC4.new(key).encrypt(block))
        t.close()
        ret = t.name
        copyfile(ret, file.split('.')[0] + '.alfdb8')
        remove(ret)
    return ret
    
encryptSystemDataSQLite('HbDat001.sqlite','Wbf*************')
