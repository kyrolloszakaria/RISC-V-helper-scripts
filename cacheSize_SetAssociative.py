import math

# Global variables
bits = -1
bytes = -1
mode = ''
mem_cap = -1
cache_cap = -1
mem_blocks = -1
cache_lines = -1
block_size = -1
set_number = -1
set_size = -1
word_size = -1
words_per_block = -1

tag_bits = -1
index_bits = -1
offset_bits = -1
tag_dir_size = -1
PA_bits = -1
m_values = []

hit_latency = -1

def convert_to_word_size(value):
    global word_size
    if value == -1:
        return -1
    unit = input("Enter the unit (bit, byte, kb, mb, gb): ")
    if unit == "bit":
        value = value / 8
    elif unit == "byte":
        value = value
    elif unit == "kb":
        value = value * 1024
    elif unit == "mb":
        value = value * 1024 * 1024
    elif unit == "gb":
        value = value * 1024 * 1024 * 1024
    value = value / word_size
    return value


def general_input():
    global bits, bytes, mode, word_size
    word_size = int(input(' enter word size in bytes: '))
 

def generate_possible_m_values():
    global m_values
    for i in range(1, int(cache_lines + 1)):
        if cache_lines % i == 0:
            m_values.append(i)
        # Calculate the possible m_values
    print('The possible m values are: ')
    print(m_values)

def values_input():
    global mem_cap, cache_cap, mem_blocks, cache_lines, block_size, set_number, set_size
    print('Enter what you know from the following. If not known, enter -1:')
    mem_cap = int(input('Please enter the memory capacity: '))
    mem_cap = convert_to_word_size(mem_cap)
    cache_cap = int(input('Please enter the cache capacity: '))
    cache_cap = convert_to_word_size(cache_cap)
    mem_blocks = int(input('Please enter the number of blocks in the memory: '))
    cache_lines = int(input('Please enter the number of lines in the cache: '))
    block_size = int(input('Please enter the block size: '))
    block_size = convert_to_word_size(block_size)
    set_size = int(input('Please enter the set size: '))
    set_number = int(input('Please enter the set number: '))

def PA_input():
    global PA_bits, offset_bits, index_bits, tag_bits, mem_cap, cache_lines, block_size, mem_blocks, set_number
    print('Enter what you know from the following. If not known, enter -1:')
    PA_bits = int(input('Please enter the number of PA_bits: '))
    if PA_bits != -1:
        mem_cap = 2 ** PA_bits
    offset_bits = int(input('Please enter the number of offset_bits: '))
    if offset_bits != -1:
        block_size = 2 ** offset_bits
    index_bits = int(input('Please enter the number of index_bits: '))
    if index_bits != -1:
        set_number = 2 ** index_bits
    tag_bits = int(input('Please enter the number of tag_bits: '))
    if tag_bits != -1 and index_bits != -1:
        mem_blocks = 2 ** (tag_bits + index_bits)

def calculate_value_from_bits():
    global PA_bits, offset_bits, index_bits, tag_bits, mem_cap, cache_lines, block_size, mem_blocks, set_number
    if PA_bits != -1:
        mem_cap = 2 ** PA_bits
    if offset_bits != -1:
        block_size = 2 ** offset_bits
    if tag_bits != -1:
        mem_blocks = 2 ** (tag_bits+index_bits)
    if index_bits != -1:
        set_number = 2 ** index_bits

