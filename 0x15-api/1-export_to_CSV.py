#!/usr/bin/python3
"""Fetch Employees TODO list and exports
the data in the CSV format"""

if __name__ == '__main__':
    import requests
    import sys

    try:
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        response = response.json()
        emp_id = int(sys.argv[1])
        list_id = emp_id - 1
        response = response[list_id].get('username')

        tasks = requests.get("https://jsonplaceholder.typicode.com/todos")
        tasks = tasks.json()

        filename = "{}.csv".format(emp_id)
        with open(filename, "a", encoding='utf-8') as f:
            for dic in tasks:
                if int(dic.get('userId')) == emp_id:
                    f.write("\"{}\",\"{}\",\"{}\",\"{}\"\n".format(
                        emp_id, response, dic.get('completed'), dic.get('title')))

    except Exception as err:
        print("Error: {}".format(err))
