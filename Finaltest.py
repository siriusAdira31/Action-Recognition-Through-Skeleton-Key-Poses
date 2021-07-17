import math

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
            print(x_test1)
        if key_no==2:
            x_test2=get_EachFeature_frame(endno,fname)
            print(x_test2)
        if key_no==3:
            x_test3=get_EachFeature_frame(endno,fname)
            print(x_test3)
        if key_no==4:
            x_test4=get_EachFeature_frame(endno,fname)
            print(x_test4)
        key_no+=1



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

test("clap_c4a1-1.txt")
