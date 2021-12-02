from tkinter import *
from tkinter import ttk
from functools import partial
from queue import Queue
import random
import math


def choose(pro_num, algo, quant, name, AT, BT):  # 프로세서 수, 알고리즘, 타임 퀀텀, 프로세스 이름, AT, BT를 입력해서 알고리즘에 맞는 함수를 찾아감
    if algo == 'FCFS':  # 알고리즘이 FCFS이면 fcfs 함수에 필요한 매개변수 넣고 돌림
        return fcfs(pro_num, BT, AT)
    elif algo == 'RR':
        return rr(pro_num, BT, AT, quant)  # rr은 타임 퀀텀도 매개변수로 받아야 함
    elif algo == 'RR_C':
        return rr_changed(pro_num, BT, AT, quant)  # rr은 타임 퀀텀도 매개변수로 받아야 함
    elif algo == 'SPN':
        return spn(pro_num, BT, AT)
    elif algo == 'SRTN':
        return srtn(pro_num, BT, AT)
    elif algo == 'SRTN_C':
        return srtn_changed(pro_num, BT, AT)
    elif algo == 'HRRN':
        return hrrn(pro_num, BT, AT)
    elif algo == 'HEUG':
        return hyeokgi(pro_num, BT, AT)


def fcfs(Processor_num, Burst, Arrival):  # fcfs 시작
    print("fcfs입력시작")
    print(Processor_num)
    print(Burst)
    print(Arrival)
    print("fcfs입력끝")
    TT = [0 for _ in range(len(Burst))]  # TT 저장할 변수 선언, Burst랑 길이 같음, 0으로 초기화
    for o in range(len(Burst)):  # Burst랑 Arrival, 그리고 프로세서 수 str 형태이므로 int형으로 변경
        Burst[o] = int(Burst[o])
    for o in range(len(Arrival)):
        Arrival[o] = int(Arrival[o])
    Processor_num = int(Processor_num)
    Burst_max = 0  # Burst의 길이를 모두 합한 값 저장할 공간
    min_Arrival = min(Arrival)  # 도착시간 중에 가장 짧은거(이만큼 Processor의 길이를 늘려줘야 index out of range X)
    for i in Burst:
        Burst_max += i  # Burst 값 모두 합침(이만큼 Processor의 길이를 늘려줘야 index out of range X)
    Processor = [[0 for _ in range(Burst_max + min_Arrival + Arrival[-1])] for _ in
                 range(Processor_num)]  # (0으로 초기화)min_Arrival이랑 Burst_max 더한 후 가장 늦게 도착한 값 더한 길이를 만듬
    i = 0  # i는 1씩 증가(초 단위)
    q = Queue()  # FCFS이므로 Queue로 가능
    while True:
        for j in range(len(Arrival)):  # 만약 Arrival가 i이면 queue에 추가
            if Arrival[j] == i:
                q.put(j)
        for j in range(len(Processor)):
            if Processor[j][i] == 0:  # Processor의 현재 시간(i)에 값이 0이면(초기화되어있으면) 시행
                if not q.empty():  # queue에 값이 있으면
                    num = q.get()  # queue에 있는 값 하나 빼고 그걸 이용
                    for k in range(Burst[num]):  # 해당 프로세서에 해당 시간부터 시작해서 Burst의 길이만큼 삽입
                        Processor[j][i + k] = num + 1
                        TT[num] = i + k + 1  # TT는 현재 시간 + Burst의 길이 + 1
        count = 0
        for j in Processor:  # count는 Processor에 0이 아닌 값의 개수
            for k in j:
                if k != 0:
                    count += 1
        i += 1
        if count == Burst_max:  # Burst의 총 길이와 count가 같으면 끝
            break
    for l in range(len(TT)):  # TT, WT, NTT 선언 + 값 대입
        TT[l] -= Arrival[l]
    WT = [0 for _ in range(len(Burst))]
    NTT = [0.0 for _ in range(len(Burst))]
    for l in range(len(TT)):
        WT[l] = TT[l] - Burst[l]
        NTT[l] = TT[l] / Burst[l]
    print("fcfs출력시작")
    print(Processor)
    print(WT)
    print(TT)
    print(NTT)
    print("fcfs출력끝")
    return Processor, WT, TT, NTT  # 이차원 배열로 프로세서 반환, WT, TT, NTT는 1차원 리스트로 반환



