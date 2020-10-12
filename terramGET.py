import re
import requests

regex = '" value="([^"]*?)"'
url = "https://www.terramaterbooks.com/wp-admin/user-new.php"

pagina = requests.get(url)
matches = re.findall(regex,pagina.text)

print(matches)