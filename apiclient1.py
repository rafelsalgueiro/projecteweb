
class ArchivClient(pbject):
    def __init__(self) -> None:
        pass

    def get_data(self):
        # consultar API arxiv
        
        # convertir xml -> dades
        # reduir dades
        # return dades
        pass

if __name__ =="__main__":
    client = ArchivClient()
    dades = client.get_data("transformers")
    print(dades)