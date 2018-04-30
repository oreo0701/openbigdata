def result(movie_name,movie_score_change):
    index = 0

    # print(movie[0],movie_score_change[0])
    # print(movie[1],movie_score_change[1])

    while index != 10:
        print("{0:^3}".format(index))
        print("{0:^15}".format(movie_name[index]))
        print("{0:^3}".format(movie_score_change[index]))
        index += 1


result(movie_name,movie_score_change)