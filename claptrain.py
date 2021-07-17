import math
x_train17=[[0 for x in range(360)] for y in range(29)]
x_train18=[[0 for x in range(360)] for y in range(29)]
x_train19=[[0 for x in range(360)] for y in range(29)]
x_train20=[[0 for x in range(360)] for y in range(29)]

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
    list=[2,5,9,12]
    dp=['v97_extraction.txt','v98_extraction.txt','v99_extraction.txt','v100_extraction.txt','v101_extraction.txt','v102_extraction.txt','v103_extraction.txt','v104_extraction.txt','v105_extraction.txt','v106_extraction.txt','v107_extraction.txt','v108_extraction.txt','v109_extraction.txt','v110_extraction.txt','v111_extraction.txt','v112_extraction.txt','v113_extraction.txt','v114_extraction.txt','v115_extraction.txt','v116_extraction.txt','v117_extraction.txt','v118_extraction.txt','v119_extraction.txt','v120_extraction.txt','v121_extraction.txt','v122_extraction.txt','v123_extraction.txt','v124_extraction.txt','v125_extraction.txt']
    while i<N:
        pos=list[i-1]
        if i>=N:
            break
        si_pos=get_EachFeature_frame(pos,"v97_extraction.txt")
        si_exp=si_pos
        vid=0
        pos_pose=[]
        while vid < 29:
            fname=dp[vid]
            pos_pose.append(Eucledian(si_exp,fname,getCnt(fname),i))
            vid+=1

        z=0
        s=97
        while z<29:
            frame=get_EachFeature_frame(pos_pose[z],"v"+str(s)+"_extraction.txt")
            s=s+1
            if i==1:
                x_train17[z]=frame
            if i==2:
                x_train18[z]=frame
            if i==3:
                x_train19[z]=frame
            if i==4:
                x_train20[z]=frame
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


