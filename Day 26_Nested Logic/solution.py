# Enter your code here. Read input from STDIN. Print output to STDOUT
d1, m1, y1 = map(int, input().split())  # actual return date
d2, m2, y2 = map(int, input().split())  # due date

fine = 0

if y1 > y2:
    fine = 10000
elif y1 == y2:
    if m1 > m2:
        fine = 500 * (m1 - m2)
    elif m1 == m2 and d1 > d2:
        fine = 15 * (d1 - d2)

print(fine)
