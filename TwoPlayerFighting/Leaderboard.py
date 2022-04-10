import pandas as pd

def leaderboard_write(filename, name, score):
    file = open(filename,'a')
    file.write('\n' + name + ' ' + str(score))
    file.close()

def leaderboard_read(filename):
    df = pd.read_csv(filename, sep=' ')
    x = df.to_numpy()
    
    return x