def rr(Processor_num, Burst, Arrival, Quant):
    print("rr입력시작")
    print(Processor_num)
    print(Burst)
    print(Arrival)
    print(Quant)
    print("rr입력끝")
    for o in range(len(Burst)):
        Burst[o] = int(Burst[o])
    for o in range(len(Arrival)):
        Arrival[o] = int(Arrival[o])
    Processor_num = int(Processor_num)
    Quant = int(Quant)  # 타임 퀀텀도 정수로 변경
    TT = [0 for _ in range(len(Burst))]
    Burst_copy = list(Burst)  # Burst값을 rr에서는 변경해줘야 하는데, 이러면 Burst가 바뀌니깐 Burst_copy을 만들어서 Burst_copy을 변경 및 사용
    Burst_max = 0
    max_Q = 0
    min_Arrival = min(Arrival)
    for i in Burst:
        Burst_max += i
    Processor = [[0 for _ in range(Burst_max + min_Arrival + Arrival[-1])] for _ in range(Processor_num)]
    time = [-1 for _ in range(len(Processor))]
    i = 0
    num = [-1,-1,-1,-1]
    q = Queue()
    while True:
        for j in range(len(Arrival)):
            if Arrival[j] == i:
                q.put(j)
        for j in range(len(Processor)):
            if Processor[j][i] == 0 and time[j] < 0:

                if i != 0 and Burst_copy[num[j]] != 0 and num[j] != -1:  # Burst_copy의 길이가 0이 아니고 0초가 아니면
                    q.put(num[j])  # Burst_copy의 값이 남아있으므로 다시 queue에 넣음
                if not q.empty():
                    num[j] = q.get()
                    if Quant > Burst_copy[num[j]]:  # Quant의 길이가 Burst_copy보다 길면
                        max_Q = Burst_copy[num[j]]  # Burst_copy를 사용하고
                        Burst_copy[num[j]] = 0  # 0으로 초기화]
                    else:
                        max_Q = Quant  # 그 반대면 Quant의 길이를 사용하고
                        Burst_copy[num[j]] -= Quant  # Burst_copy의 길이에서 Quant의 길이만큼 뺌
                    for k in range(max_Q):
                        Processor[j][i + k] = num[j] + 1
                        TT[num[j]] = i + k + 1
                    time[j] = max_Q - 1
            # # # # # # # if i != 0:
            # # # # # # #     for j in range(len(Processor)):
            # # # # # # #         for k in range(j+1,len(Processor)):
            # # # # # # #             getnum1 = 0
            # # # # # # #             getnum2 = 0

            # # # # # # #             if Processor[j][i-1] == Processor[k][i] and Processor[j][i-1] != 0:
            # # # # # # #                 change3 = Processor[j][i]
            # # # # # # #                 change4 = Processor[k][i]
            # # # # # # #                 while True:
            # # # # # # #                     if Processor[j][i+getnum1] != 0:
            # # # # # # #                         Processor[j][i+getnum1] = 0
            # # # # # # #                         getnum1 += 1
            # # # # # # #                     else :
            # # # # # # #                         break
            # # # # # # #                 while True:
            # # # # # # #                     if Processor[k][i+getnum2] != 0:
            # # # # # # #                         Processor[k][i+getnum2] = 0
            # # # # # # #                         getnum2 += 1
            # # # # # # #                     else :
            # # # # # # #                         break
            # # # # # # #                 for l in range(getnum1):
            # # # # # # #                     Processor[k][i+l] = change3
            # # # # # # #                 for l in range(getnum2):
            # # # # # # #                     Processor[j][i+l] = change4
        count = 0
        for j in Processor:
            for k in j:
                if k != 0:
                    count += 1
        for j in range(len(time)):
            time[j] -= 1
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
    print("rr출력시작")
    print(Processor)
    print(WT)
    print(TT)
    print(NTT)
    print("rr출력끝")
    return Processor, WT, TT, NTT


def rr_changed(Processor_num, Burst, Arrival, Quant):
    print("rr입력시작")
    print(Processor_num)
    print(Burst)
    print(Arrival)
    print(Quant)
    print("rr입력끝")
    for o in range(len(Burst)):
        Burst[o] = int(Burst[o])
    for o in range(len(Arrival)):
        Arrival[o] = int(Arrival[o])
    Processor_num = int(Processor_num)
    Quant = int(Quant)  # 타임 퀀텀도 정수로 변경
    TT = [0 for _ in range(len(Burst))]
    Burst_copy = list(Burst)  # Burst값을 rr에서는 변경해줘야 하는데, 이러면 Burst가 바뀌니깐 Burst_copy을 만들어서 Burst_copy을 변경 및 사용
    Burst_max = 0
    max_Q = 0
    min_Arrival = min(Arrival)
    for i in Burst:
        Burst_max += i
    Processor = [[0 for _ in range(Burst_max + min_Arrival + Arrival[-1])] for _ in range(Processor_num)]
    time = [-1 for _ in range(len(Processor))]
    i = 0
    num = [-1,-1,-1,-1]
    q = Queue()
    while True:
        for j in range(len(Arrival)):
            if Arrival[j] == i:
                q.put(j)
        for j in range(len(Processor)):
            if Processor[j][i] == 0 and time[j] < 0:

                if i != 0 and Burst_copy[num[j]] != 0 and num[j] != -1:  # Burst_copy의 길이가 0이 아니고 0초가 아니면
                    q.put(num[j])  # Burst_copy의 값이 남아있으므로 다시 queue에 넣음
                if not q.empty():
                    num[j] = q.get()
                    if Quant > Burst_copy[num[j]]:  # Quant의 길이가 Burst_copy보다 길면
                        max_Q = Burst_copy[num[j]]  # Burst_copy를 사용하고
                        Burst_copy[num[j]] = 0  # 0으로 초기화]
                    else:
                        max_Q = Quant  # 그 반대면 Quant의 길이를 사용하고
                        Burst_copy[num[j]] -= Quant  # Burst_copy의 길이에서 Quant의 길이만큼 뺌
                    for k in range(max_Q):
                        Processor[j][i + k] = num[j] + 1
                        TT[num[j]] = i + k + 1
                    time[j] = max_Q - 1
            if i != 0:
                for j in range(len(Processor)):
                    for k in range(j+1,len(Processor)):
                        getnum1 = 0
                        getnum2 = 0

                        if Processor[j][i-1] == Processor[k][i] and Processor[j][i-1] != 0:
                            change3 = Processor[j][i]
                            change4 = Processor[k][i]
                            while True:
                                if Processor[j][i+getnum1] != 0:
                                    Processor[j][i+getnum1] = 0
                                    getnum1 += 1
                                else :
                                    break
                            while True:
                                if Processor[k][i+getnum2] != 0:
                                    Processor[k][i+getnum2] = 0
                                    getnum2 += 1
                                else :
                                    break
                            for l in range(getnum1):
                                Processor[k][i+l] = change3
                            for l in range(getnum2):
                                Processor[j][i+l] = change4
        count = 0
        for j in Processor:
            for k in j:
                if k != 0:
                    count += 1
        for j in range(len(time)):
            time[j] -= 1
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
    print("rr출력시작")
    print(Processor)
    print(WT)
    print(TT)
    print(NTT)
    print("rr출력끝")
    return Processor, WT, TT, NTT




