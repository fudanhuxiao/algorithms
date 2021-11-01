class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        def helper(pattern, s, maps):
            if len(pattern) == 0 and len(s) > 0:
                return False
            if len(pattern) == 0 and len(s) == 0:
                return True
            #len(s) - k >= len(pattern)-1
            # k <= len(s)-len(pattern)+1
            for end in range(1, len(s)-len(pattern)+2):
                if pattern[0] not in maps and s[:end] not in maps.values():
                    maps[pattern[0]] = s[:end]
                    if helper(pattern[1:], s[end:], maps):
                        return True
                    del maps[pattern[0]]
                elif pattern[0] in maps and maps[pattern[0]] == s[:end]:
                    if helper(pattern[1:], s[end:], maps):
                        return True
            return False
        return helper(pattern, s, {})
                
