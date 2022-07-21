a = {1:{'course':'Python','fees':15000},
    2:{'course':'JavaScript','fees':20000}}
print("ID:")
for id in a:
    print(id)
print()
print("Keys:")
for id in a:
    for k in a[id]:
        print(k, "=" ,a[id][k])