def spn(Processor_num, Burst, Arrival):
    print("spn입력시작")
    print(Processor_num)
    print(Burst)
    print(Arrival)
    print("spn입력끝")
    TT = [0 for _ in range(len(Burst))]
    for o in range(len(Burst)):
        Burst[o] = int(Burst[o])
    for o in range(len(Arrival)):
        Arrival[o] = int(Arrival[o])
    Processor_num = int(Processor_num)
    Burst_max = 0
    Burst_copy = list(Burst)
    min_Arrival = min(Arrival)
    for i in Burst:
        Burst_max += i
    Processor = [[0 for _ in range(Burst_max + min_Arrival + Arrival[-1])] for _ in range(Processor_num)]
    i = 0
    q = []  # spn은 queue를 사용해서 해결 못하므로 리스트로 만듬
    get_pop = 0
    while True:
        for j in range(len(Arrival)):
            if Arrival[j] == i:
                q.append(j)
        for j in range(len(Processor)):
            if Processor[j][i] == 0:
                min1 = 10000  # 비교를 위해 min1을 10000으로 초기화
                for b_len in q:
                    if min1 > Burst_copy[b_len]:  # Burst_copy의 값이 더 작으면 Burst_copy값 사용
                        min1 = Burst_copy[b_len]
                        get_pop = b_len  # 그때의 인덱스 값 저장
                if Burst_copy[get_pop] != 0:  # Burst_copy의 값이 0이 아니면 실행
                    num = get_pop
                    for k in range(Burst_copy[num]):
                        if min1 != 10000:  # 만약 min1 값이 아니면 10000이면 실행
                            Processor[j][i + k] = num + 1
                            TT[num] = i + k + 1
                            Burst_copy[num] = 10000  # Burst_copy를 사용 후 10000으로 초기화해서 다음에는 이 조건문에 못 들어오게 함

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
    print("spn출력시작")
    print(Processor)
    print(WT)
    print(TT)
    print(NTT)
    print("spn출력끝")
    return Processor, WT, TT, NTT




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
        if count == Burst_max:
            break
        i += 1
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






def srtn_changed(Processor_num, Burst, Arrival):
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
            if i != 0:
                for j in range(len(Processor)):
                    for k in range(j+1,len(Processor)):
                        getnum1 = 0
                        getnum2 = 0

                        if Processor[j][i-1] == Processor[k][i] and Processor[j][i-1] != 0:
                            change3 = Processor[j][i]
                            change4 = Processor[k][i]
                            while True:
                                if Processor[j][i+getnum1] != 0:
                                    Processor[j][i+getnum1] = 0
                                    getnum1 += 1
                                else :
                                    break
                            while True:
                                if Processor[k][i+getnum2] != 0:
                                    Processor[k][i+getnum2] = 0
                                    getnum2 += 1
                                else :
                                    break
                            for l in range(getnum1):
                                Processor[k][i+l] = change3
                            for l in range(getnum2):
                                Processor[j][i+l] = change4

        count = 0
        for j in Processor:
            for k in j:
                if k != 0:
                    count += 1
        if count == Burst_max:
            break
        i += 1
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




