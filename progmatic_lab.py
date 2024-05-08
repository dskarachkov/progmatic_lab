def solution(s, target):
    res = []

    def dfs(i, path, cur_res, prev_num):
        if i == len(s):
            if cur_res == target:
                res.append(path)
            return

        num = int(s[i])
        if i == 0:
            dfs(i + 1, path + str(num), cur_res + num, num)
        else:
            dfs(i + 1, path + "+" + str(num), cur_res + num, num)
            dfs(i + 1, path + "-" + str(num), cur_res - num, -num)
            dfs(i + 1, path + str(num), (cur_res - prev_num) + prev_num * 10 + num * prev_num / abs(prev_num),
                prev_num * 10 + num * prev_num / abs(prev_num))

    dfs(0, "", 0, 0)
    return res

print(solution('9876543210', 200))
