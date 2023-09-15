class Solution:
    def countAndSay(self, n: int) -> str:
        example = ("1", "11", "21", "1211", "111221")
        if (n in (1, 2, 3, 4, 5)):
            return example[n-1]
        
        prev, res = "1", "111221"
        for _ in range(n-5):
            cnt, newRes = 0, ''
            for d in res:
                if d == prev:
                    cnt += 1
                else:
                    newRes += str(cnt) + prev
                    cnt = 1
                    prev = d
            res = newRes + str(cnt) + prev
            prev = res[0]

        return res