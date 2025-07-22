import seaborn as sns
import matplotlib.pyplot as plt

def plot_price_distribution(df):
    sns.histplot(df['price'], kde=True)
    plt.title('Price Distribution')
    plt.xlabel('Price')
    plt.ylabel('Count')
    plt.show()
