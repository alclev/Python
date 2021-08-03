#!/Python_Venv/env/bin/python



a = []
for i in range(20):
	a.append(i)

for i in range(20):
	print(a[i])

print("The length of the list is: {}".format(len(a)))	

for k in a:
	print("The element in the list is: {} ".format(k))

hills=[]
max = 15

run = True
while True:
	if len(hills) == 0:
		run = True
	if len(hills) == max:
		run = False
	if run:
		hills.append('#')
	if run == False:
		hills.remove('#')
	print(hills)