def hrrn(Processor_num, Burst, Arrival):
    print("hrrn입력시작")
    print(Processor_num)
    print(Burst)
    print(Arrival)
    print("hrrn입력끝")
    for o in range(len(Burst)):
        Burst[o] = int(Burst[o])
    for o in range(len(Arrival)):
        Arrival[o] = int(Arrival[o])
    Processor_num = int(Processor_num)
    TT = [0 for _ in range(len(Burst))]
    WT = [0 for _ in range(len(Burst))]  # hrrn은 WT도 있으므로 만듬
    visited = [False for _ in range(len(Burst))]
    Burst_max = 0
    Burst_copy = list(Burst)
    min_Arrival = min(Arrival)
    for i in Burst:
        Burst_max += i
    Processor = [[0 for _ in range(Burst_max + min_Arrival + Arrival[-1])] for _ in range(Processor_num)]
    i = 0
    q = []
    get_pop = 0
    while True:
        for j in range(len(Arrival)):
            if Arrival[j] == i:
                q.append(j)
                visited[j] = True  # q를 추가할때마다 WT도 추가
        for j in range(len(Processor)):
            if Processor[j][i] == 0:
                max1 = -1  # max를 -1로 초기화해서 사용
                for b_len in q:
                    if max1 < (Burst_copy[b_len] + WT[b_len]) / Burst_copy[b_len]:  # (BT + WT/ BT)
                        max1 = (abs(Burst_copy[b_len]) + WT[b_len]) / Burst_copy[b_len]
                        get_pop = b_len
                if Burst_copy[get_pop] != 0:
                    num = get_pop
                    for k in range(Burst_copy[num]):
                        if max1 != -1:
                            Processor[j][i + k] = num + 1
                            TT[num] = i + k + 1
                            Burst_copy[num] = -1  # -1로 초기화해놓으면 다음에 사용하게 될때 -1보다 크게 됨

        count = 0
        for j in Processor:
            for k in j:
                if k != 0:
                    count += 1
        i += 1
        for j in range(len(WT)):  # 1초 지날때마다 WT도 증가
            if visited[j]:
                WT[j] += 1
        if count == Burst_max:
            break
    for l in range(len(TT)):
        TT[l] -= Arrival[l]
    WT = [0 for _ in range(len(Burst))]
    NTT = [0.0 for _ in range(len(Burst))]
    for l in range(len(TT)):
        WT[l] = TT[l] - Burst[l]
        NTT[l] = TT[l] / Burst[l]
    print("hrrn출력시작")
    print(Processor)
    print(WT)
    print(TT)
    print(NTT)
    print("hrrn출력끝")
    return Processor, WT, TT, NTT



def hyeokgi(processor_num, BT, AT):
    print('hyeokgi 시작')
    for o in range(len(BT)):  # Burst랑 Arrival, 그리고 프로세서 수 str 형태이므로 int형으로 변경
        BT[o] = int(BT[o])
    for o in range(len(AT)):
        AT[o] = int(AT[o])
    processor_num = int(processor_num)
    get_proc_num = len(AT)
    proc_list = [[0 for _ in range(7)] for _ in range(get_proc_num)]        # 데이터 저장을 위한 프로세스 리스트(TT와 NTT는 따로 저장)
    visited = [0 for _ in range(get_proc_num)]                              # 프로세서에서 작정중인지 확인
    proc_schedule = [[] for _ in range(processor_num)]                      # 스케줄링 리스트
    unable_proc_num = 0                                                     # BT가 0인 프로세스 개수
    schedule_count = 0                                                      # 스케줄링 진행 시간

    for i in range(get_proc_num):                     # 프로세스 입력
        proc_list[i][0] = i + 1                       # 각 프로세스 index(0)에 번호 부여
        proc_list[i][1], proc_list[i][2] = AT[i], BT[i]

    while unable_proc_num < get_proc_num:             # 스케줄링 시작

        unable_proc_num = 0
        visited_num = 0
        redy_proc_num = 0

        for _ in visited:
            if _ == 1:
                visited_num += 1
            elif _ == 0 and proc_list[visited.index(_)][1] <= schedule_count:
                redy_proc_num += 1

        for i in proc_list:
            if schedule_count >= i[1] and i[2] != 0:  # 대기 중인 프로세스들의 응답률 계산(BT가 0인 경우 제외)
               i[6] = (i[2] + i[3])/i[2]              # 프로세스 리스트 마지막에 응답률 저장

        if visited_num < processor_num:

            for j in proc_schedule:
                if not j or j[-1] == 0:
                    for k in proc_list:
                        if schedule_count >= k[1] and k[2] != 0 and visited[proc_list.index(k)] == 0:
                            j.append(k[0])
                            k[2] -= 1
                            visited[proc_list.index(k)] = 1
                            break
                    if not j or j[-1] == 0:
                        j.append(0)


                else:
                    if proc_list[j[-1]-1][6] > 0:
                        j.append(j[-1])
                        proc_list[j[-1]-1][2] -= 1

                    else:
                        max_rr = 0
                        max_rr_proc = 0

                        for i in proc_list:
                            if visited[i[0]-1] == 0 and schedule_count >= i[1] and max_rr < i[6]:
                                    max_rr = i[6]
                                    max_rr_proc = i[0]

                        if max_rr_proc > 0:
                            visited[j[-1]-1] = 0
                            j.append(max_rr_proc)
                            proc_list[max_rr_proc - 1][2] -= 1
                            visited[max_rr_proc - 1] = 1

                        else:
                            j.append(0)

        else:
            if redy_proc_num > 0:

                while True:
                    min_rr = math.inf
                    min_rr_proc_schedule = None
                    max_rr = 0
                    max_rr_proc = 0

                    for i in proc_list:
                        if visited[i[0]-1] == 0 and schedule_count >= i[1] and max_rr < i[6]:
                                max_rr = i[6]
                                max_rr_proc = i[0]

                    for j in proc_schedule:
                        if len(j) <= schedule_count and min_rr > proc_list[j[-1]-1][6] and proc_list[j[-1]-1][2] == 0:
                            min_rr = proc_list[j[-1]-1][6]
                            min_rr_proc_schedule = proc_schedule.index(j)

                    if min_rr != math.inf:
                        visited[proc_schedule[min_rr_proc_schedule][-1]-1] = 2
                        proc_schedule[min_rr_proc_schedule].append(max_rr_proc)
                        proc_list[max_rr_proc-1][2] -= 1
                        visited[max_rr_proc-1] = 1

                    elif min_rr == math.inf:
                        for j in proc_schedule:
                            if len(j) <= schedule_count and min_rr > proc_list[j[-1]-1][6] and proc_list[j[-1]-1][2] > 0:
                                min_rr = proc_list[j[-1]-1][6]
                                min_rr_proc_schedule = proc_schedule.index(j)

                        if min_rr != math.inf and min_rr < max_rr:
                            visited[proc_schedule[min_rr_proc_schedule][-1]-1] = 0
                            proc_schedule[min_rr_proc_schedule].append(max_rr_proc)
                            proc_list[max_rr_proc-1][2] -= 1
                            visited[max_rr_proc-1] = 1

                        elif min_rr != math.inf and min_rr >= max_rr:
                            proc_schedule[min_rr_proc_schedule].append(proc_schedule[min_rr_proc_schedule][-1])
                            proc_list[proc_schedule[min_rr_proc_schedule][-1]-1][2] -= 1

                        else:
                            break
            else:
                for j in proc_schedule:
                    if proc_list[j[-1]-1][2] > 0:
                        j.append(j[-1])
                        proc_list[j[-1]-1][2] -= 1
                    else:
                        visited[j[-1]-1] = 2
                        j.append(0)

        for k in proc_list:                                                     # 대기 프로세스 WT 증가(현재 추가 또는 RT = 0으로 종료된 프로세스 제외)
            if schedule_count >= k[1] and k[2] !=0 and visited[k[0]-1] == 0:    # 대기 중인 스케줄 + RT = 0이 아닌 프로세스
                k[3] += 1

        for l in proc_list:
            if l[2] == 0:                            # RT가 0이면 프로세스 제거
                l[4] = schedule_count - l[1] + 1              # TT 계산
                l[5] = l[4]/BT[l[0] - 1]                             # NTT 계산
                visited[l[0]-1] = 2
                l[6] = 0                                                 # 해당 프로세스 RT = 0(더 이상 선택되지 않기 위해)
                unable_proc_num += 1

        schedule_count += 1

