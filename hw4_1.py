import re
from pathlib import Path as pt

def total_salary(path):
    try:
        with open(path, encoding = 'utf-8') as f_sal:
            lines = f_sal.read()
            digits = re.findall(r"\d+", lines)
            sum = 0
            for dig in digits:
                    sum +=int(dig)
            aver_sum = sum / len(digits) 
       
            print(f"Загальна сума заробітної плати: {sum}, Середня заробітна плата: {aver_sum}")
            
    except FileNotFoundError:
        print("Your file not found")
path_to_file = "D:\\Projects/new_file.txt"
result = total_salary(path_to_file)