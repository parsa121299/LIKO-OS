#LIKO OS Terminal edition with hack options
#repository: http://github.com/parsa121299/LIKO-OS
#Thanks for your star in github 
#your stars=you can see a new release
#made by LIKO for you
#Rubika: @liko_entertainment
#github: parsa121299
import time
import os
apps='calc','browser','files','py','git'
print('SYSTEM BOOT')
time.sleep(1)
print('CHECKING SYSTEM...')
time.sleep(1)
if not os.path.exists(os.getcwd()):
    print('BOOT ERROR!!!!!!!!!')
    exit()
print('SYSTEM OK FOR READY.. . .')
time.sleep(1)
print('STARTING LIKO OS. . .')
time.sleep(3)
print("""
       LLLLLLLLL           IIIIIIIIII    KKKK     KKKK
       LLLLLLLLL              IIII       KKKK   KKKKK
       LLLLLLLLL              IIII       KKKK  KKKK   
       LLLLLLLLL              IIII       KKKKKKKK         000000000000
       LLLLLLLLL              IIII       KKKKKKKKKK       000      0000
       LLLLLLLLL              IIII       KKKK  KKKKK     000         000
       LLLLLLLLLLLLLLLL       IIII       KKKK   KKKKK    OOO         OOO
       LLLLLLLLLLLLLLLL       IIII       KKKK    KKKKK    OOOO     OOOO
       LLLLLLLLLLLLLLLL    IIIIIIIIII    KKKK      KKKK     OOOOOOOOO  

                                           TERMINAL EDITION
       """)
