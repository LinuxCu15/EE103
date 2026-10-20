# Part 5: Fundraiser Tickets (1000 Total) - Single Loop Optimization
for alyssa in range(1001):
    ben = alyssa - 20
    cindy = alyssa * 2
    if alyssa + ben + cindy == 1000:
        print(f"1000 bilet için Alyssa'nın sattığı bilet sayısı: {alyssa}")
        break