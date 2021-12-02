#def choose(pro_num, algo, quant, name, AT, BT):
#    if algo == 'FCFS':
#        gantt_answer = fcfs(pro_num,BT,AT)
#    elif algo == 'RR':
#        gantt_answer = rr_gantt(BT,AT)
#    elif algo == 'spn':
#        gantt_answer = spn_gantt(BT,AT)
#    elif algo == 'srtn':
#        gantt_answer = srtn_gantt(BT,AT)
#    elif algo == 'hrrn':
#        gantt_answer = hrrn_gantt(BT,AT)
#    elif algo == 'heug':
#        gantt_answer = heug_gantt(BT,AT)

#def choose_result(pro_num, algo, quant, name, AT, BT):
#    if algo == 'FCFS':
#        result_answer = fcfs_result(BT,AT)
#    elif algo == 'RR':
#        result_answer = rr_result(BT,AT)
#    elif algo == 'spn':
#        result_answer = spn_result(BT,AT)
#    elif algo == 'srtn':
#        result_answer = srtn_result(BT,AT)
#    elif algo == 'hrrn':
#        result_answer = hrrn_result(BT,AT)
#    elif algo == 'heug':
#        result_answer = heug_result(BT,AT)










### FCFS 완성


#from queue import Queue
#def fcfs(Processor_num, Burst, Arrival):
#    TT = [0 for _ in range(len(Burst))]
#    Burst_max = 0
#    min_Arrival = min(Arrival)
#    for i in Burst:
#        Burst_max += i
#    Processor = [[0 for _ in range(Burst_max+min_Arrival+Arrival[-1])] for _ in range(Processor_num)]
#    i = 0
#    q = Queue()
#    while True:
#        for j in range(len(Arrival)):
#            if Arrival[j] == i:
#                q.put(j)
#        for j in range(len(Processor)):
#            if Processor[j][i] == 0:
#                if not q.empty():
#                    num = q.get()
#                    for k in range(Burst[num]):
#                        Processor[j][i+k] = num+1
#                        TT[num] = i+k+1
#        count = 0
#        for j in Processor:
#            for k in j:
#                if k != 0:
#                    count += 1
#        i += 1
#        if count == Burst_max:
#            break
#    for l in range(len(TT)):
#        TT[l] -= Arrival[l]
#    WT = [0 for _ in range(len(Burst))]
#    NTT = [0.0 for _ in range(len(Burst))]
#    for l in range(len(TT)):
#        WT[l] = TT[l] - Burst[l]
#        NTT[l] = TT[l]/Burst[l]
#    return Processor, WT, TT, NTT

#Pro = int(input("프로세서의 개수를 입력하시오 : "))
#c = int(input("프로세스의 개수를 입력하시오 : "))
#Bt = [0 for _ in range(c)]
#AT = [0 for _ in range(c)] 
#TT = [0 for _ in range(c)] 
#WT = [0 for _ in range(c)] 
#NTT = [0 for _ in range(c)] 
#for i in range(c):
#    AT[i], Bt[i] = map(int,input("P{}의 Arrival Time과 Burst Time을 입력하시오 : ".format(i+1)).split())
#BT = list(Bt)
#lists,WT,TT,NTT = fcfs(Pro, Bt, AT)
#print(lists)
#print("WT = ",WT)
#print("TT = ", TT)
#print("NTT = ",NTT)























### RR 완성


#from queue import Queue
#def rr_result(Processor_num, Burst, Arrival,Quant):
#    TT = [0 for _ in range(len(Burst))]
#    Burst_copy = list(Burst)
#    Burst_max = 0
#    max_Q = 0
#    min_Arrival = min(Arrival)
#    for i in Burst:
#        Burst_max += i
#    Processor = [[0 for _ in range(Burst_max+min_Arrival+Arrival[-1])] for _ in range(Processor_num)]
#    i = 0
#    num = 0
#    q = Queue()
#    while True:
#        for j in range(len(Arrival)):
#            if Arrival[j] == i:
#                q.put(j)
#        for j in range(len(Processor)):
#            if Processor[j][i] == 0:
#                if i != 0 and Burst_copy[num] != 0:
#                    q.put(num)
#                if not q.empty():
#                    num = q.get()
#                    if Quant > Burst_copy[num]:
#                        max_Q = Burst_copy[num]
#                        Burst_copy[num] = 0
#                    else:
#                        max_Q = Quant
#                        Burst_copy[num] -= Quant
#                    for k in range(max_Q):
#                        Processor[j][i+k] = num+1
#                        TT[num] = i+k+1
#        count = 0
#        for j in Processor:
#            for k in j:
#                if k != 0:
#                    count += 1
#        i += 1
#        if count == Burst_max:
#            break
#    for l in range(len(TT)):
#        TT[l] -= Arrival[l]
#    WT = [0 for _ in range(len(Burst))]
#    NTT = [0.0 for _ in range(len(Burst))]
#    for l in range(len(TT)):
#        WT[l] = TT[l] - Burst[l]
#        NTT[l] = TT[l]/Burst[l]
#    return Processor, WT, TT, NTT

