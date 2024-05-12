from os.path import exists


def total_salary(path: str):
    if exists(path) is False:
        return [0, 0]

    total_salary_value = 0

    with open(path, 'r', encoding='utf-8') as fh:
        workers = [line.rstrip().split(',') for line in fh]

    for item in workers:
        total_salary_value += int(item[1])

    return [total_salary_value, total_salary_value // len(workers)]


total, average = total_salary('data.txt')
print(f'Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}')
