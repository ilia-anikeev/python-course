import time
import threading
import multiprocessing

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

def sync_fib(n_delay, executions):
    for _ in range(executions):
        fib(n_delay)

def threads_fib(n_delay, thread_count):
    thread_list = []
    for _ in range(thread_count):
        new_thread = threading.Thread(target=fib, args=(n_delay,))
        thread_list.append(new_thread)
        new_thread.start()

    for thread in thread_list:
        thread.join()

def processes_fib(n_delay, process_count):
    process_list = []
    for _ in range(process_count):
        new_process = multiprocessing.Process(target=fib, args=(n_delay,))
        process_list.append(new_process)
        new_process.start()

    for process in process_list:
        process.join()

def execution_timer(function, *params):
    start = time.time()
    function(*params)
    finish = time.time()
    return finish - start

def main_fib():
    fibonacci_n = 24
    runs_count = 10
    timing_results = []

    header = "Fibonacci Execution Time Comparison\n"
    header += "="*42 + "\n"
    header += f"{'n':<10}{'Synchronous':<15}{'Threads':<15}{'Processes':<15}\n"
    header += "-"*55 + "\n"

    for index in range(runs_count):
        sync_duration = execution_timer(sync_fib, fibonacci_n + index, runs_count)
        thread_duration = execution_timer(threads_fib, fibonacci_n + index, runs_count)
        process_duration = execution_timer(processes_fib, fibonacci_n + index, runs_count)

        report_line = (
            f"{fibonacci_n + index:<10}{sync_duration:<15.2f}{thread_duration:<15.2f}{process_duration:<15.2f}\n"
        )
        timing_results.append(report_line)

    with open("../artifacts/1.txt", "w") as report_file:
        report_file.write(header + ''.join(timing_results))