# 반환값 리스트 정리
    WT = []
    TT = []
    NTT = []

    for _ in proc_list:
        WT.append(_[3])
    for i in range(len(WT)):
        TT.append(WT[i] + BT[i])
        NTT.append(TT[i]/BT[i])

    return proc_schedule, WT, TT, NTT


root = Tk()
root.title("Simulator")
root.geometry("800x800+50+50")

process_list = [[]]
name_list = []
at_list = []
bt_list = []
option_list = []


# 프로세스 리스트에 ([프로세스명], [at], [bt]) 값 전달 + 출력(콘솔창 출력으로 테스트하기 위해서)
def process_list_input(process_name_entry, at_entry, bt_entry):
    at = (at_entry.get())
    bt = (bt_entry.get())
    if at == "" and bt == "":
        return
    process_list.append(["", at, bt, "", "", ""])


# 입력 박스 비우기
def clear_input():
    enter_at.delete("0", "end")
    enter_bt.delete("0", "end")


# 입력 표 초기화
def remove_tree():
    for record in tree.get_children():
        tree.delete(record)


# 출력 표 초기화
def remove_tree2():
    for record2 in tree2.get_children():
        tree2.delete(record2)


# 프로세스 전체 비우기
def remove_list():
    process_list.clear()
    process_list.append([[]])
    name_list.clear()
    at_list.clear()
    bt_list.clear()


# 입력 표에 값 전달
def add_record():
    count = len(process_list) - 1
    tree.insert(parent='', index='end', iid=count, text="P"+str(count),
                values=(process_list[count][1], process_list[count][2]))
    at_list.append(process_list[count][1])
    bt_list.append(process_list[count][2])

def random_input():
    random_process_count = random.randint(5, 15)
    for i in range(random_process_count):
        random_at = random.randint(0, 10)
        random_bt = random.randint(2, 15)
        process_list.append(["", str(random_at), str(random_bt), "", "", ""])
        at_list.append(process_list[-1][1])
        bt_list.append(process_list[-1][2])
    for i in range(len(process_list) - 1):
        tree.insert(parent='', index='end', iid=i, text="P" + str(i + 1),values=(process_list[i + 1][1], process_list[i + 1][2], process_list[i + 1][3]))

