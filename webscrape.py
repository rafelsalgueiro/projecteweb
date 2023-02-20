import urllib3

def webScrape(object):

    def __init__(self)-> None:
        self.url = "https://www.99-bottles-of-beer.net/lyrics.html"
        pass

    def get_web(self):
        #conectar http
        httppool = urllib3.PoolManager()
        #enviar peticio
        resposta = httppool.request("GET", self.url())
        #guardar html resposta
        self.html = resposta.data.decode("utf-8")

    def get_data(self):
        # descarregar web
        self.get_web()
        # llegir dades
        # return dades
        pass

if __name__ =="__main__":
    client = webScrape()
    dades = client.get_data()
    print(dades)