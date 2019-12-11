import os

# mypath=r'F:\Wallpaper'
while 1:
    mypath=input("请输入路径\n")
    if os.path.isdir(mypath):
        break
    else:
        print("路径无效请重新输入！")
files=os.listdir(mypath)

suf=input("请输入要统一变成的后缀名\n")
suffixe="."+suf

for f in files:
    oldfile=os.path.join(mypath,f)
    file_split=f.split('.')
    if len(file_split)>2:#if file_split[2]:
        midfile=os.path.join(mypath,file_split[0])
        os.rename(oldfile,midfile)
        oldfile=midfile
        f=file_split[0]
    if f.endswith(suffixe):
        print(f+"无需重命名")
        pass
    else:
        f=file_split[0]#如果没有这句的话就会出现 1.aaa 命名后缀为.bbb，就会被命名为1.aaa.bbb。
        newf=f+suffixe
        newfile=os.path.join(mypath,newf)
        os.rename(oldfile,newfile)
        print(newf+"重命名完成")

os.system('pause')
