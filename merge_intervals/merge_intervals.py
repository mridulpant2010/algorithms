def merge_intervals(intervals):
    if len(intervals)<2:
        return     
    intervals.sort(key=lambda x:x[0])
    mergedIntervals=[]
    interval_len = len(intervals)
    prev_elem=intervals[0]
    for i in range(1,interval_len):
        curr_elem=intervals[i]
        a_start= prev_elem[0]; a_end =prev_elem[1];
        b_start= curr_elem[0]; b_end = curr_elem[1];
        #if it is overlapping :
        if b_start <=a_end:
            prev_elem[1]=max(a_end,b_end)
        else:
            mergedIntervals.append(prev_elem)
            prev_elem=curr_elem       
    mergedIntervals.append(prev_elem)
    return mergedIntervals
    
if __name__ == '__main__':
    intervals=[[1,4],[2,5],[7,9]]
    print(*merge_intervals(intervals))
    intervals1=[[6,7],[2,4],[5,9]]
    print(*merge_intervals(intervals1))
    intervals2=[[1,4],[2,6],[3,5]]
    print(*merge_intervals(intervals2))
    