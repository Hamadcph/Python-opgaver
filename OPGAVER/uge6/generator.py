import requests
import threading
import concurrent
import multiprocessing
import os
from urllib.parse import urlparse


class generator():
    def __init__(self, url_list):
        self.url_list = url_list
        self.max = len(url_list)
        self.current = 0

    def download(self, url, filename=None):

        if filename is None:
            filename = os.path.basename(urlparse(url).path)
            if url not in self._url_list:
                self._url_list.append(url)
                self.max += 1

        try:
            response = requests.get(url)

            with open(filename, 'wb') as fd:
                for chunk in response.iter_content(chunk_size=1024):
                    fd.write(chunk)

        except Exception as err:
            print(f'Other error occurred: {err}')
        else:
            print('Success!')

    def multi_download(self, url_list):
        self._url_list = url_list
        self.high = len(url_list)

    def getUrlList(self):
        return self._url_list

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current < self.max:
            item = self.getUrlList()
            filename = os.path.basename(urlparse(item[self.current]).path)
            with open(filename, encoding="utf-8") as file:  #
                print("in __next__ with open("+filename+")")
                return (filename, file.read())
        raise StopIteration
