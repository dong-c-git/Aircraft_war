#coding:utf-8
# class Solution:
#     def game(self, guess, answer):
#         #判断数组a索引位数字和索引位b数据是否相等
#         num = 0
#         if not guess or not answer:
#             return 0
#         for i in range(3):
#             if guess[i] == answer[i]:
#                 num+=1
#         return num
#
# guess = [2,2,3]
# answer = [3,2,1]
# test = Solution()
# ret = test.game(guess,answer)
# print(ret)
class Solution:
    def robot(self, command, obstacles, x, y):
        #x和y坐标值分开计算:
        if x>y:
            command = command *x
            if len(command)>1000:
                command = command[:1000]
        else:
            command*y
            if len(command)>1000:
                command = command[:1000]
        x1 = 0
        y1 = 0
        for i in command:
            if i == "U":
                y1 += 1
            elif i == "R":
                x1 +=1
            if obstacles == []:
                if x1 == x and y1 == y:
                    return True
                continue
            elif x1 == obstacles[0][0] and y1 == obstacles[0][1]:
                return False
            elif x1 != obstacles[0][0] or y1 != obstacles[0][1]:
                if x1 == x and y1 == y:
                    return True
        return False
command = "URR"
obstacles = []
x = 3
y = 2
test = Solution()
ret = test.robot(command,obstacles,x,y)
print(ret)

