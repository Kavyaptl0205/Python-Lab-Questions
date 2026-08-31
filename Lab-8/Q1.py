# Lab 4 - OTP Generator

import random

def generate_otp():
    otp = random.randint(100000, 999999)
    return otp

print("===== OTP GENERATOR =====")

otp = generate_otp()
print("Your OTP is:", otp)
entered_otp = int(input("Enter the OTP: "))

if entered_otp == otp:
    print("OTP verified successfully!")

else:
    print("Invalid OTP.")