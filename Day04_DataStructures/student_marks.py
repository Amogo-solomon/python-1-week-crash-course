marks = {
    "maths": 85,
    "science": 90,
    "english": 88
}

print('maths:', marks['maths'])
print('science:', marks['science'])
print('english:', marks['english'])

total = sum(marks.values())
average = total/len(marks)

print('total score:', total)
print('average:', average)