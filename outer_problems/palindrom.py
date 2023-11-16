input_ = "?ab??a"

def solution(S:str):
    if (S[0] == "?" and S[-1] != "?") or (S[0] != "?" and S[-1] == "?") or (S[1] == S[-1]):
        print("palindrom accepted")
        palindrom_list = [*S]
        reversed_palindrom_list = palindrom_list[::-1]
        # print(palindrom_list, reversed_palindrom_list)
        reversed_count = len(palindrom_list)
        for i in range(len(palindrom_list)):
            reversed_count -= 1
            if palindrom_list[i] == "?" and reversed_palindrom_list[i] == "?":
                palindrom_list[i] = "a"
                palindrom_list[reversed_count] = "a"
            elif palindrom_list[i] == "?" and reversed_palindrom_list[i] != "?":
                palindrom_list[i] = reversed_palindrom_list[i]

        return "".join(element for element in palindrom_list)

if __name__ == "__main__":
    output = solution(input_)
    print(output)
