def main_menu():
    print("\n==== 主菜单 ====")
    print("1. 查看用户信息")
    print("2. 浏览商品")
    print("3. 设置")
    print("4. 退出")
    choice = input("请选择一个选项（1-4）：")
    return choice

def user_info():
    print("\n---- 用户信息 ----")
    print("用户名：张三")
    print("账户余额：￥100.00")
    print("返回主菜单中...\n")
    input("按回车键返回主菜单...")

def browse_products():
    print("\n---- 商品列表 ----")
    print("1. 商品 A - ￥50.00")
    print("2. 商品 B - ￥30.00")
    print("3. 商品 C - ￥20.00")
    print("返回主菜单中...\n")
    input("按回车键返回主菜单...")

def settings():
    print("\n---- 设置 ----")
    print("1. 修改密码")
    print("2. 切换语言")
    print("返回主菜单中...\n")
    input("按回车键返回主菜单...")

def main():
    while True:
        choice = main_menu()
        if choice == '1':
            user_info()
        elif choice == '2':
            browse_products()
        elif choice == '3':
            settings()
        elif choice == '4':
            print("\n谢谢使用，程序退出。")
            break
        else:
            print("\n无效选项，请重新选择！")

if __name__ == "__main__":
    main()
