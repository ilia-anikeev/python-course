from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import multiprocessing
import math
import time

def simple_integrate(math_func, start, end, iterations):
    accumulator = 0
    segment = (end - start) / iterations
    for i in range(iterations):
        accumulator += math_func(start + i * segment) * segment
    return accumulator

def parallel_integrate(math_func, start, end, worker_count, executor_kind=None):
    part_size = 10000000 // worker_count
    future_results = []
    part_results = []

    with executor_kind(max_workers=worker_count) as worker_executor:
        interval = (end - start) / worker_count
        for i in range(worker_count):
            sec_start = start + i * interval
            sec_end = sec_start + interval
            future_results.append(worker_executor.submit(simple_integrate, math_func, sec_start, sec_end, part_size))

        for computed_future in future_results:
            part_results.append(computed_future.result())

    return sum(part_results)

def main_integrate():
    cpu_total = multiprocessing.cpu_count()
    compute_results = []

    header = "Comparison of Integration Execution Times\n\n"
    header += "n_jobs".ljust(10) + "Threads Time (s)".ljust(25) + "Processes Time (s)".ljust(25) + "\n"
    header += "-"*60 + "\n"

    for worker_total in range(1, cpu_total * 2 + 1):
        start_time = time.time()
        result_threads = parallel_integrate(math.cos, 0, math.pi / 2, worker_total, executor_kind=ThreadPoolExecutor)
        elapsed_threads = time.time() - start_time

        start_time = time.time()
        result_processes = parallel_integrate(math.cos, 0, math.pi / 2, worker_total, executor_kind=ProcessPoolExecutor)
        elapsed_processes = time.time() - start_time

        compute_results.append(f"{str(worker_total).ljust(10)}{str(elapsed_threads).ljust(25)}{str(elapsed_processes).ljust(25)}\n")

    with open("../artifacts/2.txt", "w") as results_file:
        results_file.write(header)
        for outcome in compute_results:
            results_file.write(outcome)
