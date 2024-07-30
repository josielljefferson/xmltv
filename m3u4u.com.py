import requests
from datetime import datetime

# Funções para executar os links
def execute_link1():
    response = requests.get("http://m3u4u.com/m3u/26p5n3jr29cx5p86yv7j")
    print(f"Link 1 executado com status: {response.status_code} às {datetime.now()}")

def execute_link2():
    response = requests.get("http://m3u4u.com/m3u/jq2zy9v62gfw9x37nxr5")
    print(f"Link 2 executado com status: {response.status_code} às {datetime.now()}")

def execute_link3():
    response = requests.get("http://m3u4u.com/m3u/5z3endemwjfdzj52yqpk")
    print(f"Link 3 executado com status: {response.status_code} às {datetime.now()}")

# Executar as funções
execute_link1()
execute_link2()
execute_link3()