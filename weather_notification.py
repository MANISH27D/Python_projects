import requests
from bs4 import BeautifulSoup


def getdata(url):
    r = requests.get(url)
    return r.text

htmldata =getdata("https://weather.com/en-IN/weather/tenday/l/Rajpath+Area+Delhi?canonicalCityId=bd07c6679ad5069265f742eb66d5d53172210b02b127807d6a47e92807799fbe")

soup = BeautifulSoup(htmldata, 'html.parser')

 
chances_wather = soup.find_all("p", class_="DailyContent--narrative--3Ti6_")

 
  
temp_weather = str(chances_wather) 

result ="\n"+"current weather status in Delhi: " + "\n\n" + temp_weather[66:153] +"\n\n" +"temperature: " + temp_weather[154:162]


print(result)