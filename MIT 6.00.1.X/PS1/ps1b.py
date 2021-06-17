def count_bob(s):
    if len(s) < 3:
        return 0

    bob_count = 0

    for i in range(len(s) - 2):
        if s[i: i + 3] == 'bob':
            bob_count += 1

    return bob_count


s = 'azcbobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobegghaklboboboboboboboboboboboboboboboboboboboboboooob'
print('Number of times bob occurs is: ', count_bob(s))
