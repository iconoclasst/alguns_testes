import os
import sys 

size = os.path.getsize('index.html')

header = {
            'Code': '200',
            'Size': str(size)
        }
tamanho = sys.getsizeof(header)

print(header)
print(tamanho)