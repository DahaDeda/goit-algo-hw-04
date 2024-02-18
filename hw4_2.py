from pathlib import Path
import re

def get_cats_info():
    with open("D:\\Projects/new_file.txt", encoding = "utf-8") as f_cat:
        lines = f_cat.read()
        # print(lines)
        lines = re.sub(r"\n", ",", lines)
        cat_list = []
        for cat in lines.split(','):
            # print(cat)
            if cat.isalpha():
                cat_name = {"name":cat}
                cat_list.append(cat_name)
                # print(cat_age)
            elif cat.isdigit():
                cat_age = {"age":cat}
                cat_list.append(cat_age)
                # print(cat_name)
            else:
                cat_id = {"id":cat}
                # print(cat_id)
                cat_list.append(cat_id)
                
        revers_cat_list = list(reversed(cat_list))
        print(revers_cat_list)
            
get_cats_info()