from os.path import exists


def get_cats_info(path: str):
    if exists(path) is False:
        return []

    cats = []

    try:
        with open(path, 'r', encoding='utf-8') as fh:
            for line in fh:
                splitted = line.rstrip().split(',')
                cats.append({
                    'id': splitted[0],
                    'name': splitted[1],
                    'age': splitted[2],
                })
    except FileNotFoundError:
        print('File not found')

    return cats


cats_info = get_cats_info('data.txt')
print(cats_info)
