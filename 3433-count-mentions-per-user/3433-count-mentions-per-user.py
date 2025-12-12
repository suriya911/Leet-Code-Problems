class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.sort(key = lambda x: (int(x[1]), x[0] == "MESSAGE"))
        online_lst = [0] * numberOfUsers
        mentions = [0] * numberOfUsers
        all_num = 0
        for event in events:
            if "MESSAGE" == event[0]:
                if "ALL" == event[2]:
                    all_num += 1
                elif "HERE" == event[2]:
                    time = int(event[1])
                    for i in range(numberOfUsers):
                        if online_lst[i] <= time:
                            mentions[i] += 1
                else:
                    for i in event[2].split():
                        mentions[int(i[2:])] += 1
            else:
                online_lst[int(event[2])] = int(event[1]) + 60
        for i in range(numberOfUsers):
            mentions[i] += all_num
        return mentions