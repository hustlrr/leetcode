# coding=utf-8

# Created by lruoran on 16-12-21

# 从配置文件中读取leetcode账号的用户名和密码\编程语言
username, password = None, None
language = None
with open(r'configure/user_pass') as fr:
    lines = fr.readlines()
    username = lines[0].strip()
    password = lines[1].strip()
    language = lines[2].strip()
# 模拟登录
from selenium import webdriver

driver = webdriver.PhantomJS(r'/home/lruoran/software/phantomjs/bin/phantomjs')
driver.get('https://leetcode.com/accounts/login/')
elem_username = driver.find_element_by_name('login')
elem_username.send_keys(username)
elem_keywords = driver.find_element_by_name('password')
elem_keywords.send_keys(password)
elem_login_button = driver.find_element_by_xpath(r"//button[@type='submit']")
elem_login_button.click()
print('sign in successfully')

# 过滤得到已经解决的问题
driver.find_element_by_xpath(r"//select[@class='form-control']").send_keys("Solved Problems")
# 为了避免翻页，在第一页显示所有问题
driver.find_element_by_xpath(r"//span[@class='row-selector']/select[@class='form-control']").send_keys("all")
# 得到所有solved问题的url
question_url_list = []
question_name_list = []
num_of_questions = 0
for q in driver.find_elements_by_xpath(r"//table[@class='table table-striped']//tbody[@class='reactable-data']//tr"):
    url = q.find_element_by_xpath(r"td[3]//a").get_attribute("href") + '/submissions/'
    question_url_list.append(url)
    question_name_list.append(q.find_element_by_xpath(r"td[3]//a").text)
    # print(url)
    num_of_questions += 1
print('number of solved problem: %d' % num_of_questions)

# 得到所有已经解决的问题的submission_url，即包含提交的代码的页面
idx = 1
for file_name, q_url in zip(question_name_list, question_url_list):
    driver.get(q_url)
    # 过滤到语言不相符的题目
    if driver.find_element_by_xpath(r"//div[@class='table-responsive']//tr/td[5]").text != language:
        print driver.find_element_by_xpath(r"//div[@class='table-responsive']//tr/td[5]").text, file_name
        continue

    elem = driver.find_element_by_xpath(r"//div[@class='table-responsive']//a[@class='status-accepted text-success']")
    s_url = elem.get_attribute("href")
    # 生成python文件
    driver.get(s_url)
    codes = []
    for elem in driver.find_elements_by_xpath(r"//div[@class='ace_line_group']"):
        codes.append(elem.text.replace('\n', ''))
    from generate_pyfile import remove_redundant_blank

    with open('accepted/' + file_name.strip() + '.py', 'w') as fw:
        fw.write("# coding=utf-8\n")
        fw.write(remove_redundant_blank(codes).encode('utf-8') + '\n')
        # print remove_redundant_blank(codes)
    print(idx, file_name)
    idx += 1