# Sorting Algorithms Performance Comparison

## Description

A program for empirical comparison of the performance of three sorting algorithms:
- **Insertion Sort**
- **Merge Sort**
- **Timsort** (hybrid algorithm used in Python)

The program measures the execution time of each algorithm on arrays of different sizes using the `timeit` module.

## Project Structure

```
04_homework/
├── task1.py                     # Main file with benchmarks
├── sorting_algorithms/          # Module with algorithm implementations
│   ├── __init__.py
│   ├── insertion_sort.py        # O(n²) - quadratic complexity
│   ├── merge_sort.py            # O(n log n) - linearithmic complexity
│   └── tim_sort.py              # O(n log n) - optimized hybrid
└── README.md
```

## Algorithms

### 1. Insertion Sort
- **Time Complexity:**
  - Best case: O(n) - for sorted data
  - Average case: O(n²)
  - Worst case: O(n²) - for reverse-sorted data
- **Space Complexity:** O(1)
- **Advantages:** Simple, efficient on small arrays
- **Disadvantages:** Slow on large arrays

### 2. Merge Sort
- **Time Complexity:**
  - All cases: O(n log n)
- **Space Complexity:** O(n)
- **Advantages:** Stable, predictable performance
- **Disadvantages:** Requires additional memory

### 3. Timsort
- **Time Complexity:**
  - Best case: O(n) - for nearly sorted data
  - Average/worst case: O(n log n)
- **Space Complexity:** O(n)
- **Advantages:** Optimized for real-world data, used in Python
- **Disadvantages:** Complex implementation

## Installation and Running

### Requirements
- Python 3.8+
- All dependencies are Python standard libraries

### Running

```bash
# Run performance tests
python task1.py
```

## How the Program Works

### 1. Test Data Generation
For each test, an array of random integers is created:
```python
arr = [random.randint(0, size) for _ in range(size)]
```

### 2. Time Measurement
The `timeit` module is used for accurate time measurement:
- Each test is executed **100 times** (for small arrays) or fewer (for large ones)
- Total execution time of all iterations is measured
- Results are displayed in seconds

### 3. Test Array Sizes
- **10 elements** - minimum size
- **100 elements** - small size
- **1,000 elements** - medium size
- **10,000 elements** - large size

## Sample Output

```
=== insertion_sort ===
0.0003 sec. | 100x insertion_sort() | 10 elements
0.0285 sec. | 100x insertion_sort() | 100 elements
2.7854 sec. | 100x insertion_sort() | 1,000 elements
278.5421 sec. | 100x insertion_sort() | 10,000 elements

=== merge_sort ===
0.0012 sec. | 100x merge_sort() | 10 elements
0.0145 sec. | 100x merge_sort() | 100 elements
0.1823 sec. | 100x merge_sort() | 1,000 elements
2.1547 sec. | 100x merge_sort() | 10,000 elements

=== tim_sort ===
0.0001 sec. | 100x tim_sort() | 10 elements
0.0018 sec. | 100x tim_sort() | 100 elements
0.0254 sec. | 100x tim_sort() | 1,000 elements
0.3125 sec. | 100x tim_sort() | 10,000 elements
```

## Conclusions

### Performance
1. **Small arrays (< 100 elements):** All algorithms work fast, difference is negligible
2. **Medium arrays (100-1000 elements):** Timsort shows best results
3. **Large arrays (> 1000 elements):** 
   - Insertion Sort slows down significantly (quadratic complexity)
   - Merge Sort is stable
   - Timsort is most efficient

### Recommendations
- For **small arrays (< 50):** Insertion Sort is efficient enough
- For **large arrays:** Use Timsort (built-in `sorted()` in Python)
- For **guaranteed performance:** Merge Sort

## Program Modification

### Changing test array sizes
```python
sizes = [50, 500, 5_000, 50_000]  # Different sizes
```

### Changing number of iterations
```python
benchmark_sort("insertion_sort", sizes, times=1000)  # 1000 iterations
```

### Adding your own algorithm
1. Create a file in `sorting_algorithms/`
2. Add import to `__init__.py`
3. Add call in `main()` function

## Technical Details

### Using timeit
```python
timeit(
    stmt="func(arr)",           # Code to test
    setup="arr = [...]",        # Data preparation
    number=100,                 # Number of iterations
    globals=globals()           # Access to global variables
)
```

## Author

Project created for studying and comparing sorting algorithms as part of the "Basic Algorithms and Data Structures" course.

## License

Educational project - free to use.

