import time

def count():
    print('one')
    time.sleep(1)
    print('two')
    time.sleep(1)

def main():
    for _ in range(3):
        count()


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    print(f'Time taken to complete the task: {(time.perf_counter() - start):.04f} seconds')
