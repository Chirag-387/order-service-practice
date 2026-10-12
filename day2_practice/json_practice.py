import httpx

response = httpx.get("https://jsonplaceholder.typicode.com/users")

if(response.status_code == 200):
    data = response.json()
    print(type(data))
    print(len(data))
    print(data[0]["name"])
else:
    print(response.status_code)