a = input("Введите отзыв: ")
if "Не плохо" in a or "не плохо" in a:
    a = a.replace("Не плохо", "Хорошо")
    a = a.replace("не плохо", "хорошо")
elif "Не плохая" in a or "не плохая" in a:
    a = a.replace("Не плохая", "Хорошая")
    a = a.replace("не плохая", "хорошая")
elif "Не плохой" in a or "не плохой" in a:
    a = a.replace("Не плохой", "Хороший")
    a = a.replace("не плохой", "хороший")
elif "Не плохие" in a or "не плохие" in a:
    a = a.replace("Не плохие", "Хорошие")
    a = a.replace("не плохие", "хорошие")
elif "Не плохое" in a or "не плохое" in a:
    a = a.replace("Не плохое", "Хорошие")
    a = a.replace("не плохое", "хорошие")
print("Итоговый отзыв: ", a)