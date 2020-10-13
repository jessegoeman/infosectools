import re
import requests

regex = '" value="([^"]*?)"'
url = "https://www.servus-buch.at/wp-admin/user-new.php"

pagina = requests.get(url)
matches = re.findall(regex,pagina.text)

print(matches)