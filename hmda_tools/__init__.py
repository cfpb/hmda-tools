import requests

def download_file(uri, filename):
    r = requests.get(uri)
    if r.status_code == 200:
        with open(filename, 'wb') as f:
            for chunk in r.iter_content():
                f.write(chunk)
