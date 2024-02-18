from pathlib import Path
import re

def get_cats_info():
    try:
        with open("D:\\Projects/new_file.txt", encoding = "utf-8") as f_cat:
            lines = f_cat.read()
            lines = re.sub(r"\n", ",", lines)
            cat_list = []
            for cat in lines.split(','):
                if cat.isalpha():
                    cat_name = {"name":cat}
                    cat_list.append(cat_name)
                elif cat.isdigit():
                    cat_age = {"age":cat}
                    cat_list.append(cat_age)
                else:
                    cat_id = {"id":cat}
                    cat_list.append(cat_id)  
            revers_cat_list = list(reversed(cat_list))
            print(revers_cat_list)
    except FileNotFoundError:
        print("Your file not found")
            
get_cats_info()