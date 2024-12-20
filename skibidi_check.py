text=input("Enter some text: ")
new_text=text.lower()
new_text_2=new_text.split()
count=0
indices=[]
for index, word in enumerate(new_text_2):
    if "skibidi" in word:
        count=count+1
        indices.append(index)
print(count)
print(indices)
