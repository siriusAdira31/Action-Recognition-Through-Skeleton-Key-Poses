import math
import numpy as np
from sklearn  import linear_model
x_test=[4.9340057373046875, 258.69256591796875, 24.0556640625, -3.229522705078125, 459.26485443115234, 37.923583984375, 162.8968963623047, 266.8739929199219, -1.28564453125, 212.15296936035156, 513.6002464294434, -21.126220703125, 273.96507263183594, 783.7150726318359, 110.151123046875, -153.02889689803123, 250.51113891601562, 49.39697265625, -236.4850616455078, 505.2289581298828, -1.560546875, -329.2434997558594, 753.3191223144531, 119.501220703125, 80.81657409667969, 664.6129913330078, 36.998779296875, 102.0369873046875, 1097.8154296875, 17.96533203125, 97.68458557128906, 1516.9881591796875, -47.42724609375, -103.60266494750977, 655.0613021850586, 66.584228515625, -135.96467781066895, 1082.070068359375, 61.421630859375, -201.16712188720703, 1516.8191528320312, 122.87255859375, -8.163528442382812, 200.5722885131836, 13.867919921875, 157.962890625, 8.181427001953125, -25.34130859375, 207.21896362304688, 254.9076805114746, -45.181884765625, 269.03106689453125, 525.0225067138672, 86.095458984375, -157.96290263533592, -8.181427001953125, 25.34130859375, -241.4190673828125, 246.53639221191406, -25.6162109375, -334.17750549316406, 494.6265563964844, 95.445556640625, 75.882568359375, 405.92042541503906, 12.943115234375, 97.10298156738281, 839.1228637695312, -6.09033203125, 92.75057983398438, 1258.2955932617188, -71.48291015625, -108.53667068481445, 396.36873626708984, 42.528564453125, -140.89868354797363, 823.3775024414062, 37.365966796875, -206.10112762451172, 1258.1265869140625, 98.81689453125, 166.1264190673828, -192.39086151123047, -39.209228515625, 215.3824920654297, 54.335391998291016, -59.0498046875, 277.19459533691406, 324.4502182006836, 72.2275390625, -149.7993741929531, -208.75371551513672, 11.473388671875, -233.2555389404297, 45.96410369873047, -39.484130859375, -326.01397705078125, 294.0542678833008, 81.57763671875, 84.04609680175781, 205.34813690185547, -0.9248046875, 105.26651000976562, 638.5505752563477, -19.958251953125, 100.91410827636719, 1057.7233047485352, -85.350830078125, -100.37314224243164, 195.79644775390625, 28.66064453125, -132.73515510559082, 622.8052139282227, 23.498046875, -197.9375991821289, 1057.554298400879, 84.948974609375, 49.256072998046875, 246.72625350952148, -19.840576171875, 111.06817626953125, 516.8410797119141, 111.436767578125, -315.9257932603359, -16.36285400390625, 50.6826171875, -399.3819580078125, 238.35496520996094, -0.27490234375, -492.14039611816406, 486.44512939453125, 120.786865234375, -82.080322265625, 397.73899841308594, 38.284423828125, -60.85990905761719, 830.9414367675781, 19.2509765625, -65.21231079101562, 1250.1141662597656, -46.1416015625, -266.49956130981445, 388.1873092651367, 67.869873046875, -298.86157417297363, 815.1960754394531, 62.707275390625, -364.0640182495117, 1249.9451599121094, 124.158203125, 61.812103271484375, 270.1148262023926, 131.27734375, -365.1818662583828, -263.08910751342773, 70.523193359375, -448.6380310058594, -8.371288299560547, 19.565673828125, -541.3964691162109, 239.71887588500977, 140.62744140625, -131.33639526367188, 151.01274490356445, 58.125, -110.11598205566406, 584.2151832580566, 39.091552734375, -114.4683837890625, 1003.3879127502441, -26.301025390625, -315.7556343078613, 141.46105575561523, 87.71044921875, -348.1176471710205, 568.4698219299316, 82.5478515625, -413.3200912475586, 1003.2189064025879, 143.998779296875, -426.9939695298672, -533.2039337158203, -60.754150390625, -510.45013427734375, -278.4861145019531, -111.711669921875, -603.2085723876953, -30.395950317382812, 9.35009765625, -193.14849853515625, -119.10208129882812, -73.15234375, -171.92808532714844, 314.10035705566406, -92.185791015625, -176.28048706054688, 733.2730865478516, -157.578369140625, -377.5677375793457, -128.65377044677734, -43.56689453125, -409.9297504425049, 298.35499572753906, -48.7294921875, -475.13219451904297, 733.1040802001953, 12.721435546875, -83.45616474747658, 254.7178192138672, -50.95751953125, -176.21460285782814, 502.8079833984375, 70.104248046875, 233.84547099471092, 414.1018524169922, -12.398193359375, 255.06588420271873, 847.3042907714844, -31.431640625, 250.7134824693203, 1266.4770202636719, -96.82421875, 49.42623195052147, 404.55016326904297, 17.187255859375, 17.06421908736229, 831.5589294433594, 12.024658203125, -48.1382249891758, 1266.3080139160156, 73.4755859375, -92.75843811035156, 248.0901641845703, 121.061767578125, 317.3016357421875, 159.384033203125, 38.559326171875, 338.5220489501953, 592.5864715576172, 19.52587890625, 334.1696472167969, 1011.7592010498047, -45.86669921875, 132.88239669799805, 149.83234405517578, 68.144775390625, 100.52038383483887, 576.8411102294922, 62.982177734375, 35.31793975830078, 1011.5901947021484, 124.43310546875, 410.06007385253906, -88.70613098144531, -82.50244140625, 431.2804870605469, 344.4963073730469, -101.535888671875, 426.92808532714844, 763.6690368652344, -166.928466796875, 225.6408348083496, -98.25782012939453, -52.9169921875, 193.27882194519043, 328.7509460449219, -58.07958984375, 128.07637786865234, 763.5000305175781, 3.371337890625, 21.220413208007812, 433.2024383544922, -19.033447265625, 16.868011474609375, 852.3751678466797, -84.426025390625, -184.41923904418945, -9.551689147949219, 29.58544921875, -216.78125190734863, 417.4570770263672, 24.4228515625, -281.9836959838867, 852.2061614990234, 85.873779296875, -4.3524017333984375, 419.1727294921875, -65.392578125, -205.63965225219727, -442.7541275024414, 48.618896484375, -238.00166511535645, -15.745361328125, 43.456298828125, -303.20410919189453, 419.00372314453125, 104.9072265625, -201.28725051879883, -861.9268569946289, 114.011474609375, -233.649263381958, -434.9180908203125, 108.848876953125, -298.8517074584961, -0.16900634765625, 170.2998046875, -32.36201286315918, 427.0087661743164, -5.16259765625, -97.56445693969727, 861.7578506469727, 56.288330078125, -65.20244407653809, 434.74908447265625, 61.450927734375, -152.6956329345703, 543.9384765625, 2859.608154296875, -157.629638671875, 285.24591064453125, 2835.552490234375, -149.4661102294922, 84.67362213134766, 2821.6845703125, -315.592529296875, 277.0644836425781, 2860.893798828125, -364.8486022949219, 30.33823013305664, 2880.734375, -426.66070556640625, -239.77659606933594, 2749.45703125, 0.33326396346092224, 293.4273376464844, 2810.211181640625, 83.7894287109375, 38.70951843261719, 2861.168701171875, 176.54786682128906, -209.38064575195312, 2740.10693359375, -233.51220703125, -120.67451477050781, 2822.609375, -254.7326202392578, -553.876953125, 2841.642822265625, -250.38021850585938, -973.0496826171875, 2907.035400390625, -49.09296798706055, -111.1228256225586, 2793.02392578125, -16.730955123901367, -538.131591796875, 2798.1865234375, 48.47148895263672, -972.8806762695312, 2736.735595703125]

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
    ln=0
    N=5
    i=1
    m1=0
    s1=0
    list=[4,7,8,12]
    dp=['v1_extraction.txt','v2_extraction.txt','v3_extraction.txt','v4_extraction.txt','v5_extraction.txt','v6_extraction.txt','v7_extraction.txt','v8_extraction.txt','v9_extraction.txt','v10_extraction.txt','v11_extraction.txt','v12_extraction.txt','v13_extraction.txt','v14_extraction.txt','v15_extraction.txt','v16_extraction.txt','v17_extraction.txt','v18_extraction.txt','v19_extraction.txt','v20_extraction.txt','v25_extraction.txt','v26_extraction.txt','v27_extraction.txt','v28_extraction.txt','v29_extraction.txt','v30_extraction.txt','v31_extraction.txt','v32_extraction.txt','v33_extraction.txt','v34_extraction.txt','v35_extraction.txt','v36_extraction.txt','v37_extraction.txt','v38_extraction.txt','v39_extraction.txt','v40_extraction.txt','v41_extraction.txt','v42_extraction.txt','v43_extraction.txt','v44_extraction.txt','v45_extraction.txt','v46_extraction.txt','v47_extraction.txt','v48_extraction.txt','v49_extraction.txt','v50_extraction.txt','v51_extraction.txt','v52_extraction.txt','v53_extraction.txt','v54_extraction.txt','v55_extraction.txt','v56_extraction.txt','v57_extraction.txt','v58_extraction.txt','v59_extraction.txt','v60_extraction.txt','v61_extraction.txt','v62_extraction.txt','v63_extraction.txt','v64_extraction.txt','v65_extraction.txt','v66_extraction.txt','v67_extraction.txt','v68_extraction.txt','v69_extraction.txt','v70_extraction.txt','v71_extraction.txt','v72_extraction.txt','v73_extraction.txt','v74_extraction.txt','v75_extraction.txt','v76_extraction.txt','v77_extraction.txt','v78_extraction.txt','v79_extraction.txt','v80_extraction.txt','v81_extraction.txt','v82_extraction.txt','v83_extraction.txt','v84_extraction.txt','v85_extraction.txt','v86_extraction.txt','v87_extraction.txt','v88_extraction.txt','v89_extraction.txt','v90_extraction.txt','v91_extraction.txt','v92_extraction.txt','v93_extraction.txt','v94_extraction.txt','v95_extraction.txt','v96_extraction.txt','v97_extraction.txt','v98_extraction.txt','v99_extraction.txt','v100_extraction.txt','v101_extraction.txt','v102_extraction.txt','v103_extraction.txt','v104_extraction.txt','v105_extraction.txt','v106_extraction.txt','v107_extraction.txt','v108_extraction.txt','v109_extraction.txt','v110_extraction.txt','v111_extraction.txt','v112_extraction.txt','v113_extraction.txt','v114_extraction.txt','v115_extraction.txt','v116_extraction.txt','v117_extraction.txt','v118_extraction.txt','v119_extraction.txt','v120_extraction.txt','v121_extraction.txt','v122_extraction.txt','v123_extraction.txt','v124_extraction.txt','v125_extraction.txt']
    x_train1=[[0 for x in range(360)] for y in range(15)]
    x_train2=[[0 for x in range(360)] for y in range(15)]
    x_train3=[[0 for x in range(360)] for y in range(15)]
    x_train4=[[0 for x in range(360)] for y in range(15)]

    while i<N:
        pos=list[i-1]
        print("I"+str(i))
        if i>=N:
            break
        si_pos=get_EachFeature_frame(pos,"v1_extraction.txt")
        si_exp=si_pos
        vid=0
        pos_pose=[]
        while vid < 15:
            print(vid)
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
    xt=np.array(x_test)
    xt.resize((1,360))
    print(xt.size)
    y_train=[1,1,1,1,1,1,1,1,1,1,0,0,0,0,0]
    regr=linear_model.LinearRegression()
    regr.fit(x_train1,y_train)
    print(regr.coef_)
    y_ped=regr.predict(xt)
    print(y_ped)
    #Train(x_train1,x_train2,x_train3,x_train4)


'''def Train(x_train1,x_train2,x_train3,x_train4):
    x_train5=[[0 for x in range(1440)]for y in range(15)]
    j=0
    #y_train=[1,1,1,1,1,1,1,1,1,1,0,0,0,0,0]
    while j<1:
        listv=[]
        listv.append(list(x_train2[j]))
        listv.append(list(x_train3[j]))
        listv.append(list(x_train4[j]))
        listv.append(list(x_train4[j]))
        print(listv)
        x_train5[j]=listv
        j+=1
    print(x_train5)
    regr=linear_model.LinearRegression()
    regr.fit(x_train5,y_train)'''

def Eucledian(si_pos,fname,cnt,key_no):
    #print("k"+str(key_no))
    d=math.floor(cnt/4)
    #print("d"+str(d))
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
        #print("J"+str(j))
        #print("end: "+str(endno))
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


