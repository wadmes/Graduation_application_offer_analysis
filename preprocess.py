import csv
import codecs
import pandas as pd
import seaborn as sns
import numpy as np
import pylab as p
from matplotlib import pyplot as plt
#SRC = source csv, DB= delete_blank csv, FINAL = final resultcsv
SRC = 'offer.csv'
DB = 'delete_blank.csv'
FINAL = 'final.csv'
strict = ['清华大学','复旦大学','上海交通大学']
nice = ['南京大学','北京大学','浙江大学','中国人民大学']
#Top25 around the world
Top = ['清华大学','北京大学','剑桥大学','牛津大学','伦敦大学学院','帝国理工学院','爱丁堡大学','澳大利亚国立大学','伦敦国王学院','多伦多大学','麦吉尔大学']
#TOp65
Good_School = ['新南威尔士大学','昆士兰大学','悉尼大学','南京大学','复旦大学','浙江大学','武汉大学','上海交通大学','中国人民大学','中国科学技术大学','伦敦政治经济学院','曼彻斯特大学','布里斯托大学','墨尔本大学','华威大学','格拉斯哥大学',]
#Top100
NineEightFive=['都柏林大学','都柏林圣三一学院','奥克兰大学','南安普顿大学','利兹大学','圣安德鲁斯大学','拉夫堡大学','新南威尔士大学',
'英属哥伦比亚大学','代尔夫特理工大学','蒙纳士大学','杜伦大学','谢菲尔德大学','诺丁汉大学','伯明翰大学','清华大学','北京大学','厦门大学',
'南京大学','复旦大学','	天津大学',
'浙江大学','南开大学','西安交通大学',
'东南大学','武汉大学','上海交通大学',
'山东大学','湖南大学','中国人民大学','吉林大学','重庆大学','电子科技大学','四川大学','	中山大学','华南理工大学',
'兰州大学','东北大学','西北工业大学','哈尔滨工业大学','华中科技大学','中国海洋大学','北京理工大学','大连理工大学','北京航空航天大学','北京师范大学','同济大学','中南大学','中国科学技术大学','中国农业大学','国防科学技术大学','中央民族大学','华东师范大学','西北农林科技大学']
#Top
TwoII=['阿德莱德大学','西澳大利亚大学','奥塔哥大学','萨塞克斯大学','巴斯大学','阿伯丁大学','约克大学','伦敦大学玛丽皇后学院','兰卡斯特大学','莫纳什大学','朴次茅斯','伦敦大学皇家霍洛威学院','雷丁大学','萨里大学','剑桥大学','帝国理工学院','牛津大学',
'伦敦大学学院','杜伦大学','华威大学','伦敦政治经济学院','曼彻斯特大学','谢菲尔德大学','波士顿学院','爱丁堡大学','格拉斯哥大学',
'纽卡斯尔大学','伯明翰大学','基尔大学','中央圣马丁','斯特林大学','伦敦时装学院','埃克塞特大学','伦敦大学国王学院','利物浦大学','伦敦大学玛丽女王学院','卡迪夫大学','埃塞克斯大学','诺丁汉大学',
'北京大学','中国人民大学','清华大学','北京交通大学','北京工业大学','北京航空航天大学','北京理工大学','北京科技大学',
'北京化工大学','北京邮电大学','中国农业大学','北京林业大学','北京中医药大学','北京师范大学','北京外国语大学','中国传媒大学','中央财经大学','对外经济贸易大学','北京体育大学','中央音乐学院中央民族大学','中国政法大学',
'华北电力大学','南开大学','天津大学','天津医科大学','河北工业大学','太原理工大学','内蒙古大学','辽宁大学','大连理工大学','东北大学','大连海事大学','吉林大学','延边大学','东北师范大学','哈尔滨工业大学','哈尔滨工程大学','东北农业大学',
'东北林业大学','复旦大学','同济大学','上海交通大学','华东理工大学','东华大学','华东师范大学','上海外国语大学','上海财经大学','上海大学','第二军医大学','南京大学','苏州大学','东南大学','南京航空航天大学','南京理工大学','中国矿业大学',
'河海大学','江南大学','南京农业大学','中国药科大学','南京师范大学','浙江大学','安徽大学','中国科学技术大学','合肥工业大学','厦门大学','福州大学','南昌大学','山东大学','中国海洋大学','中国石油大学',
'郑州大学','武汉大学','华中科技大学','中国地质大学','武汉理工大学','华中农业大学','华中师范大学','中南财经政法大学','湖南大学','中南大学','湖南师范大学','国防科学技术大学','中山大学','暨南大学','华南理工大学','华南师范大学',
'广西大学','海南大学','四川大学','西南交通大学','电子科技大学','四川农业大学','西南财经大学','重庆大学','西南大学','贵州大学','云南大学','西藏大学','西北大学','西安交通大学','西北工业大学','西安电子科技大学','长安大学',
'西北农林科技大学','陕西师范大学','第四军医大学','兰州大学','青海大学','宁夏大学','新疆大学','石河子大学']
#FuDan GPA calculation method
def FD_GPA(IOO):
    return min(4.0,IOO/10.0 -5.0)
