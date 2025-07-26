CPF = input('Enter a CPF (only numbers): ')

if CPF.isdigit():
    cpf_verification_number = CPF[:9]
    countdown = 10 # Countdown to calculate the CPF digits

    for i in range(2):
        sum_cpf_numbers = 0

        for n in cpf_verification_number:
            sum_cpf_numbers += int(n) * countdown
            countdown -= 1

        calculating_digit = (sum_cpf_numbers * 10) % 11
        cpf_digit = calculating_digit if calculating_digit <= 9 else 0

        # Resetting variables to calculate the second digit

        cpf_verification_number += str(cpf_digit) 
        countdown = 11

    # Checking CPF

    if cpf_verification_number == CPF:
        print('✅ This CPF is VALID')
    else:
        print('❌ This CPF is INVALID')

else:
    print('⚠️ Enter only the CPF numbers')