print("Terminal LIKO OS system")
print("LOGIN")
files= ''
folders= 'system','programs'
give_password=input("Enter your first password: ")
password= give_password
for i in range(3):
    question=input("Enter your password. . . : ")
    if question == password:
        print('welcome')
    else:
        print('YOU ARE NOT A USER!!!!!!BYE. . . .')
        break
    print("""
       LLLLLLLLL           IIIIIIIIII    KKKK     KKKK
       LLLLLLLLL              IIII       KKKK   KKKKK
       LLLLLLLLL              IIII       KKKK  KKKK   
       LLLLLLLLL              IIII       KKKKKKKK         000000000000
       LLLLLLLLL              IIII       KKKKKKKKKK       000      0000
       LLLLLLLLL              IIII       KKKK  KKKKK     000         000
       LLLLLLLLLLLLLLLL       IIII       KKKK   KKKKK    OOO         OOO
       LLLLLLLLLLLLLLLL       IIII       KKKK    KKKKK    OOOO     OOOO
       LLLLLLLLLLLLLLLL    IIIIIIIIII    KKKK      KKKK     OOOOOOOOO  
       """)
    print('MAIN TERMINAL MENU')
    from time import sleep
    sleep(4)
    computer_do=input('what do you want to the computer or mobile to do?')
    if computer_do == 'calc':
        print('LIKO OS calculator')
        calc=input('what do you want the calculator to do? ')
        if calc == '*':
            c=int(input())
            d=int(input())
            print(c * d)
        elif calc=='+':
            c2=int(input())
            d2=int(input())
            print(c2 + d2)
        elif calc=='/':
            c3=int(input())
            d3=int(input())
            print(c3 / d3)
        elif calc=='-':
            c4=int(input())
            d4=int(input())
            print(c4 - d4)
        elif calc=='//':
            c5=int(input())
            d5=int(input())
            print(c5 // d5)
        elif calc=='**':
            c6=int(input())
            d6=int(input())
            print(c6 ** d6)
        else:
            print('ERRORRRRRRRRRJFJBNGJBGNBJGNBJGBNGJBMNFKSMREGMEFIOGJERBNJEJKIFJHRTUJTU')
            import secrets
            print(secrets.token_hex(100000))
            continue
    elif computer_do == 'systeminfo':
        print('wating. . . .')
        sleep(5)
        import os
        print('OS:',os.name)
        print('CPU:',os.cpu_count())
        print('DIRECTORY:',os.getcwd())
        print('FILES:',os.listdir())
        print('USERNAME:',os.getlogin())
        import platform
        print(platform.system())
        print(platform.release())
        print(platform.version())
        print(platform.machine())
        print(platform.processor())
    elif computer_do=='createfile':
        want1=input('FileName: ')
        files=want1
        for infile in range(999):
               infile=input("")
               if infile=='END':
                   continue
    elif computer_do=='help':
        print('searching commands...')
        sleep(3)
        print('systeminfo,calc,createfile,curl,files,browse,games,reboot,apps,gitclone')
    elif computer_do=='browse':
        import urllib.request
        from html.parser import HTMLParser
        import socket
        url=input('Your website URL: ')
        if not url.startswith("http"):
            url='https://'+url
        try:
            socket.create_connection(('1.1.1.1', 443), timeout=3)
            request=urllib.request.Request(
                url,
                headers={'User-Agent': 'Mozilla/5.0'}
            )
            response=urllib.request.urlopen(request, timeout=10)
            html=response.read(2000000).decode('utf-8', errors='replace')
            class Reader(HTMLParser):
                def __init__(self):
                    super().__init__()
                    self.show=True
                def handle_starttag(self, tag, attrs):
                        if tag in ('script', 'style'):
                           self.show=False
                def handle_endtag(self, tag):
                    if tag in('script', 'style'):
                        self.show=True
                def handle_data(self, data):
                    if self.show and data.strip():
                        print(data.strip())
            browser=reader()
            browser.feed(html)
            response.close()
        except OSError:
            print('NO INTERNET CONNECTION!')
            print('BROWSE STOPPED!')
        except Exception as error:
            print('BROWSER ERROR:', error)
    elif computer_do=='curl':
        import urllib.request
        url=input('enter your url: ')
        if not url.startswith(('http://', 'https://')):
            url='https://'+url
        try:
            request=urllib.request.Request(
                url,
                headers={'User-Agent': 'LIKO-OS/1.0'}
            )
            response=urllib.request.urlopen(request, timeout=10)
            print('\n======CURL RESPONSE======')
            print('STATUS:',response.status)
            print('CONTENT TYPE:',response.headers.get('CONTENT-TYPE'))
            print('FINAL URL:', response.url)
            data=response.read(100000)
            print('\n======RESPONSE BODY======')
            print(data.decode('utf-8' , errors='replace'))
            response.close()
        except Exception as error:
            print('CURL ERROR:', error)
    elif computer_do=='files':
        print('FILES:',files)
    elif computer_do=='games':
        #You can create your game on this Terminal and put your code in codea part of games part in code.
        print('You can create your game on this Terminal and put your code in codea part of games part in code.')
        sleep(1)
        print('Waiting. . .')
        sleep(3) 
        games='guess the number'#you can add a game and coding your game
        question2=input('do you want to play games? ')
        if question2=='no':
            input('are you sure?')
            print("OK")
            from time import sleep
            sleep(2)
        elif question2=='yes':
            print('Games:',games)
            wantforgames=input('what do you want to play? ')
            if wantforgames=='guess the number':
                import random
                numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
                print('''
                           ???????????????????
                           ???????????????????
                                     ?????????
                                     ?????????
                                     ?????????
                                    ????????
                                    ?????
                                ???????
                                ???????
                               ???????

                               ???????
                               ???????
                               ???????

                               __________guess the number game__________made by LIKO
                ''')
                sleep(1)
                print('numbers are 1-20')
                sleep(1)
                print('you have 3 tries. . .')
                sleep(1)
                answer=random.choice(numbers)
                for q in range(3):
                   whq=input('what is the number?')
                   if whq==answer:
                       print('you won!the correct answer is',answer+'!')
                       yn=input('exit? [y | n]')
                       if yn=='y'or'Y':
                           continue
                       else:
                           continue
                   else:
                       print('LOSE!')
                       sleep(1)
                       continue
            else:
                print('If you don`t coding your game please coding.')
    elif computer_do=='apps':
        print(apps)
    elif computer_do=='reboot':
        print('SYSTEM BOOT')
        time.sleep(1)
        print('CHECKING SYSTEM...')
        time.sleep(1)
        if not os.path.exists(os.getcwd()):
              print('BOOT ERROR!!!!!!!!!')
              exit()
        print('SYSTEM OK FOR READY.. . .')
        time.sleep(1)
        print('STARTING LIKO OS. . .')
        time.sleep(3)
        continue
    elif computer_do=='token hex':
        import secrets
        print(secrets.token_hex(100000))
    elif computer_do=='system error':
        import time
        for error in range(4):
           print('Checking system...')
           sleep(1)
           print('AN ERROR...')
           sleep(1)
           print('Restarting os...')
           if error >2:
              print('OS')
              break
    else:
        print(computer_do,': command not found. . . .')
        print('type help for all commands')