
import collections
import numpy as np




path = "/home//foo/"


stack = ['home', 'foo','ddddd']
stack.pop()

final_str = "/" + "/".join(stack)
final_str

st =[]
st.append([0,0])

token = "+"
if token is "+":
    print("yes")
    
    


graph = {}
graph["a"] = {}

graph["a"]["b"] = 2



prerequisites = [[1,0],[1,2],[0,2]]
numCourses = 3
indegree = [0] * numCourses
adj1 = [[] for _ in range(numCourses)]

adj2 = [0] * numCourses


for prerequisite in prerequisites:
    adj[prerequisite[1]].append(prerequisite[0])
    indegree[prerequisite[0]] += 1







for neighbor, weight in graph["a"].items():
    print(neighbor, weight)


queries = [["a","c"],["b","a"],["a","e"]]

for i, (q,p) in enumerate(queries):
    print(i, q,p)


for i in range(5):


-4 % 5





p  = [0, 1, 2, 3, 4]

len(p)


def move(p, U):
    q = []
    for i in range(len(p)):
        print((i-U) % len(p))
        q.append(p[(i-U) % len(p)])
        
    return q


print(move(p, 1))







nums = [100,4,200,1,3,2,2]

intervals = [[1,3],[8,10],[15,18],[2,6]]

K = intervals.sort()
K

str1 = collections.Counter(nums) 
str2 = collections.defaultdict(nums)
print(str1)
print(str2)


nums = [0,3,7,2,5,8,4,6,0,1]

m = set(nums)
m











strs = ["eat","apple"]
key1 = sorted(strs)
key2 = sorted(strs[0])
print(key1)
    

strs = set("eat","apple")
strs[0]   

    
    
for s in strs:
    print(s)
    key = sorted(s)
    print(key)
            
            
key = ''.join(s)
my_dict = {"age", 25}  # TypeError: unhashable type: 'list'
my_dict


25 in my_dict




my_dict.items()


s = "dog cat cat dog"
words = s.split(' ')