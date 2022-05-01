''' This module is for converting csv to parquet
'''
import os
import pyarrow.parquet as pq
import pyarrow.csv as pc
import glob
import time

if __name__ == "__main__":
    FILE_NAME = os.environ.get('FILE_NAME_PATTERN')
    COMPRESSION_ALGORITHM = os.environ.get('COMPRESSION_ALGORITHM')
    FLAVOR = os.environ.get('FLAVOR')

    CSV_PATH = '/src/input/'
    PARQUET_PATH = '/src/output/'

    csv_files = glob.glob(CSV_PATH+FILE_NAME)
    
    startTime = time.time()

    for file in csv_files:
        file_name = os.path.basename(file)
        print(f'*** processing {file_name} ***')
        pq.write_table(pc.read_csv(file), PARQUET_PATH+file_name \
            .replace('.csv', '.parquet'), compression=f'{COMPRESSION_ALGORITHM}', flavor=f'{FLAVOR}')
    
    endTime = (time.time() - startTime)
    print(f'Execution took: {endTime}s')
