import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import os
import sys


pd1 = " "; pd2 = " "; pd3 = " "

def plot_trend1(dir):
    global pd1; global pd2; global pd3
    df = pd.read_excel(dir,sheet_name="Pass_Data")
    save_dir = dir.split('.')

    #fig = plt.figure(figsize=(int(len(df['Shot Number'])), int(len(df['Shot Number'])/4)))
    plt.close()
    fig = plt.figure(figsize=(100, 50))


    axis1 = fig.add_subplot(4, 4, 1)
    axis1.plot(df['Shot Number'], df['Cycl Time (s)'], color='b')
    plt.title('Cycl Time Graph', fontsize=50)
    plt.xlabel('Shot Numbers',fontsize=30)
    plt.ylabel('Cycl Time (s)',fontsize=30)




    axis2 = fig.add_subplot(4, 4, 2)
    axis2.plot(df['Shot Number'], df['DLck HlpU (%)'], color='g')
    plt.title('DLck HlpU Graph', fontsize=50)
    plt.xlabel('Shot Numbers',fontsize=30)
    plt.ylabel('DLck HlpU (%)',fontsize=30)


    axis3 = fig.add_subplot(4, 4, 3)
    axis3.plot(df['Shot Number'], df['Low Spd (m/s)'], color='r')
    plt.title('Low Spd Graph', fontsize=50)
    plt.xlabel('Shot Numbers',fontsize=30)
    plt.ylabel('Low Spd (m/s)',fontsize=30)


    axis4 = fig.add_subplot(4, 4, 4)
    axis4.plot(df['Shot Number'], df['High Spd (m/s)'], color='tab:purple')
    plt.title('High Spd Graph', fontsize=50)
    plt.xlabel('Shot Numbers',fontsize=30)
    plt.ylabel('High Spd (m/s)',fontsize=30)


    axis5 = fig.add_subplot(4, 4, 5)
    axis5.plot(df['Shot Number'], df['Pres Up T (m/s)'], color='maroon')
    plt.title('Pres Up T Graph', fontsize=50)
    plt.xlabel('Shot Numbers',fontsize=30)
    plt.ylabel('Pres Up T (m/s)',fontsize=30)



    axis6 = fig.add_subplot(4, 4, 6)
    axis6.plot(df['Shot Number'], df['Cast Pres (MPa)'], color='indigo')
    plt.title('Cast Pres Graph', fontsize=50)
    plt.xlabel('Shot Numbers',fontsize=30)
    plt.ylabel('Cast Pres (MPa)',fontsize=30)


    axis7 = fig.add_subplot(4, 4, 7)
    axis7.plot(df['Shot Number'], df['Bis Size (mm)'], color='lime')
    plt.title('Bis Size Graph', fontsize=50)
    plt.xlabel('Shot Numbers',fontsize=30)
    plt.ylabel('Bis Size (mm)',fontsize=30)


    axis8 = fig.add_subplot(4, 4, 8)
    axis8.plot(df['Shot Number'], df['H-Spd St (mm)'], color='tab:orange')
    plt.title('H-Spd St Graph', fontsize=50)
    plt.xlabel('Shot Number',fontsize=30)
    plt.ylabel('H-Spd St (mm)',fontsize=30)


    axis9 = fig.add_subplot(4, 4, 9)
    axis9.plot(df['Shot Number'], df['H-Length (mm)'], color='crimson')
    plt.title('H-Length Graph', fontsize=50)
    plt.xlabel('Shot Numbers',fontsize=30)
    plt.ylabel('H-Length (mm)',fontsize=30)



    axis10 = fig.add_subplot(4, 4, 10)
    axis10.plot(df['Shot Number'], df['Fill End (mm)'], color='b')
    plt.title('Fill End Graph', fontsize=50)
    plt.xlabel('Shot Numbers',fontsize=30)
    plt.ylabel('Fill End (mm)',fontsize=30)



    axis11 = fig.add_subplot(4, 4, 11)
    axis11.plot(df['Shot Number'], df['Peek Spd (m/s)'], color='g')
    plt.title('Peek Spd Graph', fontsize=50)
    plt.xlabel('Shot Numbers',fontsize=30)
    plt.ylabel('Peek Spd (m/s)',fontsize=30)


    axis12 = fig.add_subplot(4, 4, 12)
    axis12.plot(df['Shot Number'], df['Shot Wt (kg)'], color='r')
    plt.title('Shot Wt Graph', fontsize=50)
    plt.xlabel('Shot Numbers',fontsize=30)
    plt.ylabel('Shot Wt (kg)',fontsize=30)


    axis13 = fig.add_subplot(4, 4, 13)
    axis13.plot(df['Shot Number'], df['Spray (sec)'], color='tab:purple')
    plt.title('Spray (sec)', fontsize=50)
    plt.xlabel('Shot Numbers',fontsize=30)
    plt.ylabel('Spray (sec)',fontsize=30)



    axis14 = fig.add_subplot(4, 4, 14)
    axis14.plot(df['Shot Number'], df['Core In (sec)'], color='maroon')
    plt.title('Core In Graph', fontsize=50)
    plt.xlabel('Shot Numbers',fontsize=30)
    plt.ylabel('Core In (sec)',fontsize=30)

    axis15 = fig.add_subplot(4, 4, 15)
    axis15.plot(df['Shot Number'], df['DieC lose (sec)'], color='indigo')
    plt.title('DieC lose Graph', fontsize=50)
    plt.xlabel('Shot Numbers',fontsize=30)
    plt.ylabel('DieC lose (sec)',fontsize=30)


    axis16 = fig.add_subplot(4, 4, 16)
    axis16.plot(df['Shot Number'], df['Pouring (sec)'], color='lime')
    plt.title('Pouring Graph', fontsize=50)
    plt.xlabel('Shot Numbers',fontsize=30)
    plt.ylabel('Pouring (sec)',fontsize=30)


    pd1 = save_dir[0] + "-trend_1-" +"pass.pdf"
    fig.savefig(save_dir[0] + "-trend_1-" +"pass.pdf")
    #plt.close()



    ############
    fig = plt.figure(figsize=(100, 50))

    axis17 = fig.add_subplot(4, 4, 1)
    axis17.plot(df['Shot Number'], df['Fill Pres (MPa)'], color='b')
    plt.title('Fill Pres Graph', fontsize=50)
    plt.xlabel('Shot Numbers', fontsize=30)
    plt.ylabel('Fill Pres (MPa)', fontsize=30)


    axis18 = fig.add_subplot(4, 4, 2)
    axis18.plot(df['Shot Number'], df['Fill Time (ms)'], color='crimson')
    plt.title('Fill Time Graph', fontsize=50)
    plt.xlabel('Shot Numbers', fontsize=30)
    plt.ylabel('Fill Time (ms)', fontsize=30)


    axis19 = fig.add_subplot(4, 4, 3)
    axis19.plot(df['Shot Number'], df['Work Cool (sec)'], color='b')
    plt.title('Work Cool Graph', fontsize=50)
    plt.xlabel('Shot Numbers', fontsize=30)
    plt.ylabel('Work Cool (sec)', fontsize=30)


    axis20 = fig.add_subplot(4, 4, 4)
    axis20.plot(df['Shot Number'], df['Die Open (sec)'], color='g')
    plt.title('Die Open Graph', fontsize=50)
    plt.xlabel('Shot Numbers', fontsize=30)
    plt.ylabel('Die Open (sec)', fontsize=30)


    axis21 = fig.add_subplot(4, 4, 5)
    axis21.plot(df['Shot Number'], df['D-Height (mm)'], color='r')
    plt.title('D-Height Graph', fontsize=50)
    plt.xlabel('Shot Numbers', fontsize=30)
    plt.ylabel('D-Height (mm)', fontsize=30)


    axis22 = fig.add_subplot(4, 4, 6)
    axis22.plot(df['Shot Number'], df['Pour Ret (deg)'], color='tab:purple')
    plt.title('Pour Ret Graph', fontsize=50)
    plt.xlabel('Shot Numbers', fontsize=30)
    plt.ylabel('Pour Ret (deg)', fontsize=30)


    axis23 = fig.add_subplot(4, 4, 7)
    axis23.plot(df['Shot Number'], df['A M.Temp 1 Max (ßC)'], color='maroon')
    plt.title('A M.Temp 1 Max Graph', fontsize=50)
    plt.xlabel('Shot Numbers', fontsize=30)
    plt.ylabel('A M.Temp 1 Max (ßC)', fontsize=30)


    axis24 = fig.add_subplot(4, 4, 8)
    axis24.plot(df['Shot Number'], df['A M.Temp 1 Min (ßC)'], color='indigo')
    plt.title('A M.Temp 1 Min Graph', fontsize=50)
    plt.xlabel('Shot Numbers', fontsize=30)
    plt.ylabel('A M.Temp 1 Min (ßC)', fontsize=30)


    axis25 = fig.add_subplot(4, 4, 9)
    axis25.plot(df['Shot Number'], df['B M.Temp 2 Max (ßC)'], color='lime')
    plt.title('B M.Temp 2 Max Graph', fontsize=50)
    plt.xlabel('Shot Numbers', fontsize=30)
    plt.ylabel('B M.Temp 2 Max (ßC)', fontsize=30)


    axis26 = fig.add_subplot(4, 4, 10)
    axis26.plot(df['Shot Number'], df['B M.Temp 2 Min (ßC)'], color='tab:orange')
    plt.title('B M.Temp 2 Max Graph', fontsize=50)
    plt.xlabel('Shot Number', fontsize=30)
    plt.ylabel('B M.Temp 2 Min (ßC)', fontsize=30)

    axis27 = fig.add_subplot(4, 4, 11)
    axis27.plot(df['Shot Number'], df['Inten Tms'], color='crimson')
    plt.title('Inten Tms Graph', fontsize=50)
    plt.xlabel('Shot Numbers', fontsize=30)
    plt.ylabel('Inten Tms', fontsize=30)


    axis28 = fig.add_subplot(4, 4, 12)
    axis28.plot(df['Shot Number'], df['C F.Temp 1 Max (ßC)'], color='b')
    plt.title('C F.Temp 1 Max Graph', fontsize=50)
    plt.xlabel('Shot Numbers', fontsize=30)
    plt.ylabel('C F.Temp 1 Max (ßC)', fontsize=30)


    axis29 = fig.add_subplot(4, 4, 13)
    axis29.plot(df['Shot Number'], df['C F.Temp 1 Min (ßC)'], color='g')
    plt.title('C F.Temp 1 Min Graph', fontsize=50)
    plt.xlabel('Shot Numbers', fontsize=30)
    plt.ylabel('C F.Temp 1 Min (ßC)', fontsize=30)


    axis30 = fig.add_subplot(4, 4, 14)
    axis30.plot(df['Shot Number'], df['Fill Stat (mm)'], color='r')
    plt.title("Fill Stat Graph", fontsize=50)
    plt.xlabel('Shot Numbers', fontsize=30)
    plt.ylabel('Fill Stat (mm)', fontsize=30)


    axis31 = fig.add_subplot(4, 4, 15)
    axis31.plot(df['Shot Number'], df['P Up Stat (mm)'], color='tab:purple')
    plt.title("P Up Stat Graph", fontsize=50)
    plt.xlabel('Shot Numbers', fontsize=30)
    plt.ylabel('P Up Stat (mm)', fontsize=30)


    axis32 = fig.add_subplot(4, 4, 16)
    axis32.plot(df['Shot Number'], df['Core Out (sec)'], color='maroon')
    plt.title("Core Out Graph", fontsize=50)
    plt.xlabel('Shot Numbers', fontsize=30)
    plt.ylabel('Core Out (sec)', fontsize=30)

    pd2 = save_dir[0] + "-trend_2-" + "pass.pdf"
    fig.savefig(save_dir[0] + "-trend_2-" + "pass.pdf")

    ############
    fig = plt.figure(figsize=(100, 50))

    axis33 = fig.add_subplot(4, 4, 1)
    axis33.plot(df['Shot Number'], df['Eject (sec)'], color='indigo')
    plt.title("Eject (sec) Graph", fontsize=50)
    plt.xlabel('Shot Numbers', fontsize=30)
    plt.ylabel('Eject (sec)', fontsize=30)

    axis34 = fig.add_subplot(4, 4, 2)
    axis34.plot(df['Shot Number'], df['Take-Out (sec)'], color='lime')
    plt.title("Take-Out (sec) Graph", fontsize=50)
    plt.xlabel('Shot Numbers', fontsize=30)
    plt.ylabel('Take-Out (sec)', fontsize=30)

    axis35 = fig.add_subplot(4, 4, 3)
    axis35.plot(df['Shot Number'], df['D F.Temp 2 Max (ßC)'], color='tab:orange')
    plt.title("D F.Temp 2 Max (ßC) Graph", fontsize=50)
    plt.xlabel('Shot Number', fontsize=30)
    plt.ylabel('D F.Temp 2 Max (ßC)', fontsize=30)

    axis36 = fig.add_subplot(4, 4, 4)
    axis36.plot(df['Shot Number'], df['Shtpres (MPa)'], color='crimson')
    plt.title("Shtpres (MPa) Graph", fontsize=50)
    plt.xlabel('Shot Numbers', fontsize=30)
    plt.ylabel('Shtpres (MPa)', fontsize=30)

    axis37 = fig.add_subplot(4, 4, 5)
    axis37.plot(df['Shot Number'], df['D F.Temp 2 Min (ßC)'], color='b')
    plt.title("D F.Temp 2 Min (ßC) Graph", fontsize=50)
    plt.xlabel('Shot Numbers', fontsize=30)
    plt.ylabel('D F.Temp 2 Min (ßC)', fontsize=30)

    axis38 = fig.add_subplot(4, 4, 6)
    axis38.plot(df['Shot Number'], df['C F.Temp 1 Min (ßC)'], color='g')
    plt.title("C F.Temp 1 Min (ßC) Graph", fontsize=50)
    plt.xlabel('Shot Numbers', fontsize=30)
    plt.ylabel('C F.Temp 1 Min (ßC)', fontsize=30)

    axis39 = fig.add_subplot(4, 4, 7)
    axis39.plot(df['Shot Number'], df['E Metal Ave (ßC)'], color='r')
    plt.title("E Metal Ave (ßC) Graph", fontsize=50)
    plt.xlabel('Shot Numbers', fontsize=30)
    plt.ylabel('E Metal Ave (ßC)', fontsize=30)

    axis40 = fig.add_subplot(4, 4, 8)
    axis40.plot(df['Shot Number'], df['F M.Cool. Ave(ßC)'], color='tab:purple')
    plt.title("F M.Cool. Ave(ßC) Graph", fontsize=50)
    plt.xlabel('Shot Numbers', fontsize=30)
    plt.ylabel('F M.Cool. Ave(ßC)', fontsize=30)

    axis41 = fig.add_subplot(4, 4, 9)
    axis41.plot(df['Shot Number'], df['M.Cooling Water (l/m)'], color='maroon')
    plt.title("M.Cooling Water (l/m) Graph", fontsize=50)
    plt.xlabel('Shot Numbers', fontsize=30)
    plt.ylabel('M.Cooling Water (l/m)', fontsize=30)

    axis42 = fig.add_subplot(4, 4, 10)
    axis42.plot(df['Shot Number'], df['F.Cooling Water (l/m)'], color='indigo')
    plt.title("F.Cooling Water (l/m) Graph", fontsize=50)
    plt.xlabel('Shot Numbers', fontsize=30)
    plt.ylabel('F.Cooling Water (l/m)', fontsize=30)

    axis43 = fig.add_subplot(4, 4, 11)
    axis43.plot(df['Shot Number'], df['Tip Cooling Flow (l/m)'], color='lime')
    plt.title("Tip Cooling Flow (l/m) Graph", fontsize=50)
    plt.xlabel('Shot Numbers', fontsize=30)
    plt.ylabel('Tip Cooling Flow (l/m)', fontsize=30)

    axis44 = fig.add_subplot(4, 4, 12)
    axis44.plot(df['Shot Number'], df['Oil Cooler Flow (l/m)'], color='tab:orange')
    plt.title("Oil Cooler Flow (l/m) Graph", fontsize=50)
    plt.xlabel('Shot Number', fontsize=30)
    plt.ylabel('Oil Cooler Flow (l/m)', fontsize=30)

    axis45 = fig.add_subplot(4, 4, 13)
    axis45.plot(df['Shot Number'], df['VShutPos (mm)'], color='crimson')
    plt.title("VShutPos (mm) Graph", fontsize=50)
    plt.xlabel('Shot Numbers', fontsize=30)
    plt.ylabel('VShutPos (mm)', fontsize=30)

    axis46 = fig.add_subplot(4, 4, 14)
    axis46.plot(df['Shot Number'], df['DieLub.SprayLe (ml)'], color='b')
    plt.title("DieLub.SprayLe (ml) Graph", fontsize=50)
    plt.xlabel('Shot Numbers', fontsize=30)
    plt.ylabel('DieLub.SprayLe (ml)', fontsize=30)

    axis47 = fig.add_subplot(4, 4, 15)
    axis47.plot(df['Shot Number'], df['Vacuum (kPa)'], color='g')
    plt.title("Vacuum (kPa) Graph", fontsize=50)
    plt.xlabel('Shot Numbers', fontsize=30)
    plt.ylabel('Vacuum (kPa)', fontsize=30)

    axis48 = fig.add_subplot(4, 4, 16)
    axis48.plot(df['Shot Number'], df['Peak Vacum (kPa)'], color='r')
    plt.title("Peak Vacum (kPa) Graph", fontsize=50)
    plt.xlabel('Shot Numbers', fontsize=30)
    plt.ylabel('Peak Vacum (kPa)', fontsize=30)

    pd3 = save_dir[0] + "-trend_3-" + "pass.pdf"

    fig.savefig(save_dir[0] + "-trend_3-" + "pass.pdf")

def open_pdf():
    os.startfile(pd1)
    os.startfile(pd2)
    os.startfile(pd3)
