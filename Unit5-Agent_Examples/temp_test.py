def largest_common_substring(str1, str2):
    m = len(str1)
    n = len(str2)
    result = ''
    length = 0
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > length:
                    length = dp[i][j]
                    result = str1[i - length:i]
            else:
                dp[i][j] = 0

    return result
result = largest_common_substring('abcdef', 'zabcf')
print(result)