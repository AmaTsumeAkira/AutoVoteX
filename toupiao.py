import csv
import requests
import random
import time
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

print("正在初始化")
# 登录URL
login_url = "http://投票网址/StuChoose/UserServlet?command=login"
# 投票URL
vote_url = "http://投票网址/StuChoose/judge.jsp"
# 退出URL
logout_url = "http://投票网址/StuChoose/UserServlet?command=logout"

ua = UserAgent()
# 随机生成请求头
headers = {
    "User-Agent": ua.random,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "http://投票网址",
    "Connection": "keep-alive",
    "Referer": "http://投票网址/StuChoose/index.jsp",
    "Upgrade-Insecure-Requests": "1",
    "DNT": str(random.randint(0, 1)),
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "navigate",
}

#设置固定投票人

fixed_elements = ["28", "24", "16"]
num_random_elements = 7
possible_choices = list(range(1, 35))

for element in fixed_elements:
    possible_choices.remove(int(element))



session = requests.Session()
session.headers.update(headers)

total_votes = 1
failed_votes = 1

print("已完成初始化")

with open('user.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print("\033c")
        message = '''
     _     _     _               ___  _   _  _____  ___    _____  ____   _   _  
    / \   | | __(_) _ __  __ _  |_ _|| \ | ||  ___|/ _ \  | ____||  _ \ | | | | 
   / _ \  | |/ /| || '__|/ _` |  | | |  \| || |_  | | | | |  _|  | | | || | | | 
  / ___ \ |   < | || |  | (_| |  | | | |\  ||  _| | |_| | | |___ | |_| || |_| | 
 /_/   \_\|_|\_\|_||_|   \__,_| |___||_| \_||_|    \___/  |_____||____/  \___/  
  ____      ___     ____     _____       __   _    ____        __   _    _  _   
 |___ \    / _ \   |___ \   |___ /      / /  / |  |___ \      / /  / |  | || |  
   __) |  | | | |    __) |    |_ \     / /   | |    __) |    / /   | |  | || |_ 
  / __/   | |_| |   / __/    ___) |   / /    | |   / __/    / /    | |  |__   _|
 |_____|   \___/   |_____|  |____/   /_/     |_|  |_____|  /_/     |_|     |_|  

 代码已经运行：'''+str(total_votes)+"次" + " 投票成功："+str(total_votes-failed_votes)+"次" + " 投票失败："+str(failed_votes)+"次" + " 代码运行中，如需退出请键入Ctrl+C" '''
 运行总时长：'''+str(total_votes*2)+"秒" + "  平均每次投票耗时："+str(2)+"秒" + "  成功率："+str((total_votes-failed_votes)/total_votes*100)+"%" + "  失败率："+str(failed_votes/total_votes*100)+"%" '''
 '''
        print(message)

        import requests
        from bs4 import BeautifulSoup
        url = "http://投票网址/StuChoose/index.jsp"
        response = requests.get(url)
        response.encoding = 'gbk'
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        # 设置总投票数
        renqi_elements = soup.find_all('div', id="renqi")
        num_candidates = len(renqi_elements)

        # 终端清屏
        userId = row[0]
        password = row[1]
        data_login = {
            "userId": userId,
            "password": password,
            "bnSubmit": "^%^B5^%^C7^%^C2^%^BC"
        }
        response_logout = session.get(logout_url)
        response_login = session.post(login_url, data=data_login)
        print("总投票数：" + str(total_votes))
        print("总投票成功数" + str(total_votes-failed_votes))
        print("投票失败数：" + str(failed_votes))
        if "帐号或密码错误！" not in response_login.text:
            print(userId+"登录成功")
            total_votes += 1
            # 添加随机延迟
            random_elements = random.sample(possible_choices, num_random_elements)
            #final_elements = fixed_elements + [str(element) for element in random_elements]
            final_elements = ["28", "24", "16", "28", "24", "16", "15", "15", "22",  "22"]
            data_vote = {
                "checkbox": final_elements,
                "Submit": "^%^CC^%^E1+^%^BD^%^BB"
            }
            print(final_elements)
            response_vote = session.post(vote_url, data=data_vote)
            if "谢谢您的投票！" in response_vote.text:  # 判断投票是否成功
                print(userId+"投票成功")
                # 退出操作
                response_logout = session.get(logout_url)
                print(userId+"已退出")
                #time.sleep(random.uniform(0.5, 2))
            else:
                print(userId+"投票失败")
                failed_votes += 1
                print(response_vote.text)
                # 退出操作
                response_logout = session.get(logout_url)
                print(userId+"已退出")
        else:
            print("密码错误，登录失败")