#Pro = int(input("프로세서의 개수를 입력하시오 : "))
#c = int(input("프로세스의 개수를 입력하시오 : "))
#Quant = int(input("Time Quantum을 입력하시오 : "))
#Bt = [0 for _ in range(c)]
#AT = [0 for _ in range(c)] 
#TT = [0 for _ in range(c)] 
#WT = [0 for _ in range(c)] 
#NTT = [0 for _ in range(c)] 
#for i in range(c):
#    AT[i], Bt[i] = map(int,input("P{}의 Arrival Time과 Burst Time을 입력하시오 : ".format(i+1)).split())
#BT = list(Bt)
#lists,WT,TT,NTT = rr_result(Pro, Bt, AT,Quant)
#print(lists)
#print("WT = ",WT)
#print("TT = ", TT)
#print("NTT = ",NTT)
























### SPN 완성

#def spn_result(Processor_num, Burst, Arrival):
#    TT = [0 for _ in range(len(Burst))]
#    Burst_max = 0
#    Burst_copy = list(Burst)
#    min_Arrival = min(Arrival)
#    for i in Burst:
#        Burst_max += i
#    Processor = [[0 for _ in range(Burst_max+min_Arrival+Arrival[-1])] for _ in range(Processor_num)]
#    i = 0
#    q = []
#    get_pop = 0
#    while True:
#        for j in range(len(Arrival)):
#            if Arrival[j] == i:
#                q.append(j)
#        for j in range(len(Processor)):
#            if Processor[j][i] == 0:
#                min1 = 10000
#                for b_len in range(len(q)):
#                    if min1 > Burst_copy[b_len]:
#                        min1 = Burst_copy[b_len]
#                        get_pop = b_len
#                if Burst_copy[get_pop] != 0:
#                    num = get_pop
#                    for k in range(Burst_copy[num]):
#                        if min1 != 10000:
#                            Processor[j][i+k] = num+1
#                            TT[num] = i+k+1
#                            Burst_copy[num] = 10000
                    
#        count = 0
#        for j in Processor:
#            for k in j:
#                if k != 0:
#                    count += 1
#        i += 1
#        if count == Burst_max:
#            break
#    for l in range(len(TT)):
#        TT[l] -= Arrival[l]
#    WT = [0 for _ in range(len(Burst))]
#    NTT = [0.0 for _ in range(len(Burst))]
#    for l in range(len(TT)):
#        WT[l] = TT[l] - Burst[l]
#        NTT[l] = TT[l]/Burst[l]
#    return Processor, WT, TT, NTT

#Pro = int(input("프로세서의 개수를 입력하시오 : "))
#c = int(input("프로세스의 개수를 입력하시오 : "))
#Bt = [0 for _ in range(c)]
#AT = [0 for _ in range(c)] 
#TT = [0 for _ in range(c)] 
#WT = [0 for _ in range(c)] 
#NTT = [0 for _ in range(c)] 
#for i in range(c):
#    AT[i], Bt[i] = map(int,input("P{}의 Arrival Time과 Burst Time을 입력하시오 : ".format(i+1)).split())
#BT = list(Bt)
#lists,WT,TT,NTT = spn_result(Pro, Bt, AT)
#print(lists)
#print("WT = ",WT)
#print("TT = ", TT)
#print("NTT = ",NTT)
























# srtn 완성


