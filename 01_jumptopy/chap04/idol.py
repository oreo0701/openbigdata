f = open(".\\연습생.txt","r", encoding='UTF8')
candidate_list = f.read()
f.close()

def show_candidate():
    str(candidate_list,end='')

show_candidate()
