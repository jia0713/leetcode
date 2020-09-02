#这方法是谁想出来的，服了

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        for p in people:
            p[1] = -p[1]
        people = sorted(people, key=(lambda x: [x[0], x[1]]), reverse=True)
        for p in people:
            p[1] = -p[1]
        res = []
        for p in people:
            res.insert(p[1], p)
        return res