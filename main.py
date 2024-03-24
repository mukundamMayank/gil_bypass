import ctypes
import threading
import time

# Load the shared library
fibonacci_ext = ctypes.CDLL('./hello.so')


# Define the argument and return types for the fibonacci_with_gil and fibonacci_without_gil functions
fibonacci_ext.fibonacci_without_gil.argtypes = [ctypes.c_int]
fibonacci_ext.fibonacci_without_gil.restype = ctypes.py_object
fibonacci_ext.fibonacci_with_gil.argtypes = [ctypes.c_int]
fibonacci_ext.fibonacci_with_gil.restype = ctypes.py_object


def calculate_fibonacci_with_gil():
    start_time = time.time()
    fib_sequence = fibonacci_ext.fibonacci_with_gil(1000)
    end_time = time.time()
    print("Fibonacci with GIL execution time:", end_time - start_time, "seconds")

def calculate_fibonacci_without_gil():
    print(" ########  enter ")
    start_time = time.time()
    fib_sequence = fibonacci_ext.fibonacci_without_gil(1000)
    end_time = time.time()
    print(" ########  exit ")
    print("Fibonacci without GIL execution time:", end_time - start_time, "seconds")

# Create two threads for each calculation
threads = []
for _ in range(2):
    thread_with_gil = threading.Thread(target=calculate_fibonacci_with_gil)
    thread_without_gil = threading.Thread(target=calculate_fibonacci_without_gil)
    threads.extend([thread_with_gil, thread_without_gil])

# Start all threads
for thread in threads:
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()
