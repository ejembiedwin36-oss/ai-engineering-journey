import tracemalloc


tracemalloc.start()

data = [list(range(1000)) for _ in range(1000)]
labels = [i % 2 for i in range(1000)]
processed = [row[:500] for row in data]

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics("lineno")

for stat in top_stats[:5]:
    print(stat)