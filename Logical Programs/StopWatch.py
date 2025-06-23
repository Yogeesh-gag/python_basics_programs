import time  # To access time-related functions

def stopwatch():
    input("Press Enter to start the stopwatch...")
    start_time = time.time()  # Record the start time

    input("Press Enter to stop the stopwatch...")
    end_time = time.time()    # Record the end time

    elapsed_time = end_time - start_time  # Calculate elapsed time

    print(f"\nElapsed Time: {elapsed_time:.2f} seconds")

# Run the stopwatch
stopwatch()

