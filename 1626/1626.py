from typing import *


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        res = 0
        totalNum = len(scores)
        bestScoreOnPlayer = [0] * totalNum
        score_age = sorted(list(zip(scores, ages)))
        for i in range(totalNum):
            for prev in range(i):
                if (score_age[prev][1] <= score_age[i][1]):
                    bestScoreOnPlayer[i] = max(bestScoreOnPlayer[i], bestScoreOnPlayer[prev])
            bestScoreOnPlayer[i] += score_age[i][0]
            res = max(res, bestScoreOnPlayer[i])
            
        return res


a = Solution()
print(a.bestTeamScore([1,1,1,1,1,1,1,1,1,1], [811,364,124,873,790,656,581,446,885,134]))
