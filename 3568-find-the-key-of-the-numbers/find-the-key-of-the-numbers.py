class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        n1 = 4 - len(str(num1))
        num1 = "0" * n1 + str(num1)
        n2 = 4 - len(str(num2))
        num2 = "0" * n2 + str(num2)
        n3 = 4 - len(str(num3))
        num3 = "0" * n3 + str(num3)
        ans = ""
        check = False
        for i in range(4):
            key = min(int(num1[i]), int(num2[i]), int(num3[i]))
            if key != 0:
                check = True
            ans += str(key)

        if not check:
            return 0
        return int(ans)
