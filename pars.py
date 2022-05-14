import requests
from bs4 import BeautifulSoup
#from fake_useragent import UserAgent


def start_pars():
    #UA = UserAgent()

    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15'
    }

    response = requests.get(url="https://animego.org", headers = headers)

    with open(f'inde.html', 'w') as file:
        file.write(response.text)

    with open('inde.html') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')

    todayAnimeAll = soup.find_all('div', class_ = "last-update-item")

    data = []

    for anime in todayAnimeAll:
        title = anime.find("span", class_ = "last-update-title").text.strip() 
        num = anime.find("div", class_ = "text-truncate").text.strip()
        trunslater_audio = anime.find("div", class_="text-gray-dark-6").text.strip()

        data.append(
            [title, num, trunslater_audio]
        )

        #print(title, " - ", num, trunslater_audio)
    return data

def main():
    print("Choice options: \nPress 1 if you want to see all new anime\nPress 2 if you want to see anime from voiceline\nPress 3 if you want check anime")
    newArray = start_pars()

    n = int(input("You choice is: "))
    
    

    def allAnime():    
        for line in newArray:
            print(line[0], ", ", line[1], ", ", line[2])

    def Ozvuchka(flagName):
        for line in newArray:
            if line[2] == flagName:
                print(line[0], ", ", line[1], ", ", line[2])

    def findName(AnimeName):
        for line in newArray:
            if line[0] == AnimeName:
                print(line[0], ", ", line[1], ", ", line[2])

    if n == 1:
        allAnime()
    elif n == 2:
        voiceline = str(input("Input name voiceliner: "))
        Ozvuchka(voiceline)
    elif n == 3:
        nameAnime = str(input("Input name Anime: "))
        findName(nameAnime)
    else:
        print("Wrong settings!")
    

if __name__ == "__main__":
    main()