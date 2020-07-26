import requests

res = requests.get("https://automatetheboringstuff.com/files/rj.txt")

res.status_code

len(res.text)

print(res.text[:500])

res.raise_for_status()

badRes = requests.get("https://iejrgirtugrugurgh.com/dkdkdd")