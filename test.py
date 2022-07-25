# Author: Spencer Lynn Wahlstrom
# Date: 7/25/2022
# Description:
import time

if __name__ == '__main__':
    with open('init_search.txt', 'w') as f:
        f.write('run')
    with open('keyword.txt', 'w') as f:
        f.write('blue cheese')
    time.sleep(5)
    with open('calories.txt', 'r') as f:
        print(f.readline())
        print(f.readline())

