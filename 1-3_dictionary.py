geonwoo = {
    "Name" : "건우",
    "Age" : 27,
    "Job" : "student",
    "Address" : "Ulsan"
}

print(type(geonwoo))

geonwoo["학번"] = 20191755
print(geonwoo)

geonwoo["Hobby"] = ["Game", "Coding", "배드민턴"]
print(geonwoo)

Answer = f"건우의 취미는 {geonwoo['Hobby']}입니다"
print(Answer)
