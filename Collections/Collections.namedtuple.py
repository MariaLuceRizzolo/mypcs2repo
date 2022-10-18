from collections import namedtuple
N, field_name = int(input()), input().split()

student = namedtuple('student',field_name)
sum_ = 0

for i in range(N):
    stud = input().split()
    tmp = student(*stud)
    sum_ += int(tmp.MARKS)

print('%.2f'%(sum_/N))