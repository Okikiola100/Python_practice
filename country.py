#!\C:\\Users\Azubike Chiefo\AppData\Local\Programs\Python\Python38-32
# Author: Oladapo Okikiola
count_country = {}
def addone(country):
    if country in count_country:
        count_country[country] += 1
    else:
        count_country[country] = 1
        addone('Nigeria')
        addone('South Africa')
        addone('Ghana')
        print(len(count_country))
print("'done'\nAuthor: Oladapo Okikiola")
