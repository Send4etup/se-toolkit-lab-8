#!/usr/bin/env python3
import urllib.request
import json

url = 'http://localhost:8000/analytics/scores?lab=lab-08'
req = urllib.request.Request(url, headers={'Authorization': 'Bearer my-secret-api-key'})
try:
    with urllib.request.urlopen(req, timeout=5) as resp:
        data = json.loads(resp.read())
        print(json.dumps(data, indent=2))
except Exception as e:
    print(f'Error: {e}')
