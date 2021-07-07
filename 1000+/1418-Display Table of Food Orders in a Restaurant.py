from collections import Counter


class Solution(object):
    def displayTable(self, orders):
        """
        :type orders: List[List[str]]
        :rtype: List[List[str]]
        """
        order_counter, table_counter, res = {}, set(), []
        for order in orders:
            _, table, food = order[0], order[1], order[2]
            table_counter.add(int(table))
            if food not in order_counter:
                order_counter[food] = Counter([table])
            else:
                order_counter[food][table] += 1
        foods = list(order_counter.keys())
        tables = list(table_counter)
        foods.sort()
        tables.sort()
        res.append(["Table"] + foods)
        for table in tables:
            table, temp_res = str(table), [str(table)]
            for food in foods:
                temp_res = temp_res + [str(order_counter[food][table])]
            res.append(temp_res)
        return res
