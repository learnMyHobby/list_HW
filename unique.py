#   Print all the unique elements in the following list
#   fifa = ['Italy','Argentina','Germany','Brazil','France',
#          'Brazil','Italy','Spain','Germany','France']

def country(fifa):
    country_list = set(fifa)
    unique_country = list(country_list)
    for i in country_list:
        print(i)



fifa = ['Italy','Argentina','Germany','Brazil','France',
        'Brazil','Italy','Spain','Germany','France']
print("The unique list is : ")
country(fifa)



