f = open('C:/Users/tlgns/OneDrive/바탕 화면/헬로데이터/가공작업대상_211130_31.txt', 'r')
count = 0
countZeros = 0
countNum = 0
while True:
    line = f.readline()
    if not line:
        break
    if int(line) == 0:
        countZeros += 1
    else:
        countNum += int(line)
    count += 1
f.close()
print("이미지 수 = ", count)
print("객체 수 = ", countNum)
print("변화건물없음 수 = ", countZeros)
print("객체있는이미지 수 = ", count - countZeros)
