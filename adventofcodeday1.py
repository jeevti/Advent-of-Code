zerocounter = 0
score = 50
with open("input") as f:
    data = f.read().splitlines()
# print(data)
def split_term(s):
    return s[0], int(s[1:])

for i in data:
    letter, num = split_term(i)
    if letter=='R':
        score=(score+num) % 100
        # print(score)
    if letter=='L':
        score=(score-num) %100
        # print(score)
    if score==0:
        zerocounter+=1
        print(zerocounter)

    
    
