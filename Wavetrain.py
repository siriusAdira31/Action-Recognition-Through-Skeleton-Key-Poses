import math
x_train1=[[0 for x in range(360)] for y in range(15)]
x_train2=[[0 for x in range(360)] for y in range(15)]
x_train3=[[0 for x in range(360)] for y in range(15)]
x_train4=[[0 for x in range(360)] for y in range(15)]

def get_EachFeature_frame(ln,file):
    f=open(file)
    lines=f.readlines()
    str=lines[ln]
    feature=[]
    for word in str.split(','):
        word1=word[1:len(word)-2]
        feature.append(float(word1))
    return feature

def latent_SVM():
    N=5
    i=1
    list=[4,7,8,12]
    dp=['v1_extraction.txt','v2_extraction.txt','v3_extraction.txt','v4_extraction.txt','v5_extraction.txt','v6_extraction.txt','v7_extraction.txt','v8_extraction.txt','v9_extraction.txt','v10_extraction.txt','v11_extraction.txt','v12_extraction.txt','v13_extraction.txt','v14_extraction.txt','v15_extraction.txt']
    while i<N:
        pos=list[i-1]
        if i>=N:
            break
        si_pos=get_EachFeature_frame(pos,"v1_extraction.txt")
        si_exp=si_pos
        vid=0
        pos_pose=[]
        while vid < 15:
            fname=dp[vid]
            pos_pose.append(Eucledian(si_exp,fname,getCnt(fname),i))
            vid+=1

        z=0
        s=1
        while z<15:
            frame=get_EachFeature_frame(pos_pose[z],"v"+str(s)+"_extraction.txt")
            s=s+1
            if i==1:
                x_train1[z]=frame
            if i==2:
                x_train2[z]=frame
            if i==3:
                x_train3[z]=frame
            if i==4:
                x_train4[z]=frame
            z+=1
        i+=1

def Eucledian(si_pos,fname,cnt,key_no):
    d=math.floor(cnt/4)
    endno=0
    j=1
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
    min=temp=euclidian_dist(si_pos,get_EachFeature_frame(j,fname))
    index=j
    j=j+1
    while j<=endno:
        frame=get_EachFeature_frame(j,fname)
        temp=euclidian_dist(si_pos,frame)
        if temp<min:
            min=temp
            index=j
        j+=1
    return index



def euclidian_dist(si1,si2):
    dif=0.0
    squre=0.0
    i=0
    sum=0
    dist=0.0
    while i<360:
        dif=si1[i]-si2[i]
        squre=math.pow(dif,2)
        sum+=squre
        i+=1
    dist=math.sqrt(sum)
    return dist

def getCnt(fname):
    cnt=0
    f=open(fname)
    lines=f.readlines()
    cnt=len(lines)
    return cnt



latent_SVM()


