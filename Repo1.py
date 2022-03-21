from URLSearchParams import URLSearchParams

url = "https://duckduckgo.com/?name=python&atb=v279-1&ia=web"

var = URLSearchParams(url).get("name")

print(var)