def calculate_values():
    global mem_cap, cache_cap, mem_blocks, cache_lines,block_size,set_number, set_size
    if mem_cap == -1:
        if mem_blocks != -1 and block_size != -1:
            mem_cap = mem_blocks * block_size
    if cache_cap == -1:
        if cache_lines != -1 and block_size != -1:
            cache_cap = cache_lines * block_size
    if block_size == -1:
        if cache_cap != -1 and cache_lines != -1:
            block_size = cache_cap / cache_lines
        if mem_cap != -1 and mem_blocks != -1:
            block_size = mem_cap / mem_blocks
    if mem_blocks == -1 and mem_cap != -1 and block_size != -1:
        mem_blocks = mem_cap / block_size
    if cache_lines == -1:
        if cache_cap != -1 and block_size != -1:
            cache_lines = cache_cap / block_size
        if set_number != -1 and set_size != -1:
            cache_lines = set_size * set_number
    if set_number == -1:
        if cache_lines != -1 and set_size != -1:
            set_number = cache_lines / set_size
    if set_size == -1:
        if cache_lines != -1 and set_number  != -1:
            set_size = cache_lines / set_number
    if set_number == -1:
        if cache_lines != -1 and set_size  != -1:
            set_number = cache_lines / set_size

# get the PA bits using the values of the cache and memory
def calculate_PA_bits():
    global PA_bits, offset_bits, index_bits, tag_bits, mem_cap, cache_lines, block_size, mem_blocks, set_number
    if PA_bits == -1:
        if mem_cap != -1:
            PA_bits = math.log2(mem_cap)
        if offset_bits != -1 and tag_bits != -1 and index_bits != -1:
            PA_bits = offset_bits + tag_bits + index_bits
        if cache_cap != -1 and set_size != -1 and tag_bits != -1:
            PA_bits = tag_bits + math.log2((cache_cap / set_size))
    if offset_bits == -1:
        if block_size != -1:
            offset_bits = math.log2(block_size)
        if PA_bits != -1 and tag_bits != -1 and index_bits != -1:
            offset_bits = PA_bits - (tag_bits + index_bits)
    if index_bits == -1:
        if set_number != -1:
            index_bits = math.log2(set_number)
        if PA_bits != -1 and tag_bits != -1 and offset_bits != -1:
            index_bits = PA_bits - (tag_bits + offset_bits)
    if tag_bits == -1:
        if mem_blocks != -1 and index_bits != -1:
            tag_bits = PA_bits - offset_bits - index_bits

    
def calculate_tag_dir_size():
    global tag_dir_size, tag_bits, cache_lines
    tag_dir_size = tag_bits * cache_lines
def calculate_words_per_block():
    global word_size, block_size, words_per_block
    words_per_block = block_size / word_size
def print_all_values():
    global bits, bytes, mode, mem_cap, cache_cap, mem_blocks, cache_lines, block_size, tag_bits, index_bits, offset_bits, PA_bits, m_values, tag_dir_size, word_size, words_per_block, hit_latency, set_number, set_size
    print("Values of Global Variables:")
    print(f"NOTE ALL OUTPUTS ARE IN WORD SIZE UNIT WHICH IS {word_size} bytes.")
    # print(f"bits: {bits}")
    # print(f"bytes: {bytes}")
    print(f"mode: {mode}")
    print(f"mem_cap: {mem_cap}")
    print(f"cache_cap: {cache_cap}")
    print(f"mem_blocks: {mem_blocks}")
    print(f"cache_lines: {cache_lines}")
    print(f"block_size: {block_size}")
    print(f"number_of_words_per_block: {words_per_block}")
    print(f"tag_bits: {tag_bits}")
    print(f"index_bits: {index_bits}")
    print(f"offset_bits: {offset_bits}")
    print(f"PA_bits: {PA_bits}")
    print(f"tag_dir_size: {tag_dir_size}")
    print(F"hit_latency: {hit_latency}")
    print(f"m_values: {m_values}")
    print(f"set_size: {set_size}")
    print(f"set_number: {set_number}")
    print(f"type of comparator is {tag_bits} bit comparator")
    print(f"the number of comparator is {set_size} comparators")



def calculate_hit_latency(comparator_latency,OR_latency):
    global hit_latency,tag_bits
    hit_latency = comparator_latency * tag_bits + OR_latency


general_input()
values_input()
PA_input()
calculate_values()
for i in range(5):
    calculate_PA_bits()
calculate_value_from_bits()
for i in range(5):
    calculate_values()
calculate_tag_dir_size()
generate_possible_m_values()
print_all_values()

