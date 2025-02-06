import re
import sys

# 用户信息存储字典
users = {}

# 电子邮件正则表达式
email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

# 密码复杂度正则表达式
password_pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')

# 可接受的域名，用户可以自行添加
allowed_domains = ["126.com", "163.com", "qq.com", "sohu.com"
                   "nankai.edu.cn", "mail.nankai.edu.cn",
                   "gmail.com", "sina.com", "outlook.com"]

# # 判断邮箱是否有效
# def is_valid_email(email):
#     """验证电子邮件格式是否正确"""
#     return email_pattern.match(email) is not None

# 判断邮箱是否有效
def is_valid_email(email):
    """验证电子邮件格式是否正确"""
    if not email_pattern.match(email):
        return False
    domain = email.split('@')[1]
    return domain in allowed_domains


# 判断密码是否有效
def is_valid_password(password):
    """验证密码复杂度是否符合要求"""
    return password_pattern.match(password) is not None


# 用户名输入
def username_input():
    while True:
        username = input("请输入用户名：")
        if username in users:
            print("用户名已存在！请输入一个新的用户名！")
            continue
        else:
            break
    return username


# 邮箱输入
def email_input():
    while True:
        email = input("请输入注册邮箱：")
        if not is_valid_email(email):
            print("格式错误！请输入正确的邮箱格式！")
            continue
        else:
            break
    return email


# 密码输入
def password_input():
    regret = 'p'
    while True:
        print("请确保密码至少8个字符，且包含大写字母、小写字母、数字和特殊字符。")
        password = input("请输入密码：")
        if not is_valid_password(password):
            print("密码复杂度不符合要求，请确保密码至少8个字符，且包含大写字母、小写字母、数字和特殊字符。")
            continue
        else:
            while True:
                passwords = input("请再次输入密码：")
                if passwords != password:
                    print("第二次密码输入错误！请重新输入！")
                    regret = input("是否想修改第一次密码？[y/n]")
                    if regret == "y":
                        break
                    else:
                        continue
                else:
                    break
            if regret != "y":
                break
            else:
                continue
    return password


# 验明正身
def identify_input():
    while True:
        un = input("请输入登录用户名：")
        if un not in users:
            print("用户名不存在！请重新输入！")
            continue
        else:
            break

    while True:
        pw = input("请输入密码：")
        if pw != users[un]["password"]:
            print("密码错误！请重新输入！")
            continue
        else:
            break

    return un, pw


# 确认操作
def confirm_opt():
    con = input("是否确认操作？[y/n]")
    if con == "y":
        return True
    else:
        return False


# 注册用户信息的函数
def register_user():
    """用户注册函数"""
    print("注册信息")

    username = username_input()
    email = email_input()
    password = password_input()

    # 存储用户信息
    users[username] = {'email': email, 'password': password}
    save_user_data()
    print("用户注册成功！")


# 登录用户账号的函数
def login_user():
    """用户登录的函数"""
    print("登录账户")

    un, pw = identify_input()

    print("欢迎回来！" + un)
    return


# 注销用户账号的函数
def cancel_user():
    """用户注销函数"""
    print("注销账户")

    un, pw = identify_input()

    if confirm_opt():
        del users[un]
        print("用户已注销！")
        save_user_data()
    else:
        print("已退出，请重新选择！")

    return


# 修改用户密码的函数
def password_change_user():
    """用户改密函数"""
    print("修改密码")

    un, pw = identify_input()

    while True:
        new_pw = input("请输入新密码：")
        if not is_valid_password(new_pw):
            print("密码复杂度不符合要求，请确保密码至少8个字符，且包含大写字母、小写字母、数字和特殊字符。")
            continue
        else:
            break

    while True:
        new_pw0 = input("请再次输入新密码：")
        if new_pw == new_pw0:
            users[un]["password"] = new_pw
            print("密码已经修改！")
            save_user_data()
            break
        else:
            print("输入错误！请重新输入！")
            continue

    return


# 修改用户账号的函数
def username_change_user():
    """用户改名函数"""
    print("修改名字")

    un, pw = identify_input()

    nm = input("请输入新的用户名：")
    if confirm_opt():
        users[nm] = {"email": users[un]['email'], "password": users[un]['password']}
        del users[un]
        print("用户名已修改！")
        save_user_data()
    else:
        print("已退出，请重新选择！")
    return


# 修改用户邮箱的函数
def email_change_user():
    """用户改邮函数"""
    print("修改邮箱")

    un, pw = identify_input()

    while True:
        new_em = input("请输入新邮箱：")
        if not is_valid_email(new_em):
            print("密码复杂度不符合要求，请确保密码至少8个字符，且包含大写字母、小写字母、数字和特殊字符。")
            continue
        if new_em == users[un]['email']:
            print("邮箱重复！请重新输入！")
            continue
        else:
            if confirm_opt():
                users[un]["email"] = new_em
                print("邮箱已经修改！")
                save_user_data()
            else:
                print("操作不确认，已退出！")
            break


# 从文件读取已注册用户信息的函数
def load_user_data():
    try:
        with open('users_data.txt', 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    username, email, password = parts
                    users[username] = {'email': email, 'password': password}
    except FileNotFoundError:
        print("用户数据文件不存在，将创建新文件。")
    except Exception as e:
        print(f"读取用户数据文件时出现错误: {e}")


# 将当前用户信息保存到文件的函数
def save_user_data():
    print("保存中……")
    try:
        with open('users_data.txt', 'w') as file:
            for username, info in users.items():
                file.write(f"{username},{info['email']},{info['password']}\n")
            print("保存成功！")
    except Exception as e:
        print(f"保存用户数据文件时出现错误: {e}")


if __name__ == "__main__":
    try:
        # 启动时读取用户数据
        load_user_data()

        while True:
            print("1、注册用户")
            print("2、登录用户")
            print("3、注销用户")
            print("4、修改密码")
            print("5、修改名字")
            print("6、修改邮箱")

            opt = int(input("请输入你的选择："))
            if opt == 1:
                register_user()
            if opt == 2:
                login_user()
            if opt == 3:
                cancel_user()
            if opt == 4:
                password_change_user()
            if opt == 5:
                username_change_user()
            if opt == 6:
                email_change_user()
            if input("是否继续？[y/n]") != 'y':
                break

        # 结束时保存用户数据
        save_user_data()

    except KeyboardInterrupt:
        print("\n程序被用户中断，正在保存用户数据...")
        save_user_data()
        sys.exit(0)
