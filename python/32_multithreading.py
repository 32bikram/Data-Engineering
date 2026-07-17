import time
import random
from concurrent.futures import ThreadPoolExecutor

tables = ["order","price","address","review","cancelation"]

def fun(x):
    wait = random.randint(1,10)
    time.sleep(wait)
    print(f"{x} took {wait} seconds to execute")

with ThreadPoolExecutor (max_workers=len(tables)) as executor:

    futures = executor.map(fun, tables)

    #OR This way

    # for i in tables:
    #     future = executor.submit(fun,i)