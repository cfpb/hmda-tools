import requests
import os, errno

def download_file(uri, filename):
    r = requests.get(uri)
    if r.status_code == 200:
        with open(filename, 'wb') as f:
            for chunk in r.iter_content():
                f.write(chunk)

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise
