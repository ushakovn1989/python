import os
import django
from collections import defaultdict

root_dir = django.__path__[0]
folder_size_stats = defaultdict(int)
for root, dirs, files in os.walk(root_dir):
    for file in files:
        file_size = os.stat(os.path.join(root, file)).st_size
        max_size = 10
        while file_size >= max_size:
            max_size *= 10
        folder_size_stats[max_size] += 1

for key, value in sorted(folder_size_stats.items()):
    print(f'{key}: {value}')
