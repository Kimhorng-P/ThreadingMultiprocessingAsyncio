import threading
import time

def simulate_io_task(file_name, duration):
  print(f"Starting I/O task for {file_name} within estimated time {duration}")
  time.sleep(2)
  print(f"I/O task completed for {file_name}")
  pass

def run_io_tasks():
  files = ["file1.txt", "file2.txt", "file3.txt"]
  durations = [3, 4, 5]
  threads = []
  for i in range(len(files)):
    thread = threading.Thread(target = simulate_io_task, args=(files[i], durations[i]) )
    threads.append(thread)
  # start thread
  for thread in threads:
    thread.start()
  # wait all thread before finished 
  for thread in threads:
    thread.join()
  # print 
  print("I/O task completed")
  pass