#ZHeJiang GPA calculation method
def ZJ_GPA(IOO):
    return min(4.0,IOO/10.0 -4.5)
#detele useless row with blank entry and transfer the GPA
def delete_blank():
    with open(SRC,encoding="utf8") as fread:
        with open(DB,'w',newline='') as fwrite:
            csvfread = csv.reader(fread)
            csvfwrite = csv.writer(fwrite)
            for row in csvfread:
                is_continue = False
                #whether there is a blank entry, if yes, delete the row
                for i in range(4):
                    if row[i] == '':
                        is_continue = True
                        continue
                #whther gpa is a valid num, if 50-100, transfer it into 0-4
                try:
                    row[1] = float(row[1])
                    if row[1] > 50 and row[1] < 100:
                        row[1] = ZJ_GPA(row[1])
                    elif row[1] >0 and row[1] <4:
                        row[1] = row[1]
                    else:
                        is_continue = True
                except:
                    is_continue = True
                if is_continue:
                    continue
                csvfwrite.writerow(row)
#return the index according to the looking-up table, but drop some trick names
def getGOodnumber(str):
    for i in Top:
        if str in i:
            return 4
    for i in Good_School:
        if str in i:
            return 3
    for i in NineEightFive:
        if str in i:
            return 2
    for i in TwoII:
        if str in i:
            return 1
    return 0
#return the index according to the looking-up table
def getnumber(str):
    for i in Top:
        if i in str:
            return 4
    for i in Good_School:
        if i in str:
            return 3
    for i in NineEightFive:
        if i in str:
            return 2
    for i in TwoII:
        if i in str:
            return 1
    return 0

#change school name to the preassigned number
def Change_school_name(src=FINAL):
    with open(DB) as fread:
        with open(src,'w',newline = '') as fwrite:
            csvfread = csv.reader(fread)
            csvfwrite = csv.writer(fwrite)
            count = 0
            for row in csvfread:
                row[0] = getGOodnumber(row[0])
                if row[0] != 0:
                    count += 1
                row[2] = getnumber(row[2])
                row[3] = 1 if row[3] == '申请成功' else 0
                csvfwrite.writerow(row)
            print (count)
