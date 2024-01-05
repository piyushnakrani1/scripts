class DataStream:
    def __init__(self):
        # last timestamp for each unique string will be stored in dict
        self.last_timestamp = {}

    def output_data_stream(self, timestamp: int, data_str: str) -> bool:
        # check if string is exists in last timestamp and in the last timestamp the value of data str +5 is grater than time stamp
        if data_str in self.last_timestamp and self.last_timestamp[data_str] + 5 > timestamp:
            return False
        else:
            # update the last time stamp of current string
            self.last_timestamp[data_str] = timestamp
            return True

data_stream = DataStream()
output = [
    data_stream.output_data_stream(timestamp = 0, data_str = "hello"),
    data_stream.output_data_stream(timestamp = 1, data_str = "world"),
    data_stream.output_data_stream(timestamp = 6, data_str = "hello"),
    data_stream.output_data_stream(timestamp = 7, data_str = "hello"),
    data_stream.output_data_stream(timestamp = 8, data_str = "world")
]
