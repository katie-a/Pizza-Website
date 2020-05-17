import urllib.request, urllib.error, urllib.parse



# CHALLENGE 1: Make a connection to: 127.0.0.1:8080/winning and print
#              the response.
response = urllib.request.urlopen("http://127.0.0.1:5000")
html = response.read()
print(html)
