# You are given several logs that each log contains a unique id and timestamp. 
# Timestamp is a string that has the following format: Year:Month:Day:Hour:Minute:Second, 
# for example, 2017:01:01:23:59:59. All domains are zero-padded decimal numbers.
# Design a log storage system to implement the following functions:
# void Put(int id, string timestamp): Given a log's unique id and timestamp, store the log in your storage system.
# int[] Retrieve(String start, String end, String granularity): 
# Return the id of logs whose timestamps are within the range from start to end. 
# Start and end all have the same format as timestamp. 
# However, granularity means the time level for consideration. 
# For example, start = "2017:01:01:23:59:59", end = "2017:01:02:23:59:59", granularity = "Day", 
# it means that we need to find the logs within the range from Jan. 1st 2017 to Jan. 2nd 2017.

# Example 1:
# put(1, "2017:01:01:23:59:59");
# put(2, "2017:01:01:22:59:59");
# put(3, "2016:01:01:00:00:00");
# retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Year"); // return [1,2,3], 
# because you need to return all logs within 2016 and 2017.
# retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Hour"); // return [1,2], 
# because you need to return all logs start from 2016:01:01:01 to 2017:01:01:23, 
# where log 3 is left outside the range.

# Note:
# There will be at most 300 operations of Put or Retrieve.
# Year ranges from [2000,2017]. Hour ranges from [00,23].
# Output for Retrieve has no order required.

class LogSystem(object):
    # 提取对应的timestamp序列，并比较字典序。
    # 因为存储格式相同， 只需要比较对应timestamp序列的字典序即可。
    def __init__(self):
        self.logs = []

    def put(self, id, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: None
        """
        self.logs.append((id, timestamp))

    def retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        index = {'Year': 5,'Month': 8,'Day': 11,'Hour': 14,'Minute': 17,'Second': 20}[gra]
        start = s[:index]
        end = e[:index]
        return [ id for id, timestamp in self.logs if start <= timestamp[:index] <= end]


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)