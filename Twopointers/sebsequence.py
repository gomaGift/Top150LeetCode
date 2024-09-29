def isSubsequence(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        t_ptr = 0
        s_ptr = 0

        while t_ptr < len(t):
                if s_ptr < len(s) and s[s_ptr] == t[t_ptr]:
                        s_ptr += 1
                t_ptr += 1
        return s_ptr == len(s)



print(isSubsequence("aaaaaaa", "baab"))