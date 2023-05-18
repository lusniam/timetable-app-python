weeks=[]
file=open('tygodnie.txt','r')
for line in file:
    weeks.append(line.strip())
file.close()

file=open("dni.txt","w")
for line in weeks:
    if line=='29.05-02.06':
        file.write('29.05;30.05;31.05;01.06;02.06;\n')
    elif line=='27.02-03.03':
        file.write('27.02;28.02;01.03;02.03;03.03;\n')
    else:
        x=line.split('-')
        y=x[0].split('.')
        days=[]
        for i in range(5):
            days.append(f'{(int(y[0])+i):02d}'+'.'+y[1]+';')
        file.write(''.join(days)+'\n')
file.close()