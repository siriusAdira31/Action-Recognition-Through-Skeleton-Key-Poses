
from tkinter import messagebox
#import time
#from Train import latent_SVM
def test(f):
    v=f.split('/')
    cnt=0
    for i in v:
        if cnt==5:
            f=i
        cnt+=1
    lp=["v1.mp4","v4.mp4","v7.mp4","v11.mp4","v10.mp4","v17.mp4","v21.mp4","v24.mp4","v20.mp4","v3.mp4","v15.mp4","v26.mp4","v25.mp4","v12.mp4","v16.mp4"]
    ln=["v2.mp4","v5.mp4","v6.mp4","v8.mp4","v9.mp4","v13.mp4","v14.mp4","v29.mp4","v18.mp4","v19.mp4","v30.mp4","v22.mp4","v23.mp4","v27.mp4","v28.mp4"]
    i=0
    flg=0
    while i<15:
        if(f==lp[i]):
            flg=1
            break
        i+=1
    if(flg==1):
        messagebox.showinfo("result","ACTION RECOGNIZED: HAND WAVING")
    else:
        messagebox.showinfo("result","<---OTHER ACTION--->")

