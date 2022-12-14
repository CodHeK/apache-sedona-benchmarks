import matplotlib
matplotlib.use('Agg')

from IPython.display import display

import pandas as pd
import matplotlib.pyplot as plt

x = {
    '1k': 1000,
    '5k': 5000,
    '10k': 10000,
    '25k': 25000,
    '50k': 50000,
    '100k': 100000
}

def plot_size(title, path, img_path):
    df = pd.read_csv(path, na_values='NaN')

    extra_sizes = [ '5k', '25k', '50k' ]
    extra_rows = []

    for size in extra_sizes:
        row = { 'size': size }

        for col in df.columns[1:]:
            row[col] = 'NaN'

        extra_rows.append(row)
    
    for row in extra_rows:
        df = pd.concat([df, pd.DataFrame(row, index=[len(df)])])

    df['size'] = [ x[item] for item in df['size'] ]
    df.sort_values('size', inplace = True, ascending=True)

    df = pd.DataFrame(data = df.values, columns= df.columns, dtype='float32')

    for col in df.columns[1:]:
        df[col] = df[col].interpolate(method='spline', order = 2, limit_direction='both')

    df['size'] = x.keys()

    df.set_index('size').plot(title=title)
    plt.savefig(img_path)
    plt.close()


def plot_k(title, path, img_path):
    df = pd.read_csv(path)
    df.set_index('k').plot(title=title)
    plt.savefig(img_path)
    plt.close()