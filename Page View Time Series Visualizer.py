import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Install required libraries if not already installed
try:
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
except ImportError:
    !pip install pandas matplotlib seaborn
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns

# Task 1: Import data and set the index
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Task 2: Clean the data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

# Task 3: draw_line_plot function
def draw_line_plot():
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.plot(df.index, df['value'], color='r', linewidth=2)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    plt.show()

# Task 4: draw_bar_plot function
def draw_bar_plot():
    df_bar = df.copy()
    df_bar['Year'] = df_bar.index.year
    df_bar['Month'] = df_bar.index.strftime('%B')

    df_bar = df_bar.groupby(['Year', 'Month']).mean().unstack()

    fig, ax = plt.subplots(figsize=(14, 7))
    df_bar.plot(kind='bar', ax=ax)
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months', labels=df_bar.columns.levels[1])
    plt.show()

# Task 5: draw_box_plot function
def draw_box_plot():
    df_box = df.copy()
    df_box.reset_index(inplace=True)

    df_box['Year'] = [d.year for d in df_box['date']]
    df_box['Month'] = [d.strftime('%b') for d in df_box['date']]

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(18, 6))
    
    sns.boxplot(x='Year', y='value', data=df_box, ax=axes[0])
    sns.boxplot(x='Month', y='value', data=df_box, ax=axes[1], order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')

    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    plt.show()

# Example usage:
draw_line_plot()
draw_bar_plot()
draw_box_plot()