#def srtn_result(Processor_num, Burst, Arrival):
#    TT = [0 for _ in range(len(Burst))]
#    Burst_max = 0
#    Burst_copy = list(Burst)
#    min_Arrival = min(Arrival)
#    for i in Burst:
#        Burst_max += i
#    Processor = [[0 for _ in range(Burst_max+min_Arrival+Arrival[-1])] for _ in range(Processor_num)]
#    Doing = [-1 for _ in range(len(Processor))]
#    i = 0
#    q = []
#    get_pop = 0
#    change_zero = 0
#    while True:
#        #for j in range(len(Arrival)):
#        #    if Arrival[j] == i:
#        #        q.append(j)
#        #for j in range(len(Processor)):
#        #    for k in q:
#        #        Burst[k]
#        before = len(q)
#        for j in range(len(Arrival)):
#            if Arrival[j] == i:
#                q.append(j)
#        after = len(q)
#        #if before != after:
#        #    for j in range(len(Processor)):
#        #        if Processor[j][i] != 0:
#        #            min1 = 10000
#        #            for b_len in range(len(q)):
#        #                if min1
#        for j in range(len(Processor)):
#            #print(j,i)
#            if after != before:
#                if Processor[j][i] != 0:
#                    change_zero = Processor[j][i]
#                    k = 0
#                    while True:
#                        if Processor[j][i+k] == change_zero:
#                            Processor[j][i+k] = 0
#                        else:
#                            break
#                        k += 1
#                    Burst_copy[change_zero - 1] = k
#            #print("change_zero",Processor)
#            if Processor[j][i] == 0:
#                min1 = 10000
#                for b_len in q:
#                    if min1 > Burst_copy[b_len]:
#                        min1 = Burst_copy[b_len]
#                        get_pop = b_len
#                #print("get_pop",get_pop)
#                if Burst_copy[get_pop] != 0:
#                    num = get_pop
#                    for k in range(Burst_copy[num]):
#                        if min1 != 10000:
#                            Processor[j][i+k] = num+1
#                            TT[num] = i+k+1
#                            Burst_copy[num] = 10000
                    
#        count = 0
#        for j in Processor:
#            for k in j:
#                if k != 0:
#                    count += 1
#        i += 1
#        if count == Burst_max:
#            break
#        #print(Processor)
#        #print("count, Burst_max",count,Burst_max)
#    for l in range(len(TT)):
#        TT[l] -= Arrival[l]
#    WT = [0 for _ in range(len(Burst))]
#    NTT = [0.0 for _ in range(len(Burst))]
#    for l in range(len(TT)):
#        WT[l] = TT[l] - Burst[l]
#        NTT[l] = TT[l]/Burst[l]
#    return Processor, WT, TT, NTT

#Pro = int(input("프로세서의 개수를 입력하시오 : "))
#c = int(input("프로세스의 개수를 입력하시오 : "))
#Bt = [0 for _ in range(c)]
#AT = [0 for _ in range(c)] 
#TT = [0 for _ in range(c)] 
#WT = [0 for _ in range(c)] 
#NTT = [0 for _ in range(c)] 
#for i in range(c):
#    AT[i], Bt[i] = map(int,input("P{}의 Arrival Time과 Burst Time을 입력하시오 : ".format(i+1)).split())
#BT = list(Bt)
#lists,WT,TT,NTT = spn_result(Pro, Bt, AT)
#print(lists)
#print("WT = ",WT)
#print("TT = ", TT)
#print("NTT = ",NTT)























### hrrn 완성


# def hrrn_result(Processor_num, Burst, Arrival):
#    TT = [0 for _ in range(len(Burst))]
#    WT = []
#    Burst_max = 0
#    Burst_copy = list(Burst)
#    min_Arrival = min(Arrival)
#    for i in Burst:
#        Burst_max += i
#    Processor = [[0 for _ in range(Burst_max+min_Arrival+Arrival[-1])] for _ in range(Processor_num)]
#    i = 0
#    q = []
#    get_pop = 0
#    while True:
#        for j in range(len(Arrival)):
#            if Arrival[j] == i:
#                q.append(j)
#                WT.append(0)
#        for j in range(len(Processor)):
#            if Processor[j][i] == 0:
#                max1 = -1
#                for b_len in range(len(q)):
#                    if max1 < (Burst_copy[b_len]+WT[b_len])/Burst_copy[b_len]:
#                        max1 = (Burst_copy[b_len]+WT[b_len])/Burst_copy[b_len]
#                        get_pop = b_len
#                if Burst_copy[get_pop] != 0:
#                    num = get_pop
#                    for k in range(Burst_copy[num]):
#                        if max1 != -1:
#                            Processor[j][i+k] = num+1
#                            TT[num] = i+k+1
#                            Burst_copy[num] = -1
                    
#        count = 0
#        for j in Processor:
#            for k in j:
#                if k != 0:
#                    count += 1
#        i += 1
#        for j in range(len(WT)):
#            WT[j] += 1
#        if count == Burst_max:
#            break
#    for l in range(len(TT)):
#        TT[l] -= Arrival[l]
#    WT = [0 for _ in range(len(Burst))]
#    NTT = [0.0 for _ in range(len(Burst))]
#    for l in range(len(TT)):
#        WT[l] = TT[l] - Burst[l]
#        NTT[l] = TT[l]/Burst[l]
#    return Processor, WT, TT, NTT

