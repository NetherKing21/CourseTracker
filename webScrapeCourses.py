from requests_html import HTMLSession
from bs4 import BeautifulSoup

session = HTMLSession()

# Getting Catalog Page
URL = "https://www.byui.edu/catalog/#/courses"

# Fixing Header to try and bypass the 403 response
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}

page = session.get(URL, headers=headers)
# page.html.render(sleep=5)

# Check to see if page request worked
if page.status_code == 200:
    print(page.text)  # Print the content of the page
else:
    print(f'Request failed with status code: {page.status_code}')

# Making Beautiful Soup Object
soup = BeautifulSoup(page.content, "html.parser")

all_departments = soup.find_all("div", class_="style__collapsibleBox___15waq")

CSE_department = all_departments.find("h2", string=lambda text: "computer science" in text.lower()).parent.parent.parent

print(CSE_department.prettify())