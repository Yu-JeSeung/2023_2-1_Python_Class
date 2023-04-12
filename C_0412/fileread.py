# 텍스트 파일 경로 설정
file_path = '/Users/jeseung/Documents/학교/2학년 1학기/파이썬프로그래밍/04:12/data/class_colon.txt'

# 딕셔너리 초기화
data_dict = {}

#파일 오픈
with open(file_path, "r") as f:
    # 파일의 각 라인에 대해 반복
    for line in f:
        # 라인에서 id와 데이터를 추출하여 딕셔너리 출력
        id, *data = line.strip().split(":")
        data_dict[id] = tuple(data)

# 딕셔너리 출략
print(data_dict)

for k in data_dict:
    print(k,data_dict[k])

# midx = 0으로 하여 최대 수강인원의 강좌정보도 출력
smax = 0; midx =0
for k in data_dict:
    if int(data_dict[k][1]>smax):
        smax=int(data_dict[k][1])
        midx=k
print("최대 수강하는 강좌의 정보 = ",midx,':',data_dict[midx])

# 리스트 수강인원을 append하여 max()함수 이용
snumList=[]
for k in data_dict:
    idata=int(data_dict[k][1])
    snumList.append(idata)

print('리스트 함수 이용: 최대 수강인원은 = ',max(snumList))