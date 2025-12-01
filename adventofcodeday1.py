zerocounter = 0
score = 50
with open("input") as f:
    data = f.read().splitlines()
# print(data)
def split_term(s):
    return s[0], int(s[1:])

for i in data:
    letter, num = split_term(i)
    if num>99:
        full = num//100
        num = num%100
        zerocounter+=full
    if letter=='R':
        if (score+num)>99 and (score+num)%100!=0:
            zerocounter+=1
            # print("r",num)
        score=(score+num) % 100
        # print(score)
    if letter=='L':
        if (score-num)<0 and score!=0:
            zerocounter+=1
            # print("l",num)
        score=(score-num) %100
        # print(score)
    if score==0:
        zerocounter+=1
        # print(zerocounter)
print(zerocounter)