# Pro = int(input("프로세서의 개수를 입력하시오 : "))
# c = int(input("프로세스의 개수를 입력하시오 : "))
# Bt = [0 for _ in range(c)]
# AT = [0 for _ in range(c)] 
# TT = [0 for _ in range(c)] 
# WT = [0 for _ in range(c)] 
# NTT = [0 for _ in range(c)] 
# for i in range(c):
#    AT[i], Bt[i] = map(int,input("P{}의 Arrival Time과 Burst Time을 입력하시오 : ".format(i+1)).split())
# BT = list(Bt)
# lists,WT,TT,NTT = hrrn_result(Pro, Bt, AT)
# print(lists)
# print("WT = ",WT)
# print("TT = ", TT)
# print("NTT = ",NTT)

























# def hyeokgi(processer_num, BT, AT):
#     print('hyeokgi 시작')
#     get_proc_num = len(AT)
#     proc_list = [[0 for _ in range(7)] for _ in range(get_proc_num)]        # 데이터 저장을 위한 프로세스 리스트(TT와 NTT는 따로 저장)
#     visited = [0 for _ in range(get_proc_num)]                              # 프로세서에서 작정중인지 확인
#     proc_schedule = [[] for _ in range(processer_num)]                      # 스케줄링 리스트
#     unable_proc_num = 0                                                     # BT가 0인 프로세스 개수
#     schedule_count = 0                                                      # 스케줄링 진행 시간

#     for i in range(get_proc_num):                     # 프로세스 입력
#         proc_list[i][0] = i + 1                       # 각 프로세스 index(0)에 번호 부여
#         proc_list[i][1], proc_list[i][2] = AT[i], BT[i]

#     while unable_proc_num < get_proc_num:             # 스케줄링 시작

#         for i in proc_list:
#             if schedule_count >= i[1] and i[2] != 0:  # 대기 중인 프로세스들의 응답률 계산(BT가 0인 경우 제외)
#                i[6] = (i[2] + i[3])/i[2]              # 프로세스 리스트 마지막에 응답률 저장
        
#         for j in proc_schedule:
#             if not j or j[-1] == 0:
#                 for k in proc_list:
#                     if schedule_count >= k[1] and k[6] != 0 and visited[proc_list.index(k)] == 0:
#                         j.append(k[0])
#                         k[2] -= 1
#                         visited[proc_list.index(k)] = 1
#                         break
#                 if not j or j[-1] == 0:
#                     j.append(0)
#             else:
#                 max_rr_proc = j[-1]             # 응답률 높은 프로세스로 변경을 위한 초기화

#                 for k in proc_list:
#                     if visited[k[0]-1] == 0 and proc_list[max_rr_proc-1][6] < k[6]:   # 대기중인 프로세스와 비교
#                         max_rr_proc = k[0]

#                 if proc_list[max_rr_proc-1][6] == 0:
#                     max_rr_proc = 0
#                     j.append(max_rr_proc)

#                 else:
#                     visited[j[-1]-1] = 0
#                     j.append(max_rr_proc)
#                     proc_list[max_rr_proc-1][2] -= 1
#                     visited[max_rr_proc - 1] = 1

#         for k in proc_list:                                                     # 대기 프로세스 WT 증가(현재 추가 또는 RT = 0으로 종료된 프로세스 제외)
#             if schedule_count >= k[1] and k[2] !=0 and visited[k[0]-1] == 0:    # 대기 중인 스케줄 + RT = 0이 아닌 프로세스
#                 k[3] += 1


#         for l in range (len(visited)):
#             if visited[l] == 1 and proc_list[l][2] == 0 and proc_list[l][6] != 0:   # RT가 0이면 프로세스 제거
#                 proc_list[l][4] = schedule_count - proc_list[l][1] + 1              # TT 계산
#                 proc_list[l][5] = proc_list[l][4]/BT[l]                             # NTT 계산
#                 proc_list[l][6] = 0                                                 # 해당 프로세스 RT = 0(더 이상 선택되지 않기 위해)
#                 unable_proc_num += 1

#         schedule_count += 1

# # 반환값 리스트 정리
#     WT = []
#     TT = []
#     NTT = []

#     for _ in proc_list:
#         WT.append(_[3])
#         TT.append(_[4])
#         NTT.append(_[5])

#     return proc_schedule, WT, TT, NTT



# Pro = int(input("프로세서의 개수를 입력하시오 : "))
# c = int(input("프로세스의 개수를 입력하시오 : "))
# Bt = [0 for _ in range(c)]
# AT = [0 for _ in range(c)] 
# TT = [0 for _ in range(c)] 
# WT = [0 for _ in range(c)] 
# NTT = [0 for _ in range(c)] 
# for i in range(c):
#    AT[i], Bt[i] = map(int,input("P{}의 Arrival Time과 Burst Time을 입력하시오 : ".format(i+1)).split())
# BT = list(Bt)
# lists,WT,TT,NTT = hyeokgi(Pro, Bt, AT)
# print(lists)
# print("WT = ",WT)
# print("TT = ", TT)
# print("NTT = ",NTT)