#show the correlationships
def show_corr(df):
    f, ax = plt.subplots(figsize=(10, 8))
    corr = df.corr()
    ax.matshow(corr)
    sns.heatmap(corr, vmin=-0.1, vmax=0.2,mask=np.zeros_like(corr, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True, ax=ax)
    plt.show()
#claculate the success per and average gpa of good school's applicant
def multi_histo(df):
    common_params = dict(bins=5, range=(0, 4),normed=True)
    mean = []
    success_gpa = []
    fail_gpa = []
    for i in range(5):
        tmp = df.loc[df['to']==i]
        success_gpa.append(tmp.loc[tmp['success']==1]['gpa'].mean())
        fail_gpa.append(tmp.loc[tmp['success']==0]['gpa'].mean())
        mean.append(tmp['success'].mean())
    label = ['to 0','to 1','to 2','to 3','to 4']
    plt.bar(['to 0','to 1','to 2','to 3','to 4'],mean)
    plt.ylabel('success proportion')
    ax = plt.gca()
    ax2 = ax.twinx()
    ax2.plot(label,success_gpa,'r',label='success gpa')
    ax2.plot(label,fail_gpa,'y',label = 'fail gpa')
    ax2.plot(label,[df['gpa'].mean(),df['gpa'].mean(),df['gpa'].mean(),df['gpa'].mean(),df['gpa'].mean()],'g--',label='mean gpa')
    plt.title('offer information of graduate from 985 or above ')
    plt.legend()
    plt.show()


def basic_info(df):
    #Graduation school distribution
    plt.figure(figsize = (7, 6))
    plt.title('Graduation school distribution')
    labels = ['Top', 'C9', '985','211','others']
    sizes = [len(df.loc[df['from']==4-i]) for i in range(5)]
    colors = ['orange','red','lightskyblue','green','white']
    patches, l_text, p_text = plt.pie(sizes, labels=labels,
                                    labeldistance=1.05, autopct='%3.1f%%',
                                    startangle=90)

    plt.axis('equal')
    plt.legend()
    plt.show()
    #Application school distribution
    plt.figure(figsize = (7, 6))
    plt.title('Application school distribution')
    labels = ['Top25', 'Top65', 'Top100','Top200','others']
    sizes = [len(df.loc[df['to']==4-i]) for i in range(5)]
    colors = ['orange','red','lightskyblue','green','white']
    patches, l_text, p_text = plt.pie(sizes, labels=labels,
                                    labeldistance=1.05, autopct='%3.1f%%',
                                    startangle=90)
    plt.axis('equal')
    plt.legend()
    plt.show()
    #Success bar chart
    plt.title('Success bar chart')
    plt.bar(['fail','success'],[len(df.loc[df['success']==i]) for i in range(2)],color=['red','green'])
    plt.show()

    #GPA attribution
    plt.figure()
    plt.title('GPA distribution')
    binBoundaries = np.linspace(0,4.0,40)
    df['gpa'].hist(bins=binBoundaries)
    plt.xlabel('GPA')
    plt.ylabel('population')
    plt.legend()
    plt.show()
    print('from: ',df['from'].mean(),'to: ',df['to'].mean(),'gpa: ',df['gpa'].mean(),'success: ',df['success'].mean())

#direct relationship between GPA and success
def GPA_success(df,bound=30):
    plt.figure()
    plt.title('GPA and its success distribution')
    binBoundaries = np.linspace(1.0,4.0,bound)
    a = df.loc[df['success']==1]['gpa']
    b = df.loc[df['success']==0]['gpa']
    y,binEdges,c=plt.hist([a,b],binBoundaries,stacked = True,label=['success','fail'])
    print (y)
    bincenters = 0.5*(binEdges[1:]+binEdges[:-1])
    plt.xlabel('GPA')
    plt.ylabel('population')
    ax = plt.gca()
    ax2 = ax.twinx()
    ax2.plot(bincenters,y[1]/(y[1]+y[0]),'-',color='r')
    plt.legend()
    plt.show()
def show_good_corr(df):
    df = df.loc[df['from'].isin(['4','3','2'])]
    show_corr(df)

#keep the school level unchanged
def static_GPA_success(df):
    row = np.zeros((5,5))
    f, ax = plt.subplots(figsize=(10, 8))
    plt.title('Correlation between GPA and Success')
    for i in range(5):
        for j in range(5):
            row[i][j] = df.loc[df['from']==i].loc[df['to']==j].corr()['success']['gpa']
            print (i,j,row[i][j],len(df.loc[df['from']==i].loc[df['to']==j]))
    sns.heatmap(row,vmin=-0.2, vmax=0.2, mask=np.zeros_like(row, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
    square=True, ax=ax, xticklabels=['to 0','to 1','to 2','to 3','to 4'], yticklabels=['from 0','from 1','from 2','from 3','from 4'])
    plt.show()
def static_typical_GPA_success(df):
    row = np.zeros((2,5))
    f, ax = plt.subplots(figsize=(10, 8))
    plt.title('Correlation between GPA and Success')
    for i in range(2):
        for j in range(5):
            row[i][j] = df.loc[df['from']==i].loc[df['to']==j].corr()['success']['gpa']
            print (i,j,row[i][j],len(df.loc[df['from']==i].loc[df['to']==j]))
    sns.heatmap(row,vmin=-0.2, vmax=0.2, mask=np.zeros_like(row, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
    square=True, ax=ax, xticklabels=['to 0','to 1','to 2','to 3','to 4'], yticklabels=['from 0','from 1'])
    plt.show()

def static_FROM_success(df):
    row = np.zeros((5,5))
    f, ax = plt.subplots(figsize=(10, 8))
    plt.title('Correlation between Graduation school and Success')
    for i in range(5):
        for j in range(5):
            row[i][j] = df.loc[df['gpa'].between(3.5 - 0.5 * i, 4.0 - 0.5*i)].loc[df['to']==j].corr()['success']['from']
            print (i,j,row[i][j],len(df.loc[df['gpa'].between(3.5 - 0.5 * i, 4.0 - 0.5*i)].loc[df['to']==j]))
    sns.heatmap(row, vmin=-0.2, vmax=0.2,mask=np.zeros_like(row, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
    square=True, ax=ax, yticklabels=['to 0','to 1','to 2','to 3','to 4'], xticklabels=['3.5-4.0','3.0-3.5','2.5-3.0','2.0-2.5','1.5-2.0'])
    plt.show()

def visualize(src = FINAL):
    name = ['from','gpa','to','success']
    df = pd.read_csv(src,names=name)
    static_typical_GPA_success(df)


def typical_GPA_success(df):
    df0 = df.loc[df['from']==0]
    basic_info(df0)
    df1 = df.loc[df['from']==1]
    basic_info(df1)

def typical_preprocess():
    with open(SRC,encoding="utf8") as fread:
        with open('typical.csv','w',newline='') as fwrite:
            csvfread = csv.reader(fread)
            csvfwrite = csv.writer(fwrite)
            for row in csvfread:
                is_continue = False
                #whether there is a blank entry, if yes, delete the row
                for i in range(4):
                    if row[i] == '':
                        is_continue = True
                        continue
                #whther gpa is a valid num, if 50-100, transfer it into 0-4
                if row[0] in strict:
                    try:
                        row[1] = float(row[1])
                        if row[1] > 50 and row[1] < 100:
                            row[1] = FD_GPA(row[1])
                        elif row[1] >0 and row[1] <4:
                            row[1] = row[1]
                        else:
                            is_continue = True
                    except:
                        is_continue = True
                elif row[0] in nice:
                    try:
                        row[1] = float(row[1])
                        if row[1] > 50 and row[1] < 100:
                            row[1] = ZJ_GPA(row[1])
                        elif row[1] >0 and row[1] <4:
                            row[1] = row[1]
                        else:
                            is_continue = True
                    except:
                        is_continue = True
                else:
                    continue
                if is_continue:
                    continue
                csvfwrite.writerow(row)
def change_typical_name():
    with open('typical.csv') as fread:
        with open('typical_result.csv','w',newline = '') as fwrite:
            csvfread = csv.reader(fread)
            csvfwrite = csv.writer(fwrite)
            for row in csvfread:
                row[0] = int(row[0] in strict)
                row[2] = getnumber(row[2])
                row[3] = 1 if row[3] == '申请成功' else 0
                csvfwrite.writerow(row)





#delete_blank()
#Change_school_name()
visualize('typical_result.csv')
