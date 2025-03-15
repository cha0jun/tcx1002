def longest_common_seq(text1, text2, cs):
    if not text1 or not text2:
        return cs
    if text1[0] == text2[0]:
        cs = cs + text1[0]
        return longest_common_seq(text1[1:],text2[1:],cs)
    if text1[0] != text2[0]:
        pop1 = longest_common_seq(text1[1:],text2,cs)
        pop2 = longest_common_seq(text1,text2[1:],cs)
        if len(pop1) > len(pop2):
            return pop1
        else:
            return pop2
        
print(longest_common_seq('abac','abca',''))