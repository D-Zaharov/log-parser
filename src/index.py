import download_func
import findsearchquery

for i in range (1, 51):
    link_to_file = str('https://api.raan.garagemca.org/syslog.' + i + '.gz')
    list_of_path = download_func.path_of_files(link_to_file)
    for element in list_of_path:
        result = findsearchquery.finder(element)
        print(result)