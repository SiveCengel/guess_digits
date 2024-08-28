import random

def get_digits(number):
    digits = []
    # print("number before while:",number)
    while number > 0:
        # print("number before:",number)
        digit = number % 10
        # print("digit:",digit)
        digits.append(digit)
        number //= 10
        # print("number after:",number)
        digits.reverse()
    return digits

def is_unique_digits(number):
    digits = get_digits(number)
    # print(digits)
    return len(set(digits)) == len(digits)

def play_game():
    # Birbirinden farklı 3 basamaklı sayı oluştur
    secret_code = random.randint(100, 999)
    while not is_unique_digits(secret_code):
        secret_code = random.randint(100, 999)
    secret_digits = get_digits(secret_code)
    print(f"Gizli kod: {secret_code}")
    # print('Gizli kod: ' + str(secret_code))
    # print("Gizli kod: {}".format(secret_code))



    attempts = 0
  
    while True:
        # user_input = int(input("Tahmininizi girin (3 basamaklı, birbirinden farklı rakamlardan oluşan bir sayı): "))
        # while not is_unique_digits(user_input):
        # birbirinden farklı rakamlardan oluşan 3 basmakalı sayı girilene kadar döngü devanm eder. 
        while True:
            user_input = int(input("Lütfen 3 basamaklı, birbirinden farklı rakamlardan oluşan bir sayı girin: "))
            if is_unique_digits(user_input):
                break
        # girilen 3 basmaaklı sayının rakamlarını al      
        guess_digits = get_digits(user_input)
        
        correct_position = 0 #rakam var ve yerinde.
        correct_digit = 0  #rakam var ama doğru yerde değil.
        
        # Doğru basamak ve konumda olanları kontrol et
        for i in range(3):
            print("tahmin edilen rakam :",i, guess_digits[i])
            if guess_digits[i] == secret_digits[i]:
                correct_position += 1
                # print("yerinde tutan rakam : ",guess_digits[i])
            elif str(guess_digits[i]) in str(secret_code):
                correct_digit += 1
                # print("mevcut ama yerinde olmayan rakam",guess_digits[i])
            else:
                pass
                # print("mevcut olmayan rakam",guess_digits[i])
        
        attempts += 1
        
        print(f"\nDoğru değer ve konumda {correct_position} adet, doğru değer ama yanlış konumda {correct_digit} adet.")
        
        if correct_position == 3:
            print(f"Tebrikler! {attempts} denemede buldunuz.")
            break


play_game()