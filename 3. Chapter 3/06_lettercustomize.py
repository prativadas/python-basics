appointment_letter = ''' Dear  <|NAME|>, Congratulations!!!

You are selected as AP in DU. Hope you will join soon.

Regards, Prat


Date: <|DATE|>

'''
print(appointment_letter)

# make template of this letter. change name and date for anyone.

name = input('enter candidate name:')

date = input('enter date:')

appointment_letter = appointment_letter.replace(' <|NAME|>', name)  # always assign appointment letter with new replaced values.

appointment_letter = appointment_letter.replace(' <|DATE|>', date)

print(appointment_letter)
