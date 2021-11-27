#!/usr/bin/env python
# coding: utf-8

# In[2]:



def main():
    slovar = {"а": 1, "б": 2, "в": 3, "г": 4, "д": 5, "е": 6, "ё": 7,
            "ж": 8, "з": 9, "и": 10, "й": 11, "к": 12, "л": 13, "м": 14,
            "н": 15, "о": 16, "п": 17, "р": 18, "с": 19, "т": 20, "у": 21,
            "ф": 22, "х": 23, "ц": 24, "ч": 25, "ш": 26, "щ": 27, "ъ": 28,
            "ы": 29, "ь": 30, "э": 31, "ю": 32, "я": 34, " ": 34
            }
    slovar2 = {v: k for k, v in slovar.items()}
    
    text = input("Введите текст для шифрования: ").lower() 
    key = input("Введите ключ: ").lower()
    lengs = len(text)
    lengs_g = len(key)
    print("Длина текста",lengs, "\nДлина ключа",lengs_g)
    
    gamma = key
    while lengs >= lengs_g:
        gamma = gamma + key
        lengs_g = len(gamma)
    print("\nдорощенная гамма до длин:\n", gamma, "\nДлина гаммы",lengs_g)
    
    Text_in_numbers = list() 
    gamma_in_nambers = list()
    
    for i in text:
        Text_in_numbers.append(slovar[i])
    print("\nЧисла текста:\n", Text_in_numbers)
    
    for i in gamma:
        gamma_in_nambers.append(slovar[i])
    print("числа гаммы:\n", gamma_in_nambers)
    
    schifr_in_numbers = list() 
    ch = 0; j = 0 
    while j<lengs:
        a = (Text_in_numbers[j] + gamma_in_nambers[j])%34

        schifr_in_numbers.append(a)
        j+=1
        
    print("Числа зашифрованного текста:\n", schifr_in_numbers)
          
    textencrypted=""
    for i in schifr_in_numbers:
        textencrypted+=slovar2[i]
    print("\nЗашифрованный текст: ", textencrypted)
          
    listofdigits = list()
    for i in textencrypted:
        listofdigits.append(slovar[i])
    ch = 0
    listofdigits1 = list()
    for i in listofdigits:
        a = i - gamma_in_nambers[ch]
        if a < 1:
            a = 34 + a
        listofdigits1.append(a)
        ch+=1
    textdecrypted = ""
    for i in listofdigits1:
        textdecrypted+=slovar2[i]
    print("Расшифрованный текст: ", textdecrypted)


# In[3]:


if __name__ == '__main__':
    main()


# In[ ]:




