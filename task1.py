import sys
from timeit import timeit
import random
from sorting_algorithms import insertion_sort, merge_sort, tim_sort

def benchmark_sort(func_name, sizes=[10, 100, 1_000], times=100):
    for size in sizes:
        setup = f"arr = [random.randint(0, {size}) for _ in range({size})]"
        stmt = f"{func_name}(arr)"
        time = timeit(stmt=stmt, setup=setup, number=times, globals=globals())
        print(f"{time:.4f} sec. | {times}x {func_name}() | {size:,} elements")

def main():
    sizes = [10, 100, 1_000, 10_000]
    
    print("=== insertion_sort ===")
    benchmark_sort("insertion_sort", sizes)

    print("=== merge_sort ===")
    benchmark_sort("merge_sort", sizes)
    
    print("=== tim_sort ===")
    benchmark_sort("tim_sort", sizes)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user")
        sys.exit(0)
    except Exception as e:
        print(e)

