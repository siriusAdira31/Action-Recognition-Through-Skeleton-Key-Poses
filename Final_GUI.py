import Wavetrain as wt
import math
import Bendtrain as bt
import stand_train as st
import sittrain as st2
import claptrain as ct
import Timetrain as tt
from sklearn import tree
import numpy as np
from tkinter import *
from tkinter.filedialog import askopenfilename
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
import matplotlib as plt

arr_nm=["Waving_hand","Bending","Standing","Sitting","Clapping","Watching Time"]
#wt=15, bt=19,st=20;st2=20;ct=29;tt=13
x_traina11=wt.x_train1
x_traina12=wt.x_train2
x_traina13=wt.x_train3
x_traina14=wt.x_train4
x_traina21=bt.x_train5
x_traina22=bt.x_train6
x_traina23=bt.x_train7
x_traina24=bt.x_train8
x_traina31=st.x_train9
x_traina32=st.x_train10
x_traina33=st.x_train11
x_traina34=st.x_train12
x_traina41=st2.x_train13
x_traina42=st2.x_train14
x_traina43=st2.x_train15
x_traina44=st2.x_train16
x_traina51=ct.x_train17
x_traina52=ct.x_train18
x_traina53=ct.x_train19
x_traina54=ct.x_train20
x_traina61=tt.x_train21
x_traina62=tt.x_train22
x_traina63=tt.x_train23
x_traina64=tt.x_train24
y_train=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6,6,6,6,6]


p1=np.concatenate((x_traina11,x_traina21),axis=0)
p2=np.concatenate((p1,x_traina31),axis=0)
p3=np.concatenate((p2,x_traina41),axis=0)
p4=np.concatenate((p3,x_traina51),axis=0)
p5=np.concatenate((p4,x_traina61),axis=0)

p6=np.concatenate((x_traina12,x_traina22),axis=0)
p7=np.concatenate((p6,x_traina32),axis=0)
p8=np.concatenate((p7,x_traina42),axis=0)
p9=np.concatenate((p8,x_traina52),axis=0)
p10=np.concatenate((p9,x_traina62),axis=0)

p11=np.concatenate((x_traina13,x_traina23),axis=0)
p12=np.concatenate((p11,x_traina33),axis=0)
p13=np.concatenate((p12,x_traina43),axis=0)
p14=np.concatenate((p13,x_traina53),axis=0)
p15=np.concatenate((p14,x_traina63),axis=0)

p16=np.concatenate((x_traina14,x_traina24),axis=0)
p17=np.concatenate((p16,x_traina34),axis=0)
p18=np.concatenate((p17,x_traina44),axis=0)
p19=np.concatenate((p18,x_traina54),axis=0)
p20=np.concatenate((p19,x_traina64),axis=0)

d1=tree.DecisionTreeClassifier()
d1.fit(p5,y_train)
d2=tree.DecisionTreeClassifier()
d2.fit(p10,y_train)
d3=tree.DecisionTreeClassifier()
d3.fit(p15,y_train)
d4=tree.DecisionTreeClassifier()
d4.fit(p20,y_train)

def get_EachFeature_frame(ln,file):
    f=open(file)
    lines=f.readlines()
    str=lines[ln]
    feature=[]
    for word in str.split(','):
        word1=word[1:len(word)-2]
        feature.append(float(word1))
    return feature

def getCnt(fname):
    cnt=0
    f=open(fname)
    lines=f.readlines()
    cnt=len(lines)
    return cnt

def test(fname):
    cnt=getCnt(fname)
    d=math.floor(cnt/4)
    endno=0
    key_no=1
    while key_no<5:
        if key_no==1:
            j=1
            endno=j+d
        elif key_no==2:
            j=j+d+1
            endno=j+d
        elif key_no==3:
            j=j+d+d
            endno=j+d
            if endno>cnt:
                endno=cnt-1
        elif key_no==4:
            j=cnt-d
            endno=cnt-1

        if key_no==1:
            x_test1=get_EachFeature_frame(endno,fname)

        if key_no==2:
            x_test2=get_EachFeature_frame(endno,fname)

        if key_no==3:
            x_test3=get_EachFeature_frame(endno,fname)

        if key_no==4:
            x_test4=get_EachFeature_frame(endno,fname)
        key_no+=1
    return((x_test1,x_test2,x_test3,x_test4))



def load_file():
    fname = askopenfilename()
    v=fname.split('/')
    cnt=0
    for i in v:
        if cnt==6:
            f=i
        cnt+=1
    print(v[6])
    (x_test1,x_test2,x_test3,x_test4)=test(str(v[6]))

    xt1=np.array(x_test1)
    xt1.resize(1,360)

    xt2=np.array(x_test2)
    xt2.resize(1,360)

    xt3=np.array(x_test3)
    xt3.resize(1,360)

    xt4=np.array(x_test4)
    xt4.resize(1,360)

    knn1=KNeighborsClassifier(n_neighbors=1)
    knn2=KNeighborsClassifier(n_neighbors=1)
    knn3=KNeighborsClassifier(n_neighbors=1)
    knn4=KNeighborsClassifier(n_neighbors=1)

    knn1.fit(p5,y_train)
    knn2.fit(p10,y_train)
    knn3.fit(p15,y_train)
    knn4.fit(p20,y_train)
    print(knn1.predict(xt1))
    print(knn2.predict(xt2))
    print(knn3.predict(xt3))
    print(knn4.predict(xt4))

    y_pred5=knn1.predict(xt1)
    y_pred6=knn2.predict(xt2)
    y_pred7=knn3.predict(xt3)
    y_pred8=knn4.predict(xt4)

    text1.grid(row=4,column=1,sticky=W)
    arr=[]
    arr.append(y_pred5)
    arr.append(y_pred6)
    arr.append(y_pred7)
    arr.append(y_pred8)
    arr.sort()


    if(arr[0]==arr[1]==arr[2] or arr[1]==arr[2]==arr[3]):
        print(arr_nm[int(arr[1]-1)])
        text1.insert(INSERT,"\n")
        text1.insert(INSERT,str(arr_nm[int(arr[0]-1)]))
    else:
        print("Other action(Except Waving,bend,Sit,stand,Time,clap)")
        text1.insert(INSERT,"\n")
        text1.insert(INSERT,"Other action(Except Waving,bend,Sit,stand,Time,clap)")
    #text1.insert(INSERT,str(confusion_matrix(arr,[2,2,2,2])))
    #plt
    #plt.show()

root = Tk()
root.title("Action Recognition")

MainFrame=Frame(root)
MainFrame.grid(row=1, column=0, sticky=W)
Label(root, text="File Name :", font=880).grid(row=2, column=0, sticky=W)
button = Button(root, text="Browse",font=880, command=load_file, width=10)
button.grid(row=2, column=1, sticky=W)
text1=Text(root)



root.mainloop()


