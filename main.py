from bs4 import BeautifulSoup
import requests

url = "https://www.avto.net/Ads/results.asp?znamka=&model=&modelID=&tip=&znamka2=&model2=&tip2=&znamka3=&model3=&tip3=&cenaMin=6000&cenaMax=9000&letnikMin=2012&letnikMax=2090&bencin=0&starost2=999&oblika=13&ccmMin=0&ccmMax=99999&mocMin=&mocMax=&kmMin=75000&kmMax=200000&kwMin=96&kwMax=999&motortakt=&motorvalji=&lokacija=0&sirina=&dolzina=&dolzinaMIN=&dolzinaMAX=&nosilnostMIN=&nosilnostMAX=&lezisc=&presek=&premer=&col=&vijakov=&EToznaka=&vozilo=&airbag=&barva=&barvaint=&EQ1=1000000000&EQ2=1000000000&EQ3=1000000000&EQ4=100000000&EQ5=1000000000&EQ6=1000000000&EQ7=1010100020&EQ8=101000000&EQ9=1000000000&KAT=1010000000&PIA=&PIAzero=&PIAOut=&PSLO=&akcija=&paketgarancije=0&broker=&prikazkategorije=&kategorija=&ONLvid=&ONLnak=&zaloga=10&arhiv=&presort=&tipsort=&stran="
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows 98)'
    }


result = requests.get(url, headers=headers)
doc = BeautifulSoup(result.text, "html.parser")
print(doc.prettify())