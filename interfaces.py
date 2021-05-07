print("----------------------------------------------")
print("UTS APLIKASI BERBASIS JARINGAN - 1810530202")
print("----------------------------------------------")


file=open("db-interfaces.txt","a")
while True :
    Answer = input("Input Data Trunk? [yes/no] : ")
    if Answer == "yes" :
        print('-'*34)
        x = input("Masukan Hostname Switch: ")
        y = input("Masukan Nama Interfaces: ")
        print('-'*34)
        file.write('Hostname Switch : '+x+','' Name: '+y+'\n')
    else :
        print('='*34)
        print('-'*13 +'  DONE  '+'-'*13)
        print('='*34)
        file=open('db-interfaces.txt','r')
        for item in file:
            item=item.strip()
            print(item)
        file.close()
        break
print('='*34)
file.close()