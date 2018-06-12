from konlpy.tag import Twitter

twitter = Twitter()

malist = twitter.pos("아버지 가바에 들어가신다.", norm=True, stem=True)

print(malist)