word = input("Введите слово: ")
    
letter_count = len(word)
    
last_letter = word[-1]
    
is_first_last_same = word[0] == last_letter
    
print(f"Слово {word} имеет {letter_count} букв(ы), последняя буква \"{last_letter}\", "
        f"первая и последняя буквы {'совпадают' if is_first_last_same else 'не совпадают'}.")