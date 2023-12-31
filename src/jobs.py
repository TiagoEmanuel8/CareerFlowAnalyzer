from functools import lru_cache
import csv

# ref - dia 32.2 do course


@lru_cache
def read(path):
    with open(path) as file_csv:
        list_dict = list(
            csv.DictReader(file_csv, delimiter=",", quotechar='"')
        )
    # print(list_dict)
    return list_dict


read('src/jobs.csv')
