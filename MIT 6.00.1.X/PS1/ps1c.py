def longestSubstringAlphabetical(s):
    # O(n) time | O(n) space, 24 min
    s = s.lower()
    longestSubstrArr = []
    currentSubstrArr = []
    i = 0

    while i < len(s):

        if len(currentSubstrArr) == 0:
            currentSubstrArr.append(s[i])
        else:
            if ord(s[i]) >= ord(currentSubstrArr[-1]):
                currentSubstrArr.append(s[i])
            else:
                if len(currentSubstrArr) > len(longestSubstrArr):
                    longestSubstrArr = currentSubstrArr
                currentSubstrArr = []
                i -= 1

        i += 1

    if len(currentSubstrArr) > len(longestSubstrArr):
        longestSubstrArr = currentSubstrArr

    return ''.join(longestSubstrArr)


s = 'igawtotfumwjsorefwx'
print('Longest substring in alphabetical order is: ',
      longestSubstringAlphabetical(s))
