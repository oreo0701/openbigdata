from bs4 import BeautifulSoup
import urllib.request
import csv
from pandas import DataFrame

def result(movie_name,movie_score_change):
    index = 0

    # print(movie[0],movie_score_change[0])
    # print(movie[1],movie_score_change[1])

    while index != 20:
    #string으로 출력
        print("{0:^4}".format(index + 1), end='')
        print("{0:^30}".format(movie_name[index]), end='')
        print("{0:^4}".format(movie_score_change[index]))
        index += 1



html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html, 'html.parser')



head = soup.tr.text
add_head = head.split('\n')
print("{0:^3}".format(add_head[1])+"{0:^30}".format(add_head[2])+"{0:^6}".format(add_head[3]))

tags = soup.find_all('tbody')
movie_name =[]
movie_score_change=[]
index=0
is_movie = True
rank_list=[]
rank_info=[]

for tag in tags[0].strings:
    if tag == '\n':
        pass
    elif is_movie == True:
        movie_name.append(tag)
        # rank_info.append(movie_name)
        is_movie = False

    else:
        movie_score_change.append(tag)
        # rank_info.append(movie_score_change)
        # rank_list.append(rank_list)
        is_movie = True


# result(movie_name,movie_score_change)


# with open("naver_movie_rank.csv", 'w') as infile:
#     data = (csv.reader(infile))
