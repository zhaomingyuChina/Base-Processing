def tmshort (A , G , C , T):
    tm = 2*(A + T)+4*(C + G)
    return 'Tm值为{}℃'.format(tm)
def tmlong (A , G , C , T):
    tm = 64.9 + (41 * (G + C - 16.4)) / (A + T + G + C)
    return 'Tm值为{}℃'.format(tm)
def main (str,option):
    upstr = str.upper()
    hubustr = ''
    num = 0
    if option == 4:
        A = G = C = T = 0
        for i in upstr:
            num +=1
            if i == 'A' :
                A += 1
            elif i == 'G' :
                G += 1
            elif i == 'C' :
                C += 1
            elif i == 'T' :
                T += 1
            else :
                return '第{}个碱基输入错误，请检查后重新输入'.format(num)
        if len(upstr) < 14:
            return tmshort (A , G , C , T)
        else :
            return tmlong (A , G , C , T)
    for i in upstr:
        num +=1
        if i == 'A' :
            hubustr += 'T'
        elif i == 'G' :
            hubustr += 'C'
        elif i == 'C' :
            hubustr += 'G'
        elif i == 'T' :
            hubustr += 'A'
        else :
            return '第{}个碱基输入错误，请检查后重新输入'.format(num)
    if option == 1:
        return '互补序列为',hubustr
    elif option == 2:
        return '反向序列为',upstr[::-1]
    elif option == 3:
        return '反向互补序列为',hubustr[::-1]
    else :
        return '序号输入有误，请重新运行'
while True:
    a = input('请将碱基序列粘贴至此后回车,输入quit退出')
    if a.upper() == 'QUIT':
        break
    option = int(input('请选择执行的操作，输入序号后回车：1.互补序列 2.反向序列 3.反向互补序列 4.Tm值计算'))
    print (main(a,option))



