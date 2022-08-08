me= {'name':'Uthman muhammad ', 'address':'Unguwan sarki', 
        'number':'09013042149', 'age':13, 'dob':2009, 'pob':'Abuja',
            'work experience':'1 month', 'schools attented':'ilc schools'}

print('1. Name: {}\n2. Address: {}\n3. Phone Number: {}\n4. Age: {}\n5. Date of Birth: {}\n6. Place of Birth: {}\n7. Work Experience: {}\n8. Schools Attended: {}'.format(me['name'],me['address'],me['number'],me['age'],me['dob'],me['pob'],me['work experience'],me['schools attented']))

fruits=[{'name':'Apple', 'taste':6.5, 'colour':'red'}, #taste score /10
        {'name':'Pear', 'taste':8, 'colour':'green'},
        {'name':'Grapes', 'taste':7.5, 'colour':'purple'},
        {'name':'Orange', 'taste':7.5, 'colour':'orange'},
        {'name':'Tomato', 'taste':5, 'colour':'red'},]

#print(fruits)

fruits[0]['price']= 'N10'
fruits[1]['price']= 'N15'
fruits[2]['price']= 'N20'
fruits[3]['price']= 'N25'
fruits[4]['price']= 'N30'

print('{}: this is a {} and {} in colour'.format(fruits[0]['name'], fruits[0]['taste'], fruits[0]['colour'], fruits[0]['price']))
print('{}: this is an {} and {} in colour'.format(fruits[1]['name'], fruits[1]['taste'], fruits[1]['colour'], fruits[1]['price']))
print('{}: this is a {} and {} in colour'.format(fruits[2]['name'], fruits[2]['taste'], fruits[2]['colour'], fruits[2]['price']))
print('{}: this is a {} and {} in colour'.format(fruits[3]['name'], fruits[3]['taste'], fruits[3]['colour'], fruits[3]['price']))
print('{}: this is a {} and {} in colour'.format(fruits[4]['name'], fruits[4]['taste'], fruits[4]['colour'], fruits[4]['price']))


students = ['maska', 'bukar', 'khalil']

age = ['5' ,'6', '7']

hobbies = ['footbal, basketball, voleyball', 'cricket, research, coding','travelling, driving, count']

print('my name is {}, i am {} years old and i enjoy {}'.format(students[0], age[0], hobbies[0]))
print('my name is {}, i am {} years old and i enjoy {}'.format(students[1], age[1], hobbies[1]))
print('my name is {}, i am {} years old and i enjoy {}'.format(students[2], age[2], hobbies[2]))


fruits = 'Apple,Mango,Guava,Orange,Pear'
 
#fruit1= fruits[:5]
#fruit1= fruits.split(',')[0]
#fruit1= fruits[::-1][-5:][::-1]
fruit1= fruits[::-1][-24:][:6][::-1] #to print 'orange'
print(fruit1)

# print(fruits[:5])
# print(fruits[6:11])
# print(fruits[12:17])
# print(fruits[18:24])
# print(fruits[25:])   

# print(fruits.split(',')[0])   
# print(fruits.split(',')[1])   
# print(fruits.split(',')[2])   
# print(fruits.split(',')[3])   
# print(fruits.split(',')[4])   
  

# print(fruits[0:5]+fruits[25:])


name= input('What is your first name?')
dob= 2022-int(input('What year were you born?'))

print('{}, you are {} years old'.format(name,dob))



personalinfo = {
        'name':'Uthman',
        'state': 'borno',
        'number':'09013042149',
        'address':'unguwan sarki kaduna',
        'school': 'ILC',
        'Work experience': '3 years'
}
print('''
name:{}
state:{}
number:{}
address:{}
school:{}
Work experience:{}

'''.format(personalinfo['name'],personalinfo['state'],personalinfo['number'],personalinfo['address'],personalinfo['school'],personalinfo['Work experience']))