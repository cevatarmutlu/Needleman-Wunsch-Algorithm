def calculate(dna1: str, dna2: str, gap: float, match: float, mismatch: float):
    row_len = len(dna2) + 1
    col_len = len(dna1) + 1
    need_arr = create_list(row_len, col_len, gap)

    for row in range(1, row_len):
        for col in range(1, col_len):
            left_val = need_arr[row][col - 1] + gap
            down_val = need_arr[row - 1][col] + gap
            if dna2[row - 1] == dna1[col - 1]:
                match_value = match
            else:
                match_value = mismatch
            corner_val = need_arr[row - 1][col - 1] + match_value

            max_val = max([left_val, down_val, corner_val])
            need_arr[row].append(max_val)

    return need_arr[row_len - 1][col_len - 1]


def create_list(row_len: int, col_len: int, gap: float):
    arr = []
    temp_row = [x * gap for x in range(col_len)]
    arr.append(temp_row)
    for i in range(1, row_len):
        arr.append([arr[i - 1][0] + gap])
    return arr




