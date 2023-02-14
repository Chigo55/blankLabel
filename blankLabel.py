import os
import shutil

def blankLabelGenerator(file_dir, loop):
    for i in range(loop):
        f = open(file_dir + str(i).zfill(6)+'.txt', 'w', encoding='utf-8')
        f.close()

if __name__ == "__main__":
    path = 'C:/Users/user/Desktop/'
    blankLabelGenerator(path ,5)
    print('완료')