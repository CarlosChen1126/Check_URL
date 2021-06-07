import requests
from bs4 import BeautifulSoup
import re

f = open('weblink.txt', 'w', encoding='utf8')

url = "https://www.ntu.edu.tw/"
url_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
}
r = requests.get(url, headers=url_headers)
r.encoding = "utf8"
soup = BeautifulSoup(r.text, "lxml")
soup.prettify()
url_regexp = re.compile("^http")
tag_list = soup.find_all(href=url_regexp)


for url_str in tag_list:
    x = url_str.get('href')
    x = requests.get(x, headers=url_headers)
    print("'"+"https://www.ntu.edu.tw/"+"'"+" "+"'" +
          url_str.get('href') + "'", x.status_code, file=f)
    # print("'"+"https://www.ntu.edu.tw/"+"'"+" "+"'" +
    #      url_str.get('href') + "'", x.status_code)
    try:
        x = requests.get(url, headers=url_headers)
        x.raise_for_status()
    except requests.exceptions.RequestException as ex1:
        print("Http請求錯誤: " + str(ex1), file=f)
    except requests.exceptions.HTTPError as ex2:
        print("Http回應錯誤: " + str(ex2), file=f)
    except requests.exceptions.ConnectionError as ex3:
        print("網路連線錯誤: " + str(ex3), file=f)
    except requests.exceptions.Timeout as ex4:
        print("Timeout錯誤: " + str(ex4), file=f)
f.close()
