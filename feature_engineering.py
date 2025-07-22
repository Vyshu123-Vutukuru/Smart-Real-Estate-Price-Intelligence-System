def add_price_per_sqft(df):
    df['price_per_sqft'] = df['price'] / df['area']
    return df
