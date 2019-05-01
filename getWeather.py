



for chunk in pd.read_csv(filename, chunksize=chunksize):
    process(chunk)


def process(chunk):
    
