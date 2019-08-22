import download_func
import findsearchquery
from concurrent.futures import ThreadPoolExecutor

threads_count = 4

def get_list (list_of_links):
    path = download_func.path_of_file(link_to_file)
    result = findsearchquery.finder(path)
    return(result)

def execute_threads(urls):
    with ThreadPoolExecutor(max_workers=threads_count) as executor:
      return executor.map(get_list, urls, timeout=120)


list_of_links = []
for i in range (2, 3):
    link_to_file = 'https://api.raan.garagemca.org/syslog.' + str(i) + '.gz'
    list_of_links.append(link_to_file)

results = execute_threads(links.list_of_links)

print(results)