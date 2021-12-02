def srtn(Processor_num, Burst, Arrival):
    print("srtn입력시작")
    print(Processor_num)
    print(Burst)
    print(Arrival)
    print("srtn입력끝")
    for o in range(len(Burst)):
        Burst[o] = int(Burst[o])
    for o in range(len(Arrival)):
        Arrival[o] = int(Arrival[o])
    Processor_num = int(Processor_num)
    TT = [0 for _ in range(len(Burst))]
    Burst_max = 0
    Burst_copy = list(Burst)
    min_Arrival = min(Arrival)
    for i in Burst:
        Burst_max += i
    Processor = [[0 for _ in range(Burst_max + min_Arrival + Arrival[-1])] for _ in range(Processor_num)]
    i = 0
    q = []
    get_pop = 0
    change_zero = 0
    while True:
        before = len(q)  # 해당 시간에 추가로 삽입된 프로세스가 있는지 확인
        for j in range(len(Arrival)):
            if Arrival[j] == i:
                q.append(j)
        after = len(q)
        for j in range(len(Processor)):
            if after != before:  # 해당 시간에 추가된 프로세스가 있으면
                if Processor[j][i] != 0:  # 만약 현재 시간에 프로세서에 값이 0이면
                    change_zero = Processor[j][i]  # 그때의 프로세스를 저장
                    k = 0
                    while True:
                        if Processor[j][i + k] == change_zero:  # 그 이후 프로세스가 유지되는 길이만큼 0으로 바꿈
                            Processor[j][i + k] = 0
                        else:
                            break  # 프로세스가 바뀌면 끝
                        k += 1
                    Burst_copy[change_zero - 1] = k  # Burst_copy에 그 길이만큼 값을 대입
            if Processor[j][i] == 0:
                min1 = 10000
                for b_len in q:
                    if min1 > Burst_copy[b_len]:
                        min1 = Burst_copy[b_len]
                        get_pop = b_len
                if Burst_copy[get_pop] != 0:
                    num = get_pop
                    for k in range(Burst_copy[num]):
                        if min1 != 10000:
                            Processor[j][i + k] = num + 1
                            TT[num] = i + k + 1
                            Burst_copy[num] = 10000

        count = 0
        for j in Processor:
            for k in j:
                if k != 0:
                    count += 1
        i += 1
        if count == Burst_max:
            break
    for l in range(len(TT)):
        TT[l] -= Arrival[l]
    WT = [0 for _ in range(len(Burst))]
    NTT = [0.0 for _ in range(len(Burst))]
    for l in range(len(TT)):
        WT[l] = TT[l] - Burst[l]
        NTT[l] = TT[l] / Burst[l]
    print("srtn출력시작")
    print(Processor)
    print(WT)
    print(TT)
    print(NTT)
    print("srtn출력끝")
    return Processor, WT, TT, NTT