def test_input():
    list1 = [3, 5, 8, 2, 4, 0, 9, 5, 10, 3, 5]
    list2 = [7, 15, 10, 5, 2, 10, 12, 10, 13, 14, 7]

    for i in range(11):
        process_list.append(["", str(list1[i]), str(list2[i]), "", "", ""])
        at_list.append(process_list[-1][1])
        bt_list.append(process_list[-1][2])

    for i in range(len(process_list) - 1):
        tree.insert(parent='', index='end', iid=i, text="P" + str(i + 1),values=(process_list[i + 1][1], process_list[i + 1][2], process_list[i + 1][3]))


# 여기서는 process_list에서 값을 갖고 오는데 반환받은 함수로 바꿀 예정
def return_record(process_list):
    for i in range(len(process_list) - 1):
        tree2.insert(parent='', index='end', iid=i, text="P"+str(i + 1),
                     values=(process_list[i + 1][1], process_list[i + 1][2], process_list[i + 1][3], process_list[i + 1][4], process_list[i + 1][5]))


def return_result(option_list, name_list, at_list, bt_list):
    print("return_result 시작")
    print(option_list)
    print(name_list)
    print(at_list)
    print(bt_list)
    print("return_result 끝")
    result1, result2, result3, result4 = choose(option_list[0], option_list[1], option_list[2], name_list, at_list, bt_list)

    len_0 = 0
    len_1 = 0
    len_2 = 0
    len_3 = 0

    if int(option_list[0])>=1:
        len_0 = len(result1[0])
    if int(option_list[0])>=2:
        len_0 = len(result1[1])
    if int(option_list[0])>=3:
        len_0 = len(result1[2])
    if int(option_list[0])>=4:
        len_0 = len(result1[3])
    time_range = [len_0, len_1, len_2, len_3]

    for i in range(1, len(time_table)):
        time_table[-1].destroy()
        time_table.pop()
        color_label1[-1].destroy()
        color_label1.pop()
        color_label2[-1].destroy()
        color_label2.pop()
        color_label3[-1].destroy()
        color_label3.pop()
        color_label4[-1].destroy()
        color_label4.pop()

    print("length:"+str(max(time_range)))
    for i in range(max(time_range)):
        time_table.append(Label(gantt_frame, borderwidth=1, text=i + 1, width=2, relief="raised"))
        time_table[i] = Label(gantt_frame, borderwidth=1, text=i + 1, width=2, relief="raised")
        time_table[i].grid(row=1, column=i+2, pady=0, ipady=0, ipadx=0)

        color_label1.append(Label(gantt_frame, text='', bg="white", width=2, height=3))
        color_label1[i] = Label(gantt_frame, text='', bg="white", width=2, height=3)
        color_label1[i].grid(row=2, column=i+2, pady=0, ipady=0, ipadx=0)

        color_label2.append(Label(gantt_frame, text='', bg="white", width=2, height=3))
        color_label2[i] = Label(gantt_frame, text='', bg="white", width=2, height=3)
        color_label2[i].grid(row=3, column=i+2, pady=0, ipady=0, ipadx=0)

        color_label3.append(Label(gantt_frame, text='', bg="white", width=2, height=3))
        color_label3[i] = Label(gantt_frame, text='', bg="white", width=2, height=3)
        color_label3[i].grid(row=4, column=i+2, pady=0, ipady=0, ipadx=0)

        color_label4.append(Label(gantt_frame, text='', bg="white", width=2, height=3))
        color_label4[i] = Label(gantt_frame, text='', bg="white", width=2, height=3)
        color_label4[i].grid(row=5, column=i+2, pady=0, ipady=0, ipadx=0)



    for i in range(max(time_range)):
        if int(option_list[0])>=1:
            if result1[0][i]==0:
                color_label1[i].config(bg=color1[result1[0][i]], text='')
            else:
                color_label1[i].config(bg=color1[result1[0][i]], text=result1[0][i])
        if int(option_list[0])>=2:
            if result1[1][i] == 0:
                color_label2[i].config(bg=color1[result1[1][i]], text='')
            else:
                color_label2[i].config(bg=color1[result1[1][i]], text=result1[1][i])
        if int(option_list[0])>=3:
            if result1[2][i] == 0:
                color_label3[i].config(bg=color1[result1[2][i]], text='')
            else:
                color_label3[i].config(bg=color1[result1[2][i]], text=result1[2][i])

        if int(option_list[0])>=4:
            if result1[3][i] == 0:
                color_label4[i].config(bg=color1[result1[3][i]], text='')
            else:
                color_label4[i].config(bg=color1[result1[3][i]], text=result1[3][i])

    for i in range(len(result4)):
        result4[i] = str(round(result4[i], 1))
    for i in range(len(result2)):
        result2[i] = str(result2[i])
    for i in range(len(result3)):
        result3[i] = str(result3[i])
    for i in range(len(process_list) - 1):
        process_list[i + 1][3] = result2[i]
        process_list[i + 1][4] = result3[i]
        process_list[i + 1][5] = result4[i]



# 프로세스 수, 알고리즘, 타임퀀텀 입력
def option_input(processor_entry_, tq_entry_, combo_entry_):
    option_list.clear()
    processor_entry = (processor_entry_.get())
    tq_entry = (tq_entry_.get())
    combo_entry = (combo_entry_.get())
    option_list.append(processor_entry)
    option_list.append(combo_entry)
    option_list.append(tq_entry)


