#!/usr/bin/python3
"""Fetch Employees TODO list and exports
the data in the json format"""

if __name__ == '__main__':
    import json
    import requests
    import sys

    try:
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        response = response.json()
        new_obj = {}
        for i in range(1, 11):
            emp_id = i
            list_id = emp_id - 1
            response_rep = response[list_id].get('username')

            tasks = requests.get("https://jsonplaceholder.typicode.com/todos")
            tasks = tasks.json()

            new_list = []

            for dic in tasks:
                if int(dic.get('userId')) == emp_id:
                    new_dic = {}
                    new_dic['username'] = response_rep
                    new_dic['task'] = dic.get('title')
                    new_dic['completed'] = dic.get('completed')
                    new_list.append(new_dic)

            key = str(emp_id)
            new_obj[key] = new_list
        filename = "todo_all_employees.json"
        with open(filename, "w", encoding='utf-8') as f:
            save_json = json.dumps(new_obj)
            f.write(save_json)

    except Exception as err:
        print("Error: {}".format(err))
