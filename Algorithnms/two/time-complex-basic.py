# coding=utf-8
import time

if __name__ == '__main__':
    '''O(n),数据规模以10倍增长，用时也是10倍增长'''
    for i in range(1,10):
        n = pow(10,i)
        start = time.time()
        sum = 0
        for i in range(0,n):
            sum+=1
        print("%d的规模，用时%s" %(n,time.time()-start))
