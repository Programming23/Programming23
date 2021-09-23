from heapq import merge
from itertools import count, islice
import os
import glob
from contextlib import ExitStack  # not available on Python 2
                                  # need to care for closing files otherwise

chunk_names = []

# chunk and sort
with open('1 - Input Folder/Domains.txt') as input_file:
    for chunk_number in count(1):
        # read in next 50k lines and sort them
        sorted_chunk = sorted(islice(input_file, 50000))
        if not sorted_chunk:
            # end of input
            break

        chunk_name = 'chunk_{}.chk'.format(chunk_number)
        chunk_names.append(chunk_name)
        with open(chunk_name, 'w') as chunk_file:
            chunk_file.writelines(sorted_chunk)

with ExitStack() as stack, open('2 - Output Folder/output.txt', 'w') as output_file:
    files = [stack.enter_context(open(chunk)) for chunk in chunk_names]
    output_file.writelines(merge(*files))

files = glob.glob("*.chk")
for i in files:
	os.unlink(i)