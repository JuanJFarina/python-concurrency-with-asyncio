import requests

# I/O-bound operation, requesting content through the network
response = requests.get("https://www.example.com")

# CPU-bound operation, processing data from a dictionary
items = response.headers.items()
headers = [f"{key}: {value}" for key, value in items]
formatted_headers = "\n".join(headers)

# I/O-bound operation, writing data to a file
with open("headers.txt", "w") as file:
    file.write(formatted_headers)
