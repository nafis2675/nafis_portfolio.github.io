def calculate_sum_of_squares(nums):
    sum_of_squares = 0
    num_index = 0
    num_len = len(nums)
    
    def calculate_sum_recursive():
        nonlocal sum_of_squares, num_index
        
        if num_index == num_len:
            return
        
        num = nums[num_index]
        if num > 0:
            sum_of_squares += num ** 2
        
        num_index += 1
        calculate_sum_recursive()
    
    calculate_sum_recursive()
    return sum_of_squares

def main():
    num_test_cases = int(input())
    results = []
    test_case_index = 0
    
    def process_test_case():
        nonlocal test_case_index
        
        if test_case_index == num_test_cases:
            return
        
        test_case_index += 1
        
        _ = int(input())  # Ignoring the X value
        
        # Read the space-separated integers and convert them to a list of integers
        integers = list(map(int, input().split()))
        
        # Calculate the sum of squares and append it to the results list
        results.append(calculate_sum_of_squares(integers))
        
        process_test_case()
    
    process_test_case()
    
    # Print the results
    print("\n".join(str(result) for result in results))


if __name__ == "__main__":
    main()
