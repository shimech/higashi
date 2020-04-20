def letter_n_gram_list(s, n):
    ans = []

    if len(s) < n:
        return ans

    for i in range(len(s) - (n-1)):
        ans.append(s[i:i+n])
    return ans
