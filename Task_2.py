from itertools import product

def maximize_it():
    import sys
    data = sys.stdin.read().splitlines()
    
    if not data:
        return 0
    
    first_line = data[0].split()
    K = int(first_line[0])
    M = int(first_line[1])
    
    lists = []
    for i in range(1, K + 1):
        line = data[i].split()
        n = int(line[0])
        elements = list(map(int, line[1:1+n]))
        lists.append(elements)
    
    max_value = 0
    
    # Generate all possible combinations
    for combination in product(*lists):
        total = sum(x*x for x in combination)
        current = total % M
        if current > max_value:
            max_value = current
    
    print(max_value)

# To run with sample input, you can use:
# echo "3 1000\n2 5 4\n3 7 8 9\n5 5 7 8 9 10" | python script.py
maximize_it()