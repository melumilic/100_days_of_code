from asyncio import sleep
import time

# decorator function to measure time for function to run

def measure_runtime(function):
    def run_function_time():
        prev_time = time.time()
        function()
        print(time.time()-prev_time)
    return run_function_time

@measure_runtime
def function_test():
    print("w")

function_test()