import urllib3
import bs4

def webScrape(object):

    def __init__(self)-> None:
        self.url = "https://www.99-bottles-of-beer.net/lyrics.html"

    def get_web(self):
        #conectar http
        httppool = urllib3.PoolManager()
        #enviar peticio
        resposta = httppool.request("GET", self.url())
        #guardar html resposta
        self.html = resposta.data.decode("utf-8")

    def parse_bs4(self):
        soup = bs4.BeautifullSoup(self.html, features="html.parser")
        div_main = soup.find_all('div', attrs=("id":"main"))[0]
        self.data = div_main.find_all('pre')[0]

    def extract_data(self):
        self.data = self.data.text
        

    def parse_html(self):
        # parse bs4
        self.parse_bs4()
        # extreure dades html
        self.extract_data()
        


    def get_data(self):
        # descarregar web
        self.get_web()
        # llegir dades
        self.parse_html()
        # return dades
        

if __name__ =="__main__":
    client = webScrape()
    dades = client.get_data()
    print(dades)