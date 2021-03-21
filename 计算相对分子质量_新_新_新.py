"""
本程序是为了计算浙教科学八年级下册化学内容设计的
应用内容有：
    1.计算相对分子质量
    2.计算某一个元素在这个物质中的质量分数
    3.计算各个元素在这个物质中的质量的比值
下面介绍一下使用方法：
    1.计算相对分子质量：直接输入需要计算相对分子质量的物质的化学式即可
    2.计算某一个元素在这个物质中的质量分数：
        首先输入一个横杠(减号)，然后跟着输入需要计算质量分数的元素符号。例如 -Ca,-C等等。
        接着空格，输入化学式。
    3.计算各个元素在这个物质中的质量的比值
        在开头输入两个横杠，然后空格，再输入需要计算的化学式即可。
    举几个例子：
        计算Ca在CaCO3中的质量分数：
            -Ca CaCO3
        计算CH4中碳氢元素的质量比值：
            --CH4
        计算碳酸氢铵中个元素的质量比：
            --NH4HCO3
        计算碳酸钙的相对分子质量：
            CaCO3
        计算铁元素在四氧化三铁中的质量分数：
            -Fe Fe3O4
    还有一个注意事项：
        本程序暂不支持带离子团的物质输入（不支持括号）。
        在需要计算离子团物质时拆分输入，如Ca(OH)2请输入CaO2H2
开发者：xht
邮箱：qwertyuiop8350@163.com
"""

ar = {
    'H': 1,
    'He': 4,
    'Li': 7,
    'Be': 9,
    'B': 11,
    'C': 12,
    'N': 14,
    'O': 16,
    'F': 19,
    'Ne': 20,
    'Na': 23,
    'Mg': 24,
    'Al': 27,
    'Si': 28,
    'P': 31,
    'S': 32,
    'Cl': 35.5,
    'Ar': 40,
    'K': 39,
    'Ca': 40,
    'Sc': 45,
    'Ti': 48,
    'V': 51,
    'Cr': 52,
    'Mn': 55,
    'Fe': 56,
    'Co': 59,
    'Ni': 59,
    'Cu': 64,
    'Zn': 65,
    'Ag': 108,
    'Au': 197,
    'Hg': 201,
    'Pb': 207,
    'I': 127,
    'Sn': 119,
    'As': 75
}

import re

def bizhiyuejian(a):  # 比值约简
    max1 = max(a)
    flag = True
    i = 2
    while i <= max1 // 2:
        for index1 in a:
            if index1 % i != 0:
                i += 1
                flag = False
        if flag == True:
            a = [a[index1] // i for index1 in range(len(a))]
    return a

while True:
    huaxveshi = input(">>>化学式 = ")
    if huaxveshi == "esc":
        print("已结束")
        break
    mfsyuansu = ""
    mfsyuansudegeshu = 0
    flag = False
    if huaxveshi[0] == "-":
        if huaxveshi[1] == "-":
            yuansulist = []
            yuansugeshulist = []
            flag = True
            huaxveshi = huaxveshi[2:]
        else:
            flag = False
            mfsyuansu = re.search(r'-[A-Z][a-z]? ', huaxveshi)
            huaxveshi = huaxveshi[mfsyuansu.end():]
            mfsyuansu = mfsyuansu.group()[1:-1]
    yuansujiashuzi = re.findall(r'[A-Z][a-z]?\d*', huaxveshi)
    xiangduifenzizhiliang = 0; guocheng = ""
    for _ in yuansujiashuzi:
        yuansufuhao = re.search(r'^[A-Z][a-z]?', _).group()
        geshu = 1 if yuansufuhao == _ else int(_[len(yuansufuhao):])
        if flag == True:
            if yuansufuhao not in yuansulist:
                yuansulist.append(yuansufuhao)
                yuansugeshulist.append(geshu)
            else:
                yuansugeshulist[yuansulist.index(yuansufuhao)] += geshu
        if yuansufuhao == mfsyuansu:
            mfsyuansudegeshu += geshu
        xiangduifenzizhiliang += ar[yuansufuhao] * geshu
        guocheng += str(str(ar[yuansufuhao]) + " * " + str(geshu) + " + ")
    print("<<<相对分子质量 =", guocheng[:-3], "=", xiangduifenzizhiliang)
    if mfsyuansu != '':
        zhiliangfenshu = ar[mfsyuansu] * mfsyuansudegeshu / xiangduifenzizhiliang
        print('<<<', mfsyuansu, '在', huaxveshi, '中的质量分数 =',
              ar[mfsyuansu], '*', mfsyuansudegeshu,
              '/', xiangduifenzizhiliang, '=', zhiliangfenshu, '=',
              str(zhiliangfenshu * 100) + '%')
    if flag == True:
        yuansuzhilianglist = [yuansugeshulist[index1] * ar[yuansulist[index1]] for index1 in range(len(yuansulist))]
        zuijianbizhiyuejianlist = bizhiyuejian(yuansuzhilianglist)
        printyuansu = ""
        for each in yuansulist:
            printyuansu += "m[" + each + "] : "
        printyuansu = printyuansu[: -2] + "= "
        for index1 in range(len(yuansulist)):
            printyuansu += "(" + str(ar[yuansulist[index1]]) + " * " + str(yuansugeshulist[index1]) + ") : "
        printyuansu = printyuansu[: -2] + "= "
        for each in zuijianbizhiyuejianlist:
            printyuansu += str(each) + " : "
        printyuansu = printyuansu[: -3]
        print("<<<%s中各个元素的质量比:" % huaxveshi, printyuansu)