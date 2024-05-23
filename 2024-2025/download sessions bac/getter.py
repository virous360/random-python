import requests
import json
import download

url = lambda page : 'https://cyclades.education.gouv.fr/delos/api/public/sujets/ec?sort=libelle&order=ASC&page='+str(page)+"&itemsPerPage=1&globalFilter=svt&filtersByColumn%5B0%5D.value=,G%C3%A9n%C3%A9rale&filtersByColumn%5B0%5D.type=texte&filtersByColumn%5B0%5D.operation=IN&filtersByColumn%5B0%5D.name=parametrageSujet.voies&filtersByColumn%5B0%5D.otherColumnName=undefined&filtersByColumn%5B1%5D.value=,Premi%C3%A8re&filtersByColumn%5B1%5D.type=texte&filtersByColumn%5B1%5D.operation=IN&filtersByColumn%5B1%5D.name=parametrageSujet.niveaux&filtersByColumn%5B1%5D.otherColumnName=undefined"

response = requests.get(url(1))
max_p = json.loads(response.text)["totalPages"]
print(max_p)

def start():
    for i in range(1,max_p):
        pdf = requests.get(url(i))
        ids = json.loads(pdf.content)["content"][0]["fichiers"][0]["id"]
        # sujets.append(ids)
        download.download(ids,str(i))
        print(ids," | sujet "+str(i)+"/"+str(max_p-1))


start()