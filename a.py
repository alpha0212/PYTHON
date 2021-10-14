import os
import random
import string
se = "".join([random.choice(string.ascii_letters)for _ in range(4)])
menu = {}
print("보안문자:",se)
S = input("보안문자를 입력하세요 >")
if S == se:
    print("프로그램 접근 성공")
    flag = True
    while flag:
        print("============================")
        print("1.유저등록")
        print("2.유저목록")
        print("3.유저수정")
        print("4.로그인")
        print("5.프로그램 종료")
        print("============================")
        num = int(input("번호선택 >>")) 
        if num == str:
            flag=True
        elif num == 1: 
            name = input("USER ID 입력: ") 
            if menu.get(name) == None: 
                menu[name] = input("PASSWORD 입력: ") 
            else:
                print("입력하신 ID는 이미 존재합니다.")
        elif num == 2:
            for k,v in menu.items(): 
                print("ID:{} - PW:{}".format(k,v))

        elif num == 3:
            name = input("PW수정 할 유저이름 입력: ")
            if menu.get(name) == None:
                print("입력하신 유저는 등록되지 않았습니다.")
            else: 
                menu[name] = input("새로운 PASSWORD 입력: ")
                print("수정 완료")

        elif num == 4:
            id = input("아이디를 입력해주세요 >")
            if id == menu['admin']:
                pw = input("비밀번호를 입력해주세요 >")

            elif id == name:
                pw = input("비밀번호를 입력해주세요 >")
                if pw == menu[name]:
                    print("로그인 되었습니다.")
    

        elif num == 5:
            flag = False
            print("프로그램 종료")

            

        else:
            print("번호를 다시 입력해주세요.")

        os.system("pause")
        os.system("cls")
else:
    print("보안문자가 일치하지 않습니다.")
