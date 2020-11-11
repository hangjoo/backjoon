def ret_num_set():
    return {i:{"visit": False, "next": None} for i in range(10)}

def solution(phone_book):
    num_list = ret_num_set()
    for num_str in phone_book:
        cont = num_list
        for idx in range(len(num_str)):
            num = int(num_str[idx])
            if cont[num]["visit"] == False:
                cont[num]["visit"] = True
                if idx + 1 != len(num_str):
                    cont[num]["next"] = ret_num_set()
            else:
                if idx + 1 == len(num_str):
                    return False
                elif cont[num]["next"] is None:
                    return False
            if idx + 1 != len(num_str):
                cont = cont[num]["next"]
    answer = True
    return answer