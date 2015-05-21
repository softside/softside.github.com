from datetime import datetime
from datetime import timedelta

# input :"2015-5-9 13:44","2015-5-14 11:44"
# output : ["2015-5-9 33:44","2015-5-10","2015-5-11","2015-5-12","2015-5-13","2015-5-14 13:44"]
def make_list(start,end):
    start = datetime.strptime(start,"%Y-%m-%d %M:%S")
    end = datetime.strptime(end,"%Y-%m-%d %M:%S")
    end_list = []
    end_list.append(start)
    d = (end - start).days
    for one in range(d):
        end_list.append(start+timedelta(days=1+one))
    end_list.append(end)
    return [one.strftime("%Y-%m-%d %M:%S") for one in end_list]

start = "2015-5-9 13:44"
end = "2015-5-9 15:44"
print make_list(start,end)
