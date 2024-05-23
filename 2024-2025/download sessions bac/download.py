import requests

url = "https://cyclades.education.gouv.fr/delos/api/file/public/"

def download(id : str,name :str) -> None:
    r = requests.get(url+id)
    with open(".\\hi\\"+str(name)+".pdf","wb") as pdf:
        pdf.write(r.content)