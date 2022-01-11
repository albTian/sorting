import numpy as np
import sys
import time
from algorithms import get_algorithms



# Run the outter testing structure
def main():
    # Basic setters
    max_int = 1000000
    # Create integers 1 to 1 billion
    sizes = [10**x for x in range(10)]
    algorithms_list = get_algorithms()
    print(sizes)
    
    # For each array size, 
        # Generate array
        # For each algorithm,
            # Execute with array
            # Display time to complete
        # Find and display max and min for this generated array
    for array_size in sizes:
        test_array = np.random.randint(max_int, size=array_size)
        times_array = []
        
        for test_algorithm, test_name in algorithms_list:
            start = time.time()
            print(f'Testing {test_name} sort ...')
            test_algorithm(test_array)
            end = time.time()
            elapsed = end - start
            print(f'Execution time: {elapsed}s')
            times_array.append((elapsed, test_name))
        
        best = min(times_array, key=lambda tup: tup[0])
        worst = max(times_array, key=lambda tup: tup[0])
        print(f'For array of size {array_size},')
        print(f'{best[1]} is best at {best[0]}s')
        print(f'{worst[1]} is worst at {worst[0]}s')



if __name__ == '__main__':
    main()