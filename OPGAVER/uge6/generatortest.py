import generator

url_list = [
    "https://www.gutenberg.org/files/1952/1952-0.txt",
    "https://www.gutenberg.org/files/43/43-0.txt"
]

generator = generator.generator(url_list)

generator.download(
    "https://www.gutenberg.org/files/1342/1342-0.txt", "PrideandPrejudice.txt")
