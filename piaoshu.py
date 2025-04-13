import requests
from bs4 import BeautifulSoup
# 导入rich模块
from rich.table import Table
from rich.console import Console

import time

while True:
    url = "http://投票网址/StuChoose/index.jsp"
    response = requests.get(url)
    response.encoding = 'gbk'
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    # 设置总投票数
    renqi_elements = soup.find_all('div', id="renqi")
    num_candidates = len(renqi_elements)




    # 创建一个console实例
    console = Console()

    # 创建一个Table实例
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("学院", style="dim", width=12)
    table.add_column("姓名与班级", style="dim", width=30)
    table.add_column("票数", style="dim", width=5)

    # 创建一个列表来存储特殊的行
    special_rows = []

    for i in range(num_candidates):
        # 获取学院
        college = soup.find_all('span', style="font-size: 15px; color: rgb(137, 125, 125); font-weight: bold;")[i*3+1].get_text(strip=True)
        # 获取姓名与班级
        name_class = soup.find_all('span', style="font-size: 15px; color: rgb(137, 125, 125); font-weight: bold;")[i*3+2].get_text(strip=True)
        # 获取票数
        votes = renqi_elements[i].get_text(strip=True)
        # 检查name_class是否包含特定的姓名
        if "姓名1" in name_class or "姓名1" in name_class or "姓名1" in name_class:
            # 如果是，将这一行的样式设置为红色，并将票数的样式设置为黄色
            special_rows.append([college, "[red]" + name_class + "[/red]", "[yellow]" + votes + "[/yellow]"])
        else:
            # 如果不是，正常添加行
            table.add_row(college, name_class, votes)

    # 先将特殊的行添加到表格中
    for row in special_rows:
        table.add_row(*row)

    # 输出表格
    console.print(table)


    # 创建一个列表来存储所有的候选人
    candidates = []

    for i in range(num_candidates):
        # 获取学院
        college = soup.find_all('span', style="font-size: 15px; color: rgb(137, 125, 125); font-weight: bold;")[i*3+1].get_text(strip=True)
        # 获取姓名与班级
        name_class = soup.find_all('span', style="font-size: 15px; color: rgb(137, 125, 125); font-weight: bold;")[i*3+2].get_text(strip=True)
        # 获取票数
        votes = renqi_elements[i].get_text(strip=True)
        # 将候选人的信息添加到candidates列表中
        candidates.append((college, name_class, votes))

    # 对candidates列表进行排序，排序的依据是票数，排序的顺序是从高到低
    sorted_candidates = sorted(candidates, key=lambda x: int(x[2]), reverse=True)

    # 创建一个新的Table实例
    sorted_table = Table(show_header=True, header_style="bold magenta")
    sorted_table.add_column("排名", style="dim", width=5)
    sorted_table.add_column("学院", style="dim", width=12)
    sorted_table.add_column("姓名与班级", style="dim", width=30)
    sorted_table.add_column("票数", style="dim", width=5)

    # 将排序后的候选人信息添加到sorted_table中
    for i, candidate in enumerate(sorted_candidates[:20]):
        sorted_table.add_row(str(i+1), *candidate)

    # 输出sorted_table
    console.print(sorted_table)

    #输出投票总数与票数总数
    print("投票总数："+str(num_candidates))
    print("票数总数："+str(sum(int(renqi_element.get_text(strip=True)) for renqi_element in renqi_elements)))

    # 暂停3秒
    time.sleep(2)