# Author: Spencer Lynn Wahlstrom
# Date: 7/25/2022
# Description:
import time

if __name__ == '__main__':
    with open('init_search.txt', 'w') as f:
        f.write('run')
    with open('keyword.txt', 'w') as f:
        f.write('banana')
    time.sleep(6)  # scrape service can be slow due to internet connection, adjust accordingly as needed
    with open('calories.txt', 'r') as f:
        print(f.readline())
        print(f.readline())
    open('calories.txt', 'w').close()

