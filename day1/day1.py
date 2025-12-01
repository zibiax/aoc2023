from timeit import default_timer as timer

def read_input(input):
    with open(f'{input}.txt', 'r') as f:
        data = f.read().splitlines()
    return data


