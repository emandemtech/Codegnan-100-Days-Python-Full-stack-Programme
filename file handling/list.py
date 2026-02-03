def write_element_info_to_file(lst, filename, target_element=None):
    with open(filename, 'w') as file:
        
        # Mode 1: Only one target
        if target_element is not None:
            count = 0
            indices = []
            
            for i, x in enumerate(lst):
                if x == target_element:
                    count += 1
                    indices.append(i)
            
            file.write(f'Element: {target_element}\n')
            file.write(f'Count: {count}\n')
            file.write(f'Indices: {indices}\n')
        
        # Mode 2: All elements
        else:
            for num in set(lst):
                count = lst.count(num)
                indices = [i for i, x in enumerate(lst) if x == num]
                file.write(f'Element: {num}, Count: {count}, Indices: {indices}\n')


def read_file_content(filename):
    with open(filename, 'r') as file:
        return file.read()


lst = [1,2,3,1,2,3,1,2,3]

# ---- Use case 1: only target = 1
write_element_info_to_file(lst, 'output.txt', target_element=1)
print("Target mode:\n", read_file_content('output.txt'))

# ---- Use case 2: all elements
write_element_info_to_file(lst, 'output.txt')
print("All elements mode:\n", read_file_content('output.txt'))
