print('Interest Calculator:')

amount = float(input('Principal amount ?'))
roi = float(input('Rate of Interest ?'))
yrs = int(input('Duration (no. of years) ?'))

total = (amount * pow(1 + (roi/100), yrs))
interest = total - amount
print('\nInterest = %0.2f' %interest)