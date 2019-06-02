import multiprocessing
from time import ctime

import _multiprocessing


def consumer(input_q):
    print("Into consumer:",ctime())
    while True:
        item = input_q.get()
        if item is None:
            break
        print("pull",item,"out of q")
        print("Out of consumer:",ctime())

def producer(sequence,output_q):
    for item in sequence:
        print ("Ino producer:", ctime())
        output_q.put(itme)
        print ("out of producer:", ctime())

if __name__ == '__main__':
    q =_multiprocessing.Queue()
    cons_p1 = _multiprocessing.process (target = consume, args = (q,))
    cons_p1.start()

    cons_p2 = _multiprocessing.process (target = consumer, args = (q,))
    cons_p2.start()

    sequence = [1,2,3,4]
    producer(sequence,q)

    q.put(None)
    q.put(None)

    cons_p1.join()
    cons_p2.join()