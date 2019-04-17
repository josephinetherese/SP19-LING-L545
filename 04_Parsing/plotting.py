import sys
import matplotlib.pyplot as plt

labels = {0:'fin', 1:'por', 2:'swe', 3:'hin', 4:'hrv', 5:'en', 6:'ger', 7:'hi-en', 8:'pol', 9:'rus', 10:'tur'}
y = [0.72, 0.67, 0.7, 0.47, 0.67, 0.72, 0.64, 0.68, 0.83, 0.64, 0.59]  # proportion of VO
x = [0.28, 0.33, 0.3, 0.53, 0.34, 0.28, 0.36, 0.32, 0.17, 0.36, 0.41]  # proportion of OV
plt.plot(x, y, 'ro')
plt.title('Relative word order of verb and object')
plt.xlim([0,1]) # Set the x and y axis ranges
plt.ylim([0,1])
plt.xlabel('OV') # Set the x and y axis labels
plt.ylabel('VO')
for i in labels:  # Add labels to each of the points
    plt.text(x[i]-0.01, y[i]-0.01, labels[i], fontsize=9)
plt.savefig('/Users/josephinedouglas/SPRING_2019/SP19-LING-L545/04_Parsing/wordorder.png')
plt.show()
