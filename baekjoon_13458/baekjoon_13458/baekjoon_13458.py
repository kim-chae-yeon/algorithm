test_cnt = int(input())
student = list(map(int, input().split()))
main_, sub_ = map(int, input().split())

answer = 0
for stu in student:
    # 총감독관
    answer += 1

    # 총감독관 배치 후 남은 사람이 있을 경우
    if stu - main_ > 0:
        if (stu - main_) % sub_ == 0:
            answer += (stu - main_) // sub_
        else:
            answer += (stu - main_) // sub_ + 1

print(answer)