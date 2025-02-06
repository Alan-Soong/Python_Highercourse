import re

user = {}
# username_pattern = re.compile(r'[A-Za-z0-9_]+$')
email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
password_pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')


def judge_email(email):
    return email_pattern.match(email) is not None


def judge_password(password):
    return password_pattern.match(password) is not None


def user_register():
    print("注册信息")
    while True:
        username = input("请输入用户名：")
        if username in user:
            print("用户名已存在！请输入一个新的用户名！")
            continue
        else:
            break

    while True:
        email = input("请输入注册邮箱：")
        if not judge_email(email):
            print("格式错误！请输入正确的邮箱格式！")
            continue
        else:
            break

    while True:
        print("请确保密码至少8个字符，且包含大写字母、小写字母、数字和特殊字符。")
        password = input("请输入密码：")
        if not judge_password(password):
            print("密码复杂度不符合要求，请确保密码至少8个字符，且包含大写字母、小写字母、数字和特殊字符。")
            continue
        else:
            break

    while True:
        passwords = input("请再次输入密码：")
        if passwords != passwords:
            print("第二次密码输入错误！请重新输入！")
            continue
        else:
            break


    user[username] = {"email": email, "password": password}
    print("用户已成功注册！")

    return


def user_login():
    print("登录信息")
    while True:
        un = input("请输入用户名：")
        if un not in user:
            print("用户名不存在！请重新输入！")
            continue
        else:
            break

    while True:
        pw = input("请输入密码：")
        if pw == user[un]["password"]:
            print("欢迎回来！" + un)
            break
        else:
            print("密码错误！请重新输入！")
            continue

    return


def userpw_change():
    while True:
        un = input("请输入用户名：")
        if un not in user:
            print("用户名不存在！请重新输入！")
            continue
        else:
            break

    while True:
        pw = input("请输入密码：")
        if pw != user[un]["password"]:
            print("密码错误！请重新输入！")
            continue
        else:
            break

    while True:
        new_pw = input("请输入新密码：")
        if not judge_password(new_pw):
            print("密码复杂度不符合要求，请确保密码至少8个字符，且包含大写字母、小写字母、数字和特殊字符。")
            continue
        else:
            break

    while True:
        new_pw0 = input("请再次输入新密码：")
        if new_pw == new_pw0:
            user[un]["password"] = new_pw
            print("密码已经修改！")
            break
        else:
            print("输入错误！请重新输入！")
            continue

    return


def usernm_change():
    while True:
        un = input("请输入用户名：")
        if un not in user:
            print("用户名不存在！请重新输入！")
            continue
        else:
            break

    nm = input("请输入新的用户名：")
    user[nm] = {"email": user[un]['email'], "password": user[un]['password']}
    del user[un]
    print("用户名已修改！")
    return


if __name__ == "__main__":
    while True:
        opt = int(input("请输入选择："))
        if opt == 1:
            user_register()
        if opt == 2:
            userpw_change()
        if opt == 3:
            user_login()
        if opt == 4:
            usernm_change()
        if input("是否继续？") != 'y':
            break
