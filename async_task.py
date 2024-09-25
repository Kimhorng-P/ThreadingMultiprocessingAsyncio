import asyncio
from generate_numbers import generate_numbers_file

async def async_write_to_file(filename, data, duration):
    print(f"Starting write into {filename} within estimated {duration} seconds")
    await asyncio.sleep(duration)
    with open(filename, 'w') as w:
        for number in data:
            w.write(f"{number}")
    print(f"Finished writing into {filename}")
    pass

async def run_async_tasks():
    num_numbers = 10000
    min_value = 1
    max_value = 9988
    filename = "numbers.txt"
    prime_numbers = generate_numbers_file(filename, num_numbers, min_value, max_value)
    tasks = []
    for i in range(1,4):
        file_names = [f"Prime file {i}.txt"]
    for file_name in file_names:
        duration = 2
        tasks.append(async_write_to_file(file_name, prime_numbers, duration))
    
    await asyncio.gather(*tasks)


    pass
