import requests

website = "https://jsonplaceholder.typicode.com/posts/1"
print(requests.get(website).json())
response = requests.delete(website,data={
    "id": 1,
    "userId":12,
    "title": "my new post",

})
print(response)