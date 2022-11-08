def solution(prices, buyIndicator, sellIndicator):
    # prices is a list of prices.
    # buyIndicator is a list of arbitrary length, 1s and -1, indicating moves up and down.
    # sellIndicator is of the same format as buyIndicator.
    position = [0]*len(prices)
    currIndicator = [0]
    for i in range(1, len(prices)):
        if prices[i-1] < prices[i]:
            currIndicator.append(1)
        elif prices[i-1] > prices[i]:
            currIndicator.append(-1)
        else:
            currIndicator.append(0)

        position[i] = position[i-1]

        if len(currIndicator) >= len(buyIndicator) and currIndicator[-1] != 0:
            left = len(buyIndicator)-1
            for x in range(len(currIndicator)-1,-1,-1):
                if currIndicator[x] == buyIndicator[left]:
                    left -= 1
                elif currIndicator[x] != 0:
                    break
                if left == -1:
                    position[i] += 1
                    break
        
        if len(currIndicator) >= len(sellIndicator) and currIndicator[-1] != 0:
            left = len(sellIndicator)-1
            for x in range(len(currIndicator)-1,-1,-1):
                if currIndicator[x] == sellIndicator[left]:
                    left -= 1
                elif currIndicator[x] != 0:
                    break
                if left == -1:
                    position[i] -= 1
                    break

    return position

# print(solution([51, 56, 56, 58, 60, 59, 54, 57, 52, 48], [1, 1], [-1, -1, 1]))
print(solution([51, 56, 56, 58, 60, 60, 61, 61, 62, 62], [1, 1], [-1, -1, 1]))