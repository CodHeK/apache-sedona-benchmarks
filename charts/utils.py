import matplotlib
matplotlib.use('Agg')

from IPython.display import display

import pandas as pd
import matplotlib.pyplot as plt



def plot(title, path, img_path):
    df = pd.read_csv(path, na_values='NaN')

    extra_sizes = [ '5k', '25k', '50k' ]
    extra_rows = []

    for size in extra_sizes:
        row = { 'size': size }

        for col in df.columns[1:]:
            row[col] = 'NaN'

        extra_rows.append(row)
    
    for row in extra_rows:
        df = pd.concat([df, pd.DataFrame(row, index=[0])])

    df['size'] = [ 1000, 10000, 100000, 5000, 25000, 50000 ]
    df.sort_values('size', inplace = True, ascending=True)

    df = pd.DataFrame(data = df.values, columns= df.columns, dtype='float32')

    for col in df.columns[1:]:
        df[col] = df[col].interpolate(method='spline', order=2, limit_direction='both')

    df['size'] = [ '1k', '5k', '10k', '25k', '50k', '100k' ]

    # pd.options.display.max_columns = None
    # display(df)

    df.set_index('size').plot(title=title)
    plt.savefig(img_path)