# 옵션 박스 비우기
def clear_option():
    enter_processor.delete("0", "end")
    enter_tq.delete("0", "end")
    enter_processor.insert(0, "1")
    enter_tq.insert(0, "1")


def consol_print():
    print("옵션 리스트:")
    print(option_list)
    print("choose전달값:")
    print(option_list, name_list, at_list, bt_list, sep="\n")


# 입력 모음 -  프로세스 이름, at, bt----------------------------------------------------------------------------------------
input_frame = LabelFrame(root, text="process input", relief="solid", bd=1)
input_frame.grid(row=1, column=1)

process_name_entry = StringVar()
at_entry = StringVar()
bt_entry = StringVar()

# 각 입력

at_label = Label(input_frame, text='Arrival Time')
at_label.grid(row=0, column=2)
enter_at = ttk.Entry(input_frame, width=20, textvariable=at_entry)
enter_at.grid(row=1, column=2, columnspan=1, padx=5, pady=0, ipadx=0, ipady=0)

bt_label = Label(input_frame, text='Burst Time')
bt_label.grid(row=0, column=3)
enter_bt = ttk.Entry(input_frame, width=20, textvariable=bt_entry)
enter_bt.grid(row=1, column=3, columnspan=1, padx=5, pady=5, ipadx=0, ipady=0)

process_list_input = partial(process_list_input, process_name_entry, at_entry, bt_entry)

# 프로세서 개수, 알고리즘과 time quantum, 시작버튼 모음------------------------------------------------------------------------

option_input_frame = LabelFrame(root, text=" ", relief="solid", bd=0)
option_input_frame.grid(row=2, column=2)

processor_count_entry = StringVar()
tq_entry = StringVar()
combo_entry = StringVar()

process_count_label = Label(option_input_frame, text='Processor Count')
process_count_label.grid(row=0, column=1)
enter_processor = ttk.Entry(option_input_frame, width=10, textvariable=processor_count_entry)
enter_processor.grid(row=1, column=1, columnspan=1)
enter_processor.insert(0, "1")

# 알고리즘은 콤보박스로 결정
algorithm_label = Label(option_input_frame, text='Algorithm')
algorithm_label.grid(row=2, column=1)
# 콤보박스, 알고리즘 선택
enter_combox = ttk.Combobox(option_input_frame, width=8, textvariable=combo_entry)
enter_combox["value"] = ("FCFS", "RR", "RR_C", "SPN", "SRTN", "SRTN_C", "HRRN", "HEUG")
enter_combox.current(0)
enter_combox.grid(row=3, column=1)

tq_label = Label(option_input_frame, text='time quantum')
tq_label.grid(row=4, column=1)
enter_tq = ttk.Entry(option_input_frame, width=10, textvariable=tq_entry)
enter_tq.grid(row=5, column=1, columnspan=1)
enter_tq.insert(0, "1")

option_input = partial(option_input, processor_count_entry, tq_entry, combo_entry)
return_record = partial(return_record, process_list)
return_result = partial(return_result, option_list, name_list, at_list, bt_list)

# 버튼-----------------------------------------------------------------------------------------------------------------------------

input_button_frame = LabelFrame(root, text="", relief="solid", bd=0)
input_button_frame.grid(row=1, column=2)

# 버튼1 = add 버튼 누를 시 앞의 입력 값이 입력되고 칸을 비움
button1 = ttk.Button(input_button_frame, text="add",
                     command=lambda: [process_list_input(), add_record(), consol_print(), clear_input()])
button1.grid(row=1, column=1)

random_button = ttk.Button(input_button_frame, text="random input",
                     command=lambda: [random_input()])
random_button.grid(row=2, column=1)

test_button = ttk.Button(input_button_frame, text="test input",
                     command=lambda: [test_input()])
test_button.grid(row=3, column=1)




##버튼2 = start -- 선택된 알고리즘에 앞서 add를 통해 추가된 값 입력, time quantum  필요시 입력
button2 = ttk.Button(option_input_frame, text="start",
                     command=lambda: [option_input(), consol_print(), remove_tree2(), return_result(), return_record()])
# remove_all() - input value표 초기화
button2.grid(row=7, column=1, ipady=5)

# 버튼3 = reset --
button3 = ttk.Button(option_input_frame, text="reset",
                     command=lambda: [consol_print(), clear_input(), clear_option(), remove_tree(), remove_tree2(),
                                      remove_list()])
button3.grid(row=9, column=1)



# 입력값 출력--------------------------------------------------------------------------------------------------------------
input_table_frame = LabelFrame(root, text="Input value", relief="solid", bd=1)
input_table_frame.grid(row=2, column=1)

# 표 생성
tree = ttk.Treeview(input_table_frame, height=6)

tree["columns"] = ("one", "two")

tree.column("#0", width=133)
tree.heading("#0", text="Process name")

tree.column("one", width=133)
tree.column("two", width=133)

tree.heading("one", text="AT")
tree.heading("two", text="BT")

