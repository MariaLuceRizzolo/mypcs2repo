def count_substring(string, sub_string):
    len1 = len(string)
    len2 = len(sub_string)
    counter = 0
    for i in range (len1-len2+1):
        if(string[i:(i+len2)] == sub_string):
            counter += 1
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)