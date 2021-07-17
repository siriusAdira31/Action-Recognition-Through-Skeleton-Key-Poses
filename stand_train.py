import math
x_train9=[[0 for x in range(360)] for y in range(20)]
x_train10=[[0 for x in range(360)] for y in range(20)]
x_train11=[[0 for x in range(360)] for y in range(20)]
x_train12=[[0 for x in range(360)] for y in range(20)]
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
    list=[6,10,17,24]
    dp=['v45_extraction.txt','v46_extraction.txt','v47_extraction.txt','v48_extraction.txt','v49_extraction.txt','v50_extraction.txt','v51_extraction.txt','v52_extraction.txt','v53_extraction.txt','v54_extraction.txt','v55_extraction.txt','v56_extraction.txt','v57_extraction.txt','v58_extraction.txt','v59_extraction.txt','v60_extraction.txt','v61_extraction.txt','v62_extraction.txt','v63_extraction.txt','v64_extraction.txt']


    while i<N:
        pos=list[i-1]
        if i>=N:
            break
        si_pos=get_EachFeature_frame(pos,"v45_extraction.txt")
        si_exp=si_pos
        vid=0
        pos_pose=[]
        while vid < 20:
            fname=dp[vid]
            pos_pose.append(Eucledian(si_exp,fname,getCnt(fname),i))
            vid+=1
        z=0
        s=45
        while z<20:
            frame=get_EachFeature_frame(pos_pose[z],"v"+str(s)+"_extraction.txt")
            if i==1:
                x_train9[z]=frame
            if i==2:
                x_train10[z]=frame
            if i==3:
                x_train11[z]=frame
            if i==4:
                x_train12[z]=frame
            s=s+1
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


