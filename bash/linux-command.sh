# 
grep "ERROR" application.log

# -c count
grep -c "ERROR" application.log

# find name ending with .log, modified time less than a day ago
find . -name "*.log" -mtime -1


