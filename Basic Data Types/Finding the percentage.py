if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(0,n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

sum_= sum(student_marks[query_name])
marksaverage = sum_ /len(student_marks[query_name])
print('%.2f'%marksaverage)