# .append()
# last element : num_list[-1]
# def solution(num_list):
#     answer = num_list
#     # last_element = num_list[-1];
#     # print(last_element)
#     if num_list[-1] > num_list[-2] :
#         answer.append(num_list[-1]-num_list[-2])
#     else :
#         answer.append(num_list[-1]*2)
#     return answer

def solution(num_list):
    last, prev = num_list[-1], num_list[-2]
    append_val = last - prev if last > prev else last * 2
    return num_list + [append_val]
