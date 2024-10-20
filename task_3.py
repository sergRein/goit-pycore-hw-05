import os
import argparse
from datetime import datetime


LOG_LEVELS = ('INFO', 'DEBUG', 'ERROR', 'WARNING') #lets predefine log levels


def parse_log_line(line: str) -> dict:
    parts = line.split(' ', 3) #split log string to ensure its correct
    if len(parts) < 4:
        return {}
    
    date = parts[0]
    time = parts[1]
    log_level = parts[2].upper()
    info = parts[3].strip()
    #check date and time
    try:
        datetime.strptime(date, '%Y-%m-%d')
        datetime.strptime(time, '%H:%M:%S')
    except ValueError:
        return {}

    if log_level not in LOG_LEVELS: #check log level
        return {}
    
    return {'date': date, 'time': time, 'log_level': log_level, 'info': info}


def load_logs(file_path: str):
    with open(file_path, 'r') as file:
        for line in file:
            log = parse_log_line(line)
            if log:
                yield log #use generator if log file is huge


def filter_logs_by_level(logs: list, level: str) -> list:
    list_to_show = [log for log in logs if log['log_level'] == level.upper()]
    if list_to_show:
        print(f"Деталі логів для рівня '{level.upper()}':")
        for log_item in list_to_show:
            print(f"{' '.join(str(value) for value in log_item.values())} ") #use only values in log item dict
    else:
       print(f"Відсутні логи для рівня '{level.upper()}'") 


def count_logs_by_level(logs: list) -> dict:
    counts = {}
    for log_level in LOG_LEVELS:
        # filter logs by log_level
        counts[log_level] = len(list(filter(lambda log: log['log_level'] == log_level, logs)))
    return counts


def display_log_counts(counts: dict):
    print(f"{'Рівень логування':<18} | {'Кількість':<10}")
    print('-' * 35)
    for level, count in counts.items():
        print(f"{level:<18} | {count:<10}")


def main():
    parser = argparse.ArgumentParser(description="Парчер лог файлу")
    parser.add_argument('file_path', type=str, help="Шлях до файлу логів")
    parser.add_argument('log_level', type=str, nargs='?', default=None, choices=[log_level.lower() for log_level in LOG_LEVELS],  help="Вивід логів обраного рівня (info|debug|warning|errror)")
    
    args = parser.parse_args()

    if not os.path.isfile(args.file_path):
        print(f"Файл за шляхом {args.file_path} не знайдено.")
        return
    loaded_logs = list(load_logs(args.file_path))
    display_log_counts(count_logs_by_level(loaded_logs))
  
    if args.log_level:
        filter_logs_by_level(loaded_logs, args.log_level)


if __name__ == '__main__':
    main()