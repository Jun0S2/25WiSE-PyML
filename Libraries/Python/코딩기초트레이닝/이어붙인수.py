# def solution(num_list):
#     even_str = ''
#     odd_str = ''
#     for i in num_list:
#         if (i % 2 ==0):
#             even_str += str(i)
#         else :
#             odd_str+=str(i)
#     return int(even_str) + int(odd_str)

#  python 스러운 버전.. "".join( ) 사용
def solution(num_list):
    convert_tostring = [str(i) for i in num_list]
    # print(convert_tostring)
    
    odd = "".join(x for x in convert_tostring if int(x)%2!=0)
    even = "".join(x for x in convert_tostring if int(x)%2==0)
    return int(odd)+int(even)