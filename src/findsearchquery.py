import subprocess
import urllib.parse
import re

def finder(pathtofile):
    cmd = f"cat {pathtofile} | grep search%5Bquery%5D="
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    reslt = process.communicate()[0]
    listofall = []
    reslt_as_string_list = str(reslt).split("\\n")

    for s in reslt_as_string_list:
        try:

            f = urllib.parse.unquote(s)
            regex  = 'search\[query\]=([^&]+)'
            res = re.search(regex, f)
            listofall.append([res.group(1), f])

        except AttributeError:
            listofall.append(None)
    return(listofall)
