#!/usr/bin/python3
"""Displays the TODO list progress of employee whose
ID is passed as a parameter to the script"""

if __name__ == "__main__":
    import requests
    import sys

    try:
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        response = response.json()
        emp_id = int(sys.argv[1])
        list_id = emp_id - 1
        response = response[list_id]

        tasks = requests.get("https://jsonplaceholder.typicode.com/todos")
        tasks = tasks.json()
        countTask, countComp = 0, 0
        compTask = list()

        for dic in tasks:
            if int(dic.get('userId')) == emp_id:
                countTask += 1
                if dic.get('completed') is True:
                    countComp += 1
                    tk = dic.get('title')
                    compTask.append(tk)

        print("Employee", response['name'],
              "is done with tasks({}/{}):".format(countComp, countTask))
        for i in compTask:
            print("\t", i)

    except Exception as err:
        print("Error: {}".format(err))
