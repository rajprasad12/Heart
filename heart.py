import gzip
import time
import subprocess

subprocess.Popen('color 4', shell=True)
for i in range(10):
    print(gzip.decompress(b'\x1f\x8b\x08\x00\x95\x10\xe0R\x02\xffSPP\xf0\xc9/KU\x80\x03\x10\x8f\x0bB\xa1c.l\x82dJ\xe0\xb0\x01\xe6\x02\x0cATa.T\xf7\x02\x00\xd9\x91g\x05\xc5\x00\x00\x00').decode('ascii'))
    time.sleep(1)
    print('\n=========================\n')