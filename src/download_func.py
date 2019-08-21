import tempfile
import wget

import gzip
import shutil

# скачивает архив по ссылке, распаковывает архив и возвращает путь к распакованному файлу
def path_of_file(link):

    gzipped_file  = wget.download(link)

    ungzipped_file = tempfile.NamedTemporaryFile(delete=False)

    with gzip.open(gzipped_file, 'rb') as f_in:
        with open(ungzipped_file.name, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    return(ungzipped_file.name)
