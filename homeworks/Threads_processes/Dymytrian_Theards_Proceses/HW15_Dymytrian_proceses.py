from math import sqrt
import time
from multiprocessing import Process

def quadr_equation1(a, b, c):
    D = b ** 2 - 4 *a *c
    if D > 0:
        x1 = (-b + sqrt(D)) / (2 * a)
        x2 = (-b - sqrt(D)) / (2 * a)
        print('x1=',x1)
        print('x2=',x2)
    elif D == 0:
        x = (-b) / (2 * a)
        print('x=',x)
    else:
        print('Дане рівняння не має розвязків в множині дійсних чисел')
    time.sleep(1)

def quadr_equation2(a1, b1, c1):
    D1 = b1 ** 2 - 4 *a1 *c1
    if D1 > 0:
        x1 = (-b1 + sqrt(D1)) / (2*a1)
        x2 = (-b1 - sqrt(D1)) / (2*a1)
        print('x1=',x1)
        print('x2=',x2)
    elif D1 == 0:
        x = (-b1) / (2 * a1)
        print('x=',x)
    else:
        print('Дане рівняння не має дійсних коренів')
    time.sleep(1)

start1 = time.time()
quadr_equation1(6, 1, 35)
quadr_equation2(5, 2, 9)
print(f'Single process total time: {time.time() - start1}')

process_1 = Process(target=quadr_equation1)
process_2 = Process(target=quadr_equation2)
start_2 = time.time()
process_1.start()
process_2.start()

process_1.join()
process_2.join()
print(f'Ttotal time: {time.time() - start_2}')
