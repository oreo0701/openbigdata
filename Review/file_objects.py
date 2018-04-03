with open('test.txt', 'r') as rf:
    #
    # size_to_read = 10
    # f_contents = f.read(size_to_read)
    #
    # # while len(f_contents) > 0:
    # #     print(f_contents, end='*')
    # #     f_contents = f.read(size_to_read)
    #
    # # print(f_contents, end='*')
    # #
    # # f.seek(0)
    # #
    # # f_contents = f.read(size_to_read)
    # # print(f_contents, end='*')
    #
    # # print(f.tell())

    # f.write('Test')
    # f.seek(0)
    # f.write('R')
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            chunk_size = 4096
            rf_chunk = rf.read(chunk_size)
            while len(rf_chunk) > 0:
                wf.write(rf_chunk)
                rf_chunk = rf.read(chunk_size)
