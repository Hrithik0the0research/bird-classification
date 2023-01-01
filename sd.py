from bs4 import BeautifulSoup
import requests
urls=[]
def site_req(site):
    r=requests.get(site)
    s=BeautifulSoup(r.text,"html.parser")
    h=[]
    for i in s.find_all("a"):
        x=i.attrs["href"]
        h.append(x)
    #print(h)
    s2=[]
    s1="/download"
    for i in h:
        if(s1 in i):
            s2.append(i)
    print(s2)
    x1="https://xeno-canto.org"
    for i in s2:
        m=x1+i
        print(m,end=" ")

    
if __name__=="__main__":
    site_req("https://xeno-canto.org/species/Pavo-cristatus")
