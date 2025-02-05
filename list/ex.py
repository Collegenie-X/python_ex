csv_data = "name,age,score\nAlice,30,85\nBob,25,92\nCharlie,35,88"
rows = [item for line in csv_data.split('\n') for item in line.split(',')]
print(rows)
