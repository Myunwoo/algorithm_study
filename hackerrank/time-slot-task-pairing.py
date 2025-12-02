def findTaskPairForSlot(taskDurations, slotLength):
    dic = {}
    for i in range(len(taskDurations)):
        if slotLength - taskDurations[i] in dic:
            return [dic[slotLength - taskDurations[i]], i]
        dic[taskDurations[i]] = i
    return [-1, -1]