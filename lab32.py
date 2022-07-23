d=[{"v":"s001"},{"v":"s002"},{"v1":"s001"},{"v1":"s005"},{"v111":"s005"},{"v":"s009"},{"v111":"s007"}]
print("original list:",d)
unique_value=set(value for dic in d for value in dic.values())
print("Unique value:",unique_value)