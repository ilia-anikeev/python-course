import time
import multiprocessing
import codecs
from datetime import datetime

def processor_a(input_queue, output_queue):
    while True:
        if input_queue.empty():
            continue
        msg = input_queue.get()
        output_queue.put(msg.lower())
        time.sleep(5)

def processor_b(input_queue, main_queue_output):
    while True:
        if input_queue.empty():
            continue
        msg = input_queue.get()
        trans_msg = codecs.encode(msg, 'rot_13')
        log_message = (f"Timestamp: {datetime.now()}\n"
                       f"Original Message: {msg}\n"
                       f"Processed Message: {trans_msg}\n"
                       f"{'='*40}\n")
        print(log_message)
        main_queue_output.put(trans_msg)

def main_pipes():
    main_in_out_queue = multiprocessing.Queue()
    queue_from_a = multiprocessing.Queue()
    queue_from_b = multiprocessing.Queue()

    proc_a_work = multiprocessing.Process(target=processor_a, args=(queue_from_a, queue_from_b))
    proc_b_work = multiprocessing.Process(target=processor_b, args=(queue_from_b, main_in_out_queue))

    proc_a_work.start()
    proc_b_work.start()

    try:
        while True:
            input_msg = input()
            print(f"Sending to Processor A: {input_msg}\n{'-'*40}")
            queue_from_a.put(input_msg)
    except KeyboardInterrupt:
        proc_a_work.terminate()
        proc_b_work.terminate()
