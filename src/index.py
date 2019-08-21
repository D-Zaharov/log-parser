import download_func
import findsearchquery

for i in range (2, 3):
    link_to_file = 'https://api.raan.garagemca.org/syslog.' + str(i) + '.gz'
    print("Downloading " + link_to_file)
    path = download_func.path_of_file(link_to_file)
    result = findsearchquery.finder(path)
    print(result)