# 앞서 입력값을 treelist에 저장해서 전달 + 출력하면 될 듯
# 뒤의 0은 알고리즘의 결과를 받아 입력하고 그대로 결과 표 출력에 이용
empty_data = ["", "", ""]

for record in range(len(empty_data)):
    tree.insert(parent='', index='end', iid=record, text=record, values=(empty_data[1], empty_data[2]))
remove_tree()

tree.grid(row=2, column=1, padx=12, pady=5, ipadx=6, ipady=0)

# 간트차트----------------------------------------------------------------------------------------------------------------

color1 = ["white", "salmon", "royalblue", "orange", "dodgerblue", "gold", "lightblue", "yellowgreen", "lavenderblush",
          "teal", "burlywood", "slateblue", "yellow", "mediumpurple", "purple", "forestgreen"]
mycanvs=Canvas(root, width = 680)
gantt_frame = LabelFrame(mycanvs, text="gantt chart", relief="solid", bd=0)
scroll = ttk.Scrollbar(root, orient="horizontal", command=mycanvs.xview)
mycanvs.configure(xscrollcommand=scroll.set)


mycanvs.grid(row=3, column=1)
scroll.grid(row=4, column=1, stick='s')
mycanvs.create_window((4,4), window=gantt_frame, anchor="nw")



time_table = []
table_range = 34
for k in range(2, 34):
    time_table.append(Label(gantt_frame, borderwidth=1, text=k - 1, width=2, relief="raised"))
    time_table[k - 2] = Label(gantt_frame, borderwidth=1, text=k - 1, width=2, relief="raised")
    time_table[k - 2].grid(row=1, column=k, pady=0, ipady=0, ipadx=0)

# p1시각화

processor_num1 = Label(gantt_frame, borderwidth=1, text="p1", bg="gray", width=2, height=3, relief="raised")
processor_num1.grid(row=2, column=1, pady=0, ipady=0, ipadx=0)
color_label1 = []
for i in range(32):
    color_label1.append(Label(gantt_frame, text='', bg="white", width=2, height=3))
    color_label1[i] = Label(gantt_frame, text='', bg="white", width=2, height=3)
    color_label1[i].grid(row=2, column=i + 2, pady=0, ipady=0, ipadx=0)

# p2시각화 걍 모양만 넣은 것, p1수정해서 입력
processor_num2 = Label(gantt_frame, borderwidth=1, text="p2", bg="gray", width=2, height=3, relief="raised")
processor_num2.grid(row=3, column=1, pady=0, ipady=0, ipadx=0)
color_label2 = []
for i in range(32):
    color_label2.append(Label(gantt_frame, text='', bg="white", width=2, height=3))
    color_label2[i] = Label(gantt_frame, text='', bg="white", width=2, height=3)
    color_label2[i].grid(row=3, column=i + 2, pady=0, ipady=0, ipadx=0)

# p3 위와 같음
processor_num3 = Label(gantt_frame, borderwidth=1, text="p3", bg="gray", width=2, height=3, relief="raised")
processor_num3.grid(row=4, column=1, pady=0, ipady=0, ipadx=0)
color_label3 = []
for i in range(32):
    color_label3.append(Label(gantt_frame, text='', bg="white", width=2, height=3))
    color_label3[i] = Label(gantt_frame, text='', bg="white", width=2, height=3)
    color_label3[i].grid(row=4, column=i + 2, pady=0, ipady=0, ipadx=0)
# p4 위와 같음
processor_num4 = Label(gantt_frame, borderwidth=1, text="p4", bg="gray", width=2, height=3, relief="raised")
processor_num4.grid(row=5, column=1, pady=0, ipady=0, ipadx=0)
color_label4 = []
for i in range(32):
    color_label4.append(Label(gantt_frame, text='', bg="white", width=2, height=3))
    color_label4[i] = Label(gantt_frame, text='', bg="white", width=2, height=3)
    color_label4[i].grid(row=5, column=i + 2, pady=0, ipady=0, ipadx=0)


# 결과 표로 출력-----------------------------------------------------------------------------------------------------------

result_table_frame = LabelFrame(root, text="result", relief="solid", bd=0)
result_table_frame.grid(row=5, column=1)

tree2 = ttk.Treeview(result_table_frame, height=6)

# 순서대로 프로세스 이름, at, bt, wt, tt, ntt
tree2["columns"] = ("one", "two", "three", "four", "five")

tree2.column("#0", width=100)
tree2.heading("#0", text="Process name")
tree2.column("one", width=100)
tree2.column("two", width=100)
tree2.column("three", width=100)
tree2.column("four", width=100)
tree2.column("five", width=100)
tree2.heading("one", text="AT")
tree2.heading("two", text="BT")
tree2.heading("three", text="WT")
tree2.heading("four", text="TT")
tree2.heading("five", text="NTT")

empty_data2 = ["", "", "", "", "", ""]

for record2 in range(len(empty_data2)):
    tree2.insert(parent='', index='end', iid=record2, text=record2, values=(empty_data2[1], empty_data2[2], empty_data2[3], empty_data2[4], empty_data2[5]))

remove_tree2()

tree2.grid(row=2, column=1, padx=0, pady=5, ipadx=0, ipady=0)

root.mainloop()