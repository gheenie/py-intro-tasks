# Take a look at the following variables



tutor = 'david john bartlett'

title = 'Mr'

dob = "30/12/1996"

job_title = "Senior Tutor"

pronouns =  'he/him'


# Use them to create new strings with the following values:


# 1. first_name = David

name = tutor.split()

first_name_lowercase = name[0]
first_name = first_name_lowercase.capitalize()

# 2. surname = Bartlett

surname_lowercase = name[2]
surname = surname_lowercase.capitalize()

# 3. reverse_reverse = tteltraB divaD

reverse_reverse = f'{first_name} {surname}'[::-1]

# 4. digital_signature = David J. Bartlett

middle_name_initial = name[1][0].capitalize()

digital_signature = f'{first_name} {middle_name_initial}. {surname}'

# 5. side_hustle = DJ Bartlett

first_name_initial = first_name[0]

side_hustle = f'{first_name_initial}{middle_name_initial} {surname}'

# 6. us_dob = 12/30/96

dob_split = dob.split('/')
dob_day = dob_split[0]
dob_month = dob_split[1]
dob_year = dob_split[2]

us_dob = f'{dob_month}/{dob_day}/{dob_year[2:]}'

# 7. slack_handle = David-NC

slack_handle = f'{first_name}-NC'

# 8. twitter_handle = @dbart3012

twitter_handle = f'@{first_name_lowercase[0]}{surname_lowercase[0:4]}{dob_day}{dob_month}'

# 9. formal_salutation = Mr D Bartlett

formal_salutation = f'{title} {first_name_initial} {surname}'

# 10. email_signature = David Bartlett (he/him) - Senior Tutor

email_signature = f'{first_name} {surname} ({pronouns}) - {job_title}'

# 11. sandwich = bartdavidlett

sandwich = f'{surname_lowercase[0:4]}{first_name_lowercase}{surname_lowercase[4:]}'

# 12. pig_latin = Avidday Artlettbay

pig_latin = 'placeholder'

print(sandwich)
