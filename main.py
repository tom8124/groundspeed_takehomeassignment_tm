import pandas as pd

car_1 = {
    'id':['0001'],
    'year':['2000'],
    'make':['Kia'],
    'model':['Sephia'],
    'purchase value ($)':[850],
    'VIN':['10FC03IE1994GIWOK'],
    'license plate state':['NY'],
    'license plate number':['IWSB012']
    }

car_2 = {
    'id':['0002'],
    'year':['2015'],
    'make':['RAM'],
    'model':['2500'],
    'purchase value ($)':[23000],
    'VIN':['02TI15WID2022BDWRN'],
    'license plate state':['NY'],
    'license plate number':['BTMLT22']
}

fleet = pd.concat([(pd.DataFrame(car_1)),(pd.DataFrame(car_2))])

print(pd.DataFrame(fleet))

metrics = {
    'Total count':[fleet['id'].count()],
    'Total purchase price':[fleet['purchase value ($)'].aggregate('sum')]
    }

print(pd.DataFrame(metrics))