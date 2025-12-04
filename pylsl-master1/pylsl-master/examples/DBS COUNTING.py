from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
from pylsl import StreamInlet, resolve_stream
import datetime
import random

print("looking for an EEG stream...\n刷新时间为0.5s")
streams = resolve_stream('type', 'EEG')

inlet = StreamInlet(streams[0])

ch=[[0 for x in range(125)] for y in range(8)]
sampling_rate=250
fft_size=125
group=0
an=[]
name=input('please input the ID:')

begin=datetime.datetime.now()
while True:
    for num in range(0,125):
        sample, timestamp = inlet.pull_sample()  #读取数据
        for num1 in range(0,8):
            ch[num1][num]=sample[num1+1]
            
    for catch in range(0,8):
        b, a = signal.butter(8, 2*30/sampling_rate, 'lowpass')  #低频滤波器
        filtedData = signal.filtfilt(b, a, ch[catch])  #这里要改
        
        xs=filtedData                               #傅里叶变换
        xf=np.fft.rfft(ch[catch])/fft_size                           
        freqs=np.linspace(0,sampling_rate/2,fft_size/2+1)      #频率
        #xfp=20*np.log10(np.clip(np.abs(xf),1e-20,1e100))      #幅值的对数表示
        a=np.abs(xf)*2                                         #幅值
        an=a
        for i in range(2,60):
            if an[i]>an[i+1]:
                an[i+1]=an[i]
            else:
                fftmax=i+1
        A_max=a[fftmax]/100
        #A_max=random.uniform(0,1)
        #freqs_max=random.uniform(1,10)
        freqs_max=freqs[fftmax]
        end=datetime.datetime.now()
        print('[',end-begin,']    ',end='')
        if catch==0:
            group=group+1
            print('num',str(group).zfill(4),end='')
        else:
            print('        ',end='')
        print('   ch',catch,'僵直系数= ',round(A_max**2,2),' 震颤系数= ',round(freqs_max,2))
        text='['+str(end-begin)+']    '+'ch'+str(catch)+'僵直系数= '+str(round(A_max**2,2))+'   震颤系数= '+str(round(freqs_max,2))+ '\n'
        file_data=open(name+'-data.txt','a')
        file_data.write(text)
        file_data.close

