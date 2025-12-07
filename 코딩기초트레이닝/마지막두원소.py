# .append()
# last element : num_list[-1]
def solution(num_list):
    answer = num_list
    # last_element = num_list[-1];
    # print(last_element)
    if num_list[-1] > num_list[-2] :
        answer.append(num_list[-1]-num_list[-2])
    else :
        answer.append(num_list[-1]*2)
    return answer