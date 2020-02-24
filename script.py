import requests

r = requests.get("https://jarestreh.github.io")
print(r.status_code)
print(r.ok)
