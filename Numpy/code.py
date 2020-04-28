# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
#Code starts here
data=np.genfromtxt(path,delimiter=',',skip_header=1)
census=np.concatenate((data,new_record),axis=0)



# --------------
#Code starts here
age=np.array(census[0:,0])
max_age=age.max()
min_age=age.min()
age_mean=age.mean()
age_std = np.std(age)




# --------------
#Code starts here
race_0=np.array([i for i in census if i[2]==0])
race_1=np.array([i for i in census if i[2]==1])
race_2=np.array([i for i in census if i[2]==2])
race_3=np.array([i for i in census if i[2]==3])
race_4=np.array([i for i in census if i[2]==4])
len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)
check=[len_0,len_1,len_2,len_3,len_4]
a=min(check)
minority=[i for i in check if i==a]
minority_race=check.index(minority[0])


# --------------
#Code starts here
senior_citizens = np.array([i for i in census if i[0]>60])
working_hours_sum= sum(list(senior_citizens[:,6]))
senior_citizens_len= len(senior_citizens)
avg_working_hours= working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
high= np.array([i for i in census if i[1]>10])
low= np.array([i for i in census if i[1]<=10])
avg_pay_high = high[:,7].mean()
avg_pay_low= low[:,7].mean()
bool = avg_pay_high>avg_pay_low
print(bool)


