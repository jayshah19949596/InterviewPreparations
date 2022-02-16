class Solution(object):
    cache = {}
    def isMatch(self, s, p):
        stack = [[0, 0]]
        while stack:
            cur_s, cur_p = stack.pop()
            og_cur_s, og_cur_p = cur_s, cur_p
            if (og_cur_s, og_cur_p) in self.cache:
                continue
            if self.check_matching(cur_s, cur_p, s, p):
                return True
            while cur_s < len(s) and cur_p < len(p):
                if cur_p + 1 < len(p) and p[cur_p + 1] == "*":
                    if s[cur_s] == p[cur_p] or p[cur_p] == ".":
                         stack.append([cur_s + 1, cur_p + 2])
                    stack.append([cur_s, cur_p + 2])
                    break
                elif s[cur_s] == p[cur_p] or p[cur_p] == ".":
                    cur_s, cur_p = cur_s + 1, cur_p + 1
                    if cur_s == len(s) and cur_p == len(p): return True
                    if self.check_matching(cur_s, cur_p, s, p): return True
                elif s[cur_s] != p[cur_p]:
                    self.cache[(og_cur_s, og_cur_p)] = False
                    break
        return False

    def check_matching(self, cur_s, cur_p, s, p):
        if cur_s == len(s) and cur_p == len(p):
            return True
        if cur_s == len(s) and cur_p < len(p):
            while cur_p < len(p):
                if cur_p + 1 < len(p) and p[cur_p + 1] == "*":
                    cur_p = cur_p + 2
                else:
                    break
            else:
                if cur_p == len(p): return True