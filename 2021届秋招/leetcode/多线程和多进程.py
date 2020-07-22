from multiprocessing import Pool
def show(num):
    print('num : ' + str(num))

if __name__=="__main__":
    pool = Pool(processes = 3)
    for i in range(6):
        # 维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去
        pool.apply_async(show, args=(i, ))
    print('======  apply_async  ======')
    pool.close()
    #调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
    pool.join()