from time import time, sleep


class measure_performance:
    def __enter__(self):
        self.start_time = time()
        self.time = self.start_time
        self.benchmark_number = 0
        return self

    def __exit__(self, *exc_args):
        print(f'Finished for: {time() - self.start_time}')

    def benchmark(self, msg=None, restart=False):
        self.benchmark_number += 1
        if not msg:
            msg = f'Benchmark No.{self.benchmark_number}'

        current_time = time()

        print(f'{msg}: {current_time - self.time}')

        if restart:
            self.time = current_time


def main():
    with measure_performance() as p:
        sleep(1)
        p.benchmark('1st step')

        sleep(2)
        p.benchmark('2nd step', restart=True)

        sleep(3)
        p.benchmark(restart=True)

        sleep(4)
        p.benchmark()


if __name__ == '__main__':
    main()
