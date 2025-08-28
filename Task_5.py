def matrix_script():
    import re
    
    # Read input
    first_line = input().split()
    n = int(first_line[0])
    m = int(first_line[1])
    
    matrix = []
    for _ in range(n):
        matrix_item = input()
        matrix.append(matrix_item)
    
    # Read columns from top to bottom, left to right
    decoded = ''
    for col in range(m):
        for row in range(n):
            decoded += matrix[row][col]
    
    # Replace non-alphanumeric characters between alphanumeric characters with space
    # Using regex to avoid if conditions
    pattern = r'([A-Za-z0-9])([^A-Za-z0-9]+)([A-Za-z0-9])'
    result = re.sub(pattern, r'\1 \3', decoded)
    
    print(result)

# Run the matrix script decoder
matrix_script()