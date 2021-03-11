import sys
import pandas as pd
import matplotlib.pyplot as plt
import re

filename = sys.argv
#print(filename[1])
filename = filename[1]
file =open(filename, "r")
lines = file.readlines()
file.close()


def date_format(data):
    # data = pd.DataFrame(columns=['Col1', 'Col2', 'Col3', 'Col4', 'Col5', 'Col6', 'Col7', 'Col8', 'Col9', 'Col10', 'Col11', 'Col12', 'Col13', 'Col14', 'Col15', 'Col16', 'Col17', 'Col18', 'Col19', 'Col20', 'Col21', 'Col22', 'Col23', 'Col24', 'Col25', 'Col26', 'Col27', 'Col28', 'Col29', 'Col30', 'Col31', 'Col32', 'Col33', 'Col34', 'Col35', 'Col36', 'Col37', 'Col38', 'Col39', 'Col40', 'Col41', 'Col42', 'Col43', 'Col44', 'Col45', 'Col46', 'Col47', 'Col48', 'Col49', 'Col50', 'Col51', 'Col52'])
    data_1 = re.findall('\d+', data[0])
    first_val = data_1[0] + '/' + data_1[1] + '/' + data_1[2]
    second_val = data_1[3] + ':' + data_1[4] + ':' + data_1[5]
    return (first_val, second_val)

data = pd.DataFrame(columns=['Col1', 'Col2', 'Col3', 'Col4', 'Col5', 'Col6', 'Col7', 'Col8', 'Col9', 'Col10', 'Col11',
                             'Col12', 'Col13', 'Col14', 'Col15', 'Col16', 'Col17', 'Col18', 'Col19', 'Col20', 'Col21',
                             'Col22', 'Col23', 'Col24', 'Col25', 'Col26', 'Col27', 'Col28', 'Col29', 'Col30', 'Col31',
                             'Col32', 'Col33', 'Col34', 'Col35', 'Col36', 'Col37', 'Col38', 'Col39', 'Col40', 'Col41',
                             'Col42', 'Col43', 'Col44', 'Col45', 'Col46', 'Col47', 'Col48', 'Col49', 'Col50', 'Col51', 'Col52'])


data = data.append({'Col1':'Date', 'Col2': "Time",'Col3':'Shot Number','Col4':'StartUp On','Col5':'Cycl Time (s)',
                    'Col6':'DLck HlpU (%)','Col7':'Low Spd (m/s)','Col8':'High Spd (m/s)','Col9':'Pres Up T (m/s)',
                    'Col10':'Cast Pres (MPa)','Col11':'Bis Size (mm)','Col12':'H-Spd St (mm)','Col13':'H-Length (mm)',
                    'Col14':'Fill End (mm)','Col15':'Peek Spd (m/s)','Col16':'Shot Wt (kg)','Col17':'Spray (sec)',
                    'Col18':'Core In (sec)','Col19':'DieC lose (sec)','Col20':'Pouring (sec)','Col21':'Fill Pres (MPa)',
                    'Col22':'Fill Time (ms)','Col23':'Shot (sec)','Col23':'Work Cool (sec)','Col24':'Die Open (sec)',
                    'Col25':'D-Height (mm)','Col26':'Pour Ret (deg)','Col27':'A M.Temp 1 Max (ßC)',
                    'Col28':'A M.Temp 1 Min (ßC)','Col29':'B M.Temp 2 Max (ßC)','Col30':'B M.Temp 2 Min (ßC)',
                    'Col31':'Inten Tms','Col32':'C F.Temp 1 Max (ßC)','Col33':'C F.Temp 1 Min (ßC)','Col34':'Fill Stat (mm)',
                    'Col35':'P Up Stat (mm)','Col36':'Core Out (sec)','Col37':'Eject (sec)','Col38':'Take-Out (sec)',
                    'Col39':'D F.Temp 2 Max (ßC)','Col40':'Shtpres (MPa)','Col41':'D F.Temp 2 Min (ßC)',
                    'Col42':'E Metal Ave (ßC)','Col43':'F M.Cool. Ave(ßC)','Col44':'M.Cooling Water (l/m)',
                    'Col45':'F.Cooling Water (l/m)','Col46':'Tip Cooling Flow (l/m)','Col47':'Oil Cooler Flow (l/m)',
                    'Col48':'VShutPos (mm)','Col49':'DieLub.SprayLe (ml)','Col50':'Vacuum (kPa)',
                    'Col51':'Peak Vacum (kPa)','Col52':" "},ignore_index=True)

for line in lines:
    words = line.split(',')
    #print(words[0])
    numbers_col1 = re.findall('\d+',words[0])
    if len(numbers_col1) >= 6:
        #print(words)
        #print(len(words))
        first_columns = date_format(words)
        data = data.append({'Col1':first_columns[0], 'Col2': first_columns[1],'Col3':words[1],'Col4':words[2],'Col5':float(str(words[3])),
                            'Col6':int(words[4]),'Col7':float(words[5]),'Col8':float(words[6]),'Col9':int(words[7]),'Col10':float(words[8]),'Col11':float(words[9]),
                            'Col12':float(words[10]),'Col13':float(words[11]),'Col14':float(words[12]),'Col15':float(words[13]),'Col16':float(words[14]),
                            'Col17':float(words[15]),'Col18':float(words[16]),'Col19':float(words[17]),'Col20':float(words[18]),'Col21':float(words[19]),
                            'Col22':int(words[20]),'Col23':float(words[21]),'Col23':float(words[22]),'Col24':float(words[23]),'Col25':float(words[24]),
                            'Col26':float(words[25]),'Col27':float(words[26]),'Col28':float(words[27]),'Col29':float(words[28]),'Col30':float(words[29]),
                            'Col31':float(words[30]),'Col32':float(words[31]),'Col33':float(words[32]),'Col34':float(words[33]),'Col35':float(words[34]),
                            'Col36':float(words[35]),'Col37':float(words[36]),'Col38':float(words[37]),'Col39':float(words[38]),'Col40':float(words[39]),
                            'Col41':float(words[40]),'Col42':float(words[41]),'Col43':float(words[42]),'Col44':float(words[43]),'Col45':float(words[44]),
                            'Col46':float(words[45]),'Col47':float(words[46]),'Col48':float(words[47]),'Col49':float(words[48]),'Col50':float(words[49]),
                            'Col51':float(words[50]),'Col52':" "},ignore_index=True)


filename = filename.replace(".SPR",".xlsx")
writer = pd.ExcelWriter(filename, engine='xlsxwriter')

data.to_excel(writer,sheet_name="1", startcol=0, header=None, index=False)
writer.save()
