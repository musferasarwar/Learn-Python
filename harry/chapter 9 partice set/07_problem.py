with open("c:/Learn-Python-main/harry/chapter 9 partice set/log.txt", "r") as f:
    lines = f.readlines()
lineon=1
for line in lines:
    if ("python" in line):
         print(f"yes python is present.line no:{lineon}")
         break
    lineon += 1


else:
    print("no python is not present")
