#coding=GBK
lie = list(input("���������ݲ��á���������:"))
sou = 1
print "����ͳ��Ӧ�ó���"
while 2:
    a = raw_input("�����루-h��Ѱ�������:")
    if a == "-q":break
    elif a == "-h":
        print "\n","��������:","\n","-q  ���������˳�����","\n","-t  �ı�ͳ����Ԫ��","\n","-s  �����д�С��������","\n","-d  �����дӴ�С����","\n","-x  ���б��е���","\n","-l  ��ӡ��������б�", "\n","-p  ���б�ƽ����","\n","-z  ���б��������ܺ�","\n","-j  �����м���","\n","-f  ���б��׼��","\n","-b  ���б����λ��","\n","-m  �������","\n"
    elif a == "-t":
        try:
            aa = int(raw_input("Ҫ�ı������:"))
            bb = float(raw_input("�µ���:"))
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
        print "�б��й���",en,"��"
    elif a == "-l":
        print lie
    elif a == "-p":
        if len(lie) >= 1:
            print "ƽ����Ϊ:", sum(lie)/len(lie)
        else:
            print "Error!"
    elif a == "-z":
        print "�ܺ�", sum(lie)
    elif a == "-j":
        coue = lie[:]
        coue.sort()
        couea = coue[0]
        coueb = coue[len(coue)-1]
        print
        print "���ֵ", coueb
        print "��Сֵ", couea
        print "����", coueb-couea
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
            print "��׼��", math.sqrt(fan1)
        else:
            print "Error!"
    elif a == "-b":
        o_lies = len(lie)
        o_j = len(lie) % 2
        o_a = len(lie) / 2
        looei = lie[:]
        if o_j == 1:
            looei.sort()
            print "��λ��Ϊ:",looei[o_a]
        else:
            looei.sort()
            liea = looei[o_a-1]
            lieb = looei[o_a]
            print "��λ��Ϊ:",(liea+lieb)/2
    elif a == "-m":
        print "�����ѳ�ʼ��!"
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
    print "�����������ʼ����"
    raw_input()
