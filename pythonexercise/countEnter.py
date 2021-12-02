f = open('C:/Users/tlgns/OneDrive/바탕 화면/헬로데이터/가공작업대상_211130_34.txt', 'r')
count = 0
while True:
    line = f.readline()
    if not line:
        break
    count += 1
f.close()
print(count)
