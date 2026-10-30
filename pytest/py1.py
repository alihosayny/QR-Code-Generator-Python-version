age: int = 9
# age = 'Ali'
# age = "test"

# print(type(age))

# # --- EXEMPLES DE CONDITIONS (if / elif / else) ---

# # 1. Condition simple (if)
# if age < 18:
#     print("La personne est mineure.")

# # 2. Condition alternative (if / else)
# if age >= 18:
#     print("Accès autorisé (Majeur).")
# else:
#     print("Accès refusé (Mineur).")

# # 3. Conditions multiples (if / elif / else)
# if age < 12:
#     print("Catégorie : Enfant")
# elif age < 18:
#     print("Catégorie : Adolescent")
# elif age < 65:
#     print("Catégorie : Adulte")
# else:
#     print("Catégorie : Senior")

# # 4. Conditions combinées avec des opérateurs logiques (and, or)
# if age >= 6 and age <= 10:
#     print("L'enfant est à l'école primaire.")

# # 5. Condition en une seule ligne (Expression ternaire)
# statut = "Majeur" if age >= 18 else "Mineur"
# print(f"Statut : {statut}")

# if age != 10:
    # print('age different de 10')

# test1 = True
# test2 = False
# a = 5
# if(a>0) : 
#     print(test1)
# else : 
#     print(
#         test2
#     )    

listName = [1,"test",3 , 4,5]

while i < len(listName):
    print(listName[i])
    i+=1