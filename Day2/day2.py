def IsValid(input):
    first = True
    asc = False

    for i in range(1, len(input)):
        if first:
            first = False
            asc = input[i] > input[i - 1]
            
        if abs(input[i] - input[i - 1]) > 3:
            return False
        if(input[i] == input[i - 1]):
            return False
        if asc:
            if input[i] < input[i - 1]:
                return False
        else:
            if input[i] > input[i - 1]:
                return False
    
    return True

if __name__ == '__main__':
    # Load from file and iterate over each line
    result = 0

    with open('./input.txt') as f:
        for line in f:
            # Split the line into a list of integers
            b = [int(x) for x in line.split(' ')]
            # Call the IsValid function and print the result
            if IsValid(b):
                result += 1
    
    print(result)