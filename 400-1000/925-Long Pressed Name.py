class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        name = "*" + name + "*"
        typed = "*" + typed + "*"
        name_helper, typed_helper = [], []
        for index in range(1, len(name)):
            if name[index] != name[index - 1]:
                name_helper.append(index)
        for index in range(1, len(typed)):
            if typed[index] != typed[index - 1]:
                typed_helper.append(index)
        if len(name_helper) != len(typed_helper):
            return False
        for index in range(len(name_helper)):
            if name[name_helper[index]] != typed[typed_helper[index]]:
                return False
            if index >= 1:
                if (
                    name_helper[index] - name_helper[index - 1]
                    > typed_helper[index] - typed_helper[index - 1]
                ):
                    return False
        return True
