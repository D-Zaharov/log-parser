import tempfile
import wget
import zipfile
from pathlib import PurePath

def path_of_files(link):

    gzipped_file = tempfile.NamedTemporaryFile()

    wget.download(link, gzipped_file.name)

    temp_dir_path = tempfile.mkdtemp()

    zip = zipfile.ZipFile(gzipped_file.name)
    zip.extractall(temp_dir_path)
    list_of_files = zip.namelist()

    zip.close
    gzipped_file.close

    list_of_path = []
    for file_name in list_of_files:
        path = str(PurePath(temp_der_path, file_name))
        list_of_path.append(path)

return(list_of_path)