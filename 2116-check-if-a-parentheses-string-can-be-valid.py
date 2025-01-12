class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2:
            return False
        st_locked, st_unlocked = [], []
        for i,p in enumerate(s):
            if locked[i] == '0':
                st_unlocked.append(i)
            elif p == '(':
                st_locked.append(i)
            else:
                if st_locked:
                    st_locked.pop()
                elif st_unlocked:
                    st_unlocked.pop()
                else:
                    return False
        while st_locked and st_unlocked and st_locked[-1] < st_unlocked[-1]:
            st_locked.pop()
            st_unlocked.pop()

        if st_locked: return False
        return not (len(st_unlocked) % 2)
