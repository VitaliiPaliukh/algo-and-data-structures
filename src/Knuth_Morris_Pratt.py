def build_prefix_suffix_array(pattern):
    pattern_length = len(pattern)
    pattern_index = 1
    prefix_suffix_index = 0
    prefix_suffix = [0] * pattern_length
    while pattern_index < pattern_length:
        if pattern[pattern_index] == pattern[prefix_suffix_index]:
            prefix_suffix_index += 1
            prefix_suffix[pattern_index] = prefix_suffix_index
            pattern_index += 1
        else:
            if prefix_suffix_index != 0:
                prefix_suffix_index = prefix_suffix[prefix_suffix_index - 1]
            else:
                prefix_suffix[pattern_index] = 0
                pattern_index += 1
    return prefix_suffix
    

def knuth_morris_pratt_search(string, pattern):
    index_in_string, index_in_pattern = 0, 0
    string_length = len(string)
    pattern_length = len(pattern)
    if pattern_length == 0:
        return 0
    prefix_suffix_array = build_prefix_suffix_array(pattern)
    while index_in_string < string_length:
        if string[index_in_string] == pattern[index_in_pattern]:
            index_in_pattern += 1
            index_in_string += 1
            if index_in_pattern == pattern_length:
                return index_in_string - index_in_pattern
        else:
            if index_in_pattern == 0:
                index_in_string += 1
            else:
                index_in_pattern = prefix_suffix_array[index_in_pattern - 1]
    return -1
