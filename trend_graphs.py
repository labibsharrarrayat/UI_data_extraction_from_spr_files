import matplotlib.pyplot as plt
import pandas as pd

def plt_trend(dir, df, status):
    dir = dir.split('.')

    fig = plt.figure(figsize=(int(len(df['Shot Number'])), int(len(df['Shot Number']) / 4)))

    plt.plot(df['Shot Number'], df['Cycl Time (s)'], color='b')
    plt.title('Cycl Time Graph', fontsize=50)
    plt.xlabel('Shot Numbers', fontsize=30)
    plt.ylabel('Cycl Time (s)', fontsize=30)
    plt.xticks(rotation=90)

    fig.savefig(dir[0] + "-Cycle_Time-" + status + ".pdf")