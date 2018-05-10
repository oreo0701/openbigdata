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
index = 1
for tag in tags[0].strings:
    if tag == '\n':
        pass
    elif is_movie == True:
        rank_info.append(index)
        rank_info.append(tag)
        is_movie = False
    else:
        rank_info.append(tag)
        rank_list.append(rank_info)
        print(rank_info)
        rank_info=[]
        is_movie = True
        index +=1

movie_table = DataFrame(rank_list, columns=('rank','movie name','movie rank change'))
movie_table.to_csv('naver_movie_rank.csv', encoding="cp949",mode='w',index=False)

# result(movie_name,movie_score_change)


# with open("naver_movie_rank.csv", 'w') as infile:
#     data = (csv.reader(infile))
