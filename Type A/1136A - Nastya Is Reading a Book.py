n = int(input())

chapter_border = []
for i in range(n):
    chapter_border.append(list(map(int, input().split())))

current_page = int(input())
current_chapter = [start <= current_page <= end for (start, end) in chapter_border]

print(n - current_chapter.index(True))