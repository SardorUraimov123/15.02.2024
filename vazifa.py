# # 1-misol
# import multiprocessing

# def harfni_raqamga_ayirish(harf):
#     harflar = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
#     for indeks, qator in enumerate(harflar, start=2):
#         if harf.lower() in qator:
#             return indeks
#     return None

# def ish_bajarish(harf):
#     return harfni_raqamga_ayirish(harf) or 0

# def main():
#     input_soz = input("Soz kiriting: ")

#     pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
#     raqamlar_soni = sum(pool.map(ish_bajarish, (harf for harf in input_soz if harf.isalpha())))
#     pool.close()
#     pool.join()

#     print(f"{input_soz} sozda {raqamlar_soni} marta yoziladi.")

# if __name__ == "__main__":
#     main()
# # 2-misol
# import multiprocessing

# def ochirish_teglari(input_teglar, teg):
#     return input_teglar.replace(teg, ''), input_teglar.count(teg)

# def main():
#     input_teglar = input("Teglardan iborat so'zlar kiriting: ")

#     teglar = ['!', '@', '#', '$', '%', '^', '&', '*', '<', '>', '?', '/', '\\']
#     pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    
#     results = pool.starmap(ochirish_teglari, [(input_teglar, teg) for teg in teglar])
#     pool.close()
#     pool.join()

#     teglarlar_ochirilgan, teglar_soni = zip(*results)

#     print(f"Teglardan {sum(teglar_soni)} ta bo'lib, ajratingiz: {teglarlar_ochirilgan[-1]}")

# if __name__ == "__main__":
#     main()
# # 3-misol
# import multiprocessing

# def tartibla_va_qaytar(raqamlar):
#     return ''.join(sorted(raqamlar))

# def main():
#     input_raqamlar = input("Raqamlarni kiriting: ")

#     if not input_raqamlar.isdigit():
#         print("Noto'g'ri kiritish. Raqamlardan iborat bo'lishi kerak.")
#         return

#     chunk_size = max(1, len(input_raqamlar) // multiprocessing.cpu_count())
    
#     pool = multiprocessing.Pool()
#     raqamlar_qismi_list = [input_raqamlar[i:i + chunk_size] for i in range(0, len(input_raqamlar), chunk_size)]
    
#     natijalar = pool.map(tartibla_va_qaytar, raqamlar_qismi_list)
    
#     pool.close()
#     pool.join()

#     raqamlar_tartiblangan = ''.join(sorted(''.join(natijalar)))
#     print(f"Kichikdan kattaga qaratib tartiblangan raqamlar: {raqamlar_tartiblangan}")

# if __name__ == "__main__":
#     main()
# 4-misol
# 5-misol
def find_error_pairs(numbers_list):
    error_pairs = []
    for i in range(1, len(numbers_list)):
        if numbers_list[i] < numbers_list[i-1]:
            error_pairs.append((numbers_list[i-1], numbers_list[i]))
    return error_pairs

input_numbers = input("Iltimos, raqamlarni biror tartibda kiriting: ")
numbers_list = [int(i) for i in input_numbers.split()]
print("Rost emas juftliklar:", find_error_pairs(numbers_list))
# 6-misol
def count_syllables(word:str):
    count = 0
    vowels = 'aeiou'
    for char in word.lower():
        if char in vowels:
            count += 1
    return count

def count_syllables_in_text(text:str):
    words = {}
    for word in text.split():
        words[word] = count_syllables(word)
    return words

input_text = input("Iltimos, biror matn kiriting: ")
print("So'zlar bo'g'inlar soni:", count_syllables_in_text(input_text))
# 7misol
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def count_prime_numbers_up_to(number):
    prime_count = 0
    for i in range(2, number + 1):
        if is_prime(i):
            prime_count += 1
    return prime_count

input_number = int(input("Iltimos, bir son kiriting: "))
print("Tub sonlar soni:", count_prime_numbers_up_to(input_number))
# 8-misol
def find_largest_until_max(numbers_list):
    if not numbers_list:
        return None
    
    max_num = numbers_list[0]
    for num in numbers_list:
        if num > max_num:
            max_num = num
        else:
            break  
    return max_num

input_numbers = input("Raqamlarni kiriting (bo'sh joylar bilan ajrating): ").split()
numbers_list = [int(num) for num in input_numbers if num.strip()] 
largest_num = find_largest_until_max(numbers_list)
if largest_num is not None:
    print("Eng katta raqam:", largest_num)
else:
    print("Siz bo'sh ro'yxat kiritdingiz.")
