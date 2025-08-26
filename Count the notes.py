

Amount = int(input("Please enter amount to withdraw"))
note_1 = (Amount//100)
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10

print("There are ",note_1,"100 rupee notes.")
print("There are",note_2,"50 rupee notes")
print("There are",note_3,"10 rupee notes")
