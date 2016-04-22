#coding=GBK
lie = list(input("请输入数据并用‘，’隔开:"))
sou = 1
print "这是统计应用程序"
while 2:
    a = raw_input("请输入（-h以寻求帮助）:")
    if a == "-q":break
    elif a == "-h":
        print "\n","参数介绍:","\n","-q  结束运算退出程序","\n","-t  改变统计项元素","\n","-s  对数列从小到大排列","\n","-d  对数列从大到小排列","\n","-x  求列表中的项","\n","-l  打印已输入的列表", "\n","-p  求列表平均数","\n","-z  求列表中数的总和","\n","-j  求数列极差","\n","-f  求列表标准差","\n","-b  求列表的中位数","\n","-m  清除数据","\n"
    elif a == "-t":
        try:
            aa = int(raw_input("要改变的项数:"))
            bb = float(raw_input("新的数:"))
            lie[aa-1] = bb
        except:
            print"Error!"
    elif a == "-s":
        avf = lie[:]
        avf.sort()
        print avf
    elif a == "-d":
        dvf = lie[:]
        dvf.sort(reverse = True)
        print dvf
    elif a == "-x":
        en = len(lie)
        print "列表中共有",en,"项"
    elif a == "-l":
        print lie
    elif a == "-p":
        if len(lie) >= 1:
            print "平均数为:", sum(lie)/len(lie)
        else:
            print "Error!"
    elif a == "-z":
        print "总和", sum(lie)
    elif a == "-j":
        coue = lie[:]
        coue.sort()
        couea = coue[0]
        coueb = coue[len(coue)-1]
        print
        print "最大值", coueb
        print "最小值", couea
        print "极差", coueb-couea
        print
    elif a == "-f":
        if len(lie) >= 1:
            import math
            bang = []
            fangping = sum(lie)/len(lie)
            fangxiang =  len(lie)
            for fan in lie:
                jia = (fan-fangping)**2
                bang.append(jia)
            fan1 = sum(bang)/fangxiang
            print "标准差", math.sqrt(fan1)
        else:
            print "Error!"
    elif a == "-b":
        o_lies = len(lie)
        o_j = len(lie) % 2
        o_a = len(lie) / 2
        looei = lie[:]
        if o_j == 1:
            looei.sort()
            print "中位数为:",looei[o_a]
        else:
            looei.sort()
            liea = looei[o_a-1]
            lieb = looei[o_a]
            print "中位数为:",(liea+lieb)/2
    elif a == "-m":
        print "程序已初始化!"
        print
        lie = []
        sou = 1

    else:
        try:
            b = float(a)
            print "#" + str(sou),"  ", b
            sou = sou +1
            lie.append(b)
        except:
            print "Error!"
    print
    print "输入任意键开始运算"
    raw_input()
