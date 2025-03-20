import csv


# data format:
# 1. id: int
# 2. text: str
# 3. sentiment: int (-1 = negative, 0 = neutral, 1 = positive)
# 4. title: Optional[str]
# 5. summary: Optional[str]
# 6. type: Optional[str]
# 7. url: Optional[str]
data = []
id = 0


for i in range(6):
    with open(f"raw/dataset_{i}.csv", encoding="ISO-8859-1") as f:
        sentiment_map = {"neutral": 0, "positive": 1, "negative": -1, "none": 0}
        reader = csv.reader(f, delimiter=",")
        print(f"reading dataset {i}...")

        # Labeled datasets
        if i == 2:
            next(reader)
            for row in reader:
                data.append([id, row[3], sentiment_map[row[6]], row[2], "", row[7], row[4]])
                id += 1
        if i == 0:
            for row in reader:
                data.append([id, row[1], sentiment_map[row[0]], "", "", "", ""])
                id += 1
        if i == 1:
            next(reader)
            for row in reader:
                data.append([id, row[3], sentiment_map[row[4].rstrip().lower()], row[1], row[2], "", ""])
                id += 1
        if i == 3:
            next(reader)
            for row in reader:
                data.append([id, row[2], sentiment_map[row[9]], "", "", "", row[1]])
                id += 1
        if i == 4:
            next(reader)
            for row in reader:
                data.append([id, row[3], 1 if int(float(row[2])) == 1 else -1, row[0], row[1], "", row[4]])
                id += 1

        # Unlabeled datasets
        if i == 5:
            next(reader)
            for row in reader:
                data.append([id, row[5], "", row[3], row[8], row[0], row[1]])
                id += 1


with open("consolidated.csv", "w") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow(["Id", "Text", "Sentiment", "Title", "Summary", "Type", "URL"])
    writer.writerows(data)


