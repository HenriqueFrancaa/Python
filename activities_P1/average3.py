n1,n2,n3,n4 = input().split(" ")
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = (n1 * 2 + n2 * 3 + n3 * 4 + n4) / 10

print(f"Media: {media:.1f}")
if media >= 7.0:
    print("Aluno aprovado.")


if media >= 5.0:
    if media <= 6.9:
        print("Aluno em exame.")
        n5 = float(input())
        print(f"Nota do exame: {n5:.1f}")
        media2 = (n5 + media) / 2
        if media2 >= 5.0:
            print("Aluno aprovado.")
        if media2 <= 4.9:
            print("Aluno reprovado.")
        media_final = media2
        print(f"Media final: {media_final:.1f}")

else:
    print("Aluno reprovado.")
