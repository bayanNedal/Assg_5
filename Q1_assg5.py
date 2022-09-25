numbers = [12, 75, 150, 180, 145, 525, 50]
for i in range(len(numbers)):
    if numbers[i] > 500:
        break
    elif numbers[i] <= 150:
        if numbers[i] % 5 == 0:
            print(numbers[i])

# or
# for x in range(len(numbers)):
# if numbers[x] > 500:
#     break
# elif numbers[x] > 150:
#     continue
# elif numbers[x] % 5 == 0:
#     print(numbers[x])