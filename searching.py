import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)

    with open (file_name, "r") as file:
        my_dict = json.load(file)
    my_keys = my_dict.keys()

    if field not in my_keys:
        return None
    else:
        return my_dict[field]

def linear_search(sequence, number):
    """
    :param sequence:
    :param number:
    :return:
    """

    positions = []
    for idx, num in enumerate(sequence):
        if num == number:
            positions.append(idx)
        else:
            pass
    return {'positions':positions, 'count':len(positions)}

def pattern_search(sequence, pattern):
    """
    :param sequence:
    :param pattern:
    :return:
    """
    list_of_positions = set()
    size = len(sequence)
    window = len(pattern)
    end = size - window + 1

    for num in range(0, end):
        partial_seq = sequence[num:num+window]
        if partial_seq == pattern:
            list_of_positions.add(int(num + window/2))
        else:
            pass
    return list_of_positions



def main():
    sequence = read_data("sequential.json", "dna_sequence")
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)

    print(pattern_search(sequence, "ATA"))
    pass



if __name__ == '__main__':
    main()