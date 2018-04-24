from bs4 import BeautifulSoup
import urllib.request

html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html, 'html.parser')
# print(soup)
# print(soup.prettify())

tags = soup.find_all('tbody')
# print(tags[0].strings)



# movie_title=soup.select('title')
# print(movie_title)





movie_name =[]
movie_score_change=[]
is_movie = True
for tag in tags[0].strings:
        if tag == '\n':
            pass
        elif is_movie == True:
            movie_name.append(tag)
            is_movie = False
        else:
            movie_score_change.append(tag)
            is_movie = True

print(movie_name)
print(movie_score_change)

