class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        sh, sm, ss = map(int, startTime.split(':'))
        eh, em, es = map(int, endTime.split(':'))

        start = sh * 3600 + sm * 60 + ss
        end = eh * 3600 + em * 60 + es

        return end - start
        # sec=0
        # if len(startTime)==len(endTime):
        #     stH=int(startTime[:2])
        #     stM=int(startTime[3:5])
        #     stS=int(startTime[6:])
        #     endH=int(endTime[:2])
        #     endM=int(endTime[3:5])
        #     endS=int(endTime[6:])
        #     if 
        #     sec=(endH*60*60+endM*60+endS)-(stH*60*60+stM*60+stS)
        # return sec
        