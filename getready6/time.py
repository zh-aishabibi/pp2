# import math
import time

# num = float(input("number: "))
# sec = int(input("milliseconds: "))

# print ("square root is ")
# time.sleep(sec/1000)

# print(math.sqrt(num))

# import time

print("⏳ Press Enter to start the stopwatch...")
input()  # Wait for Enter key press
start_time = time.time()  # Start time using time.time()

print("🟢 Stopwatch started! Press Enter again to stop.")
input()  # Wait for Enter key press
end_time = time.time()  # Stop time using time.time()

elapsed_time = end_time - start_time  # Calculate elapsed time
print(f"⏱️ Elapsed time: {elapsed_time:.2f} seconds")

