import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data_text = """Date 
重试
  
错误原因
January 
重试
  
错误原因
February 
重试
  
错误原因
March  三月
April 
重试
  
错误原因
May 
重试
  
错误原因
June 
重试
  
错误原因
July 
重试
  
错误原因
August  八月
September 
重试
  
错误原因
October 
重试
  
错误原因
November 
重试
  
错误原因
December 
重试
  
错误原因
01
PH
NT
NT
PH
PH
PH
3,935.00**
-
-
-
NT
-
02
4,819.00
PH
PH
4,835.00
3,968.00
PH
-
NT
-
-
PH
-
03
4,726.00
4,620.50
4,741.00
4,791.00
NT
3,953.00
-
PH
-
-
-
-
04
NT
4,599.00
4,677.50
4,764.50
PH
3,940.50
-
-
-
NT
-
-
05
PH
4,650.00
4,712.50
NT
3,870.00
3,936.00
NT
-
-
PH
-
-
06
4,642.50
4,675.50
4,776.50
PH
3,878.00
3,913.50
PH
-
NT
-
-
NT
07
4,709.00
4,731.50
4,817.00
4,644.00
3,781.00
NT
-
-
PH
-
-
PH
08
4,702.50
NT
NT
4,576.50
3,779.50
PH
-
-
-
-
NT
-
09
4,631.00
PH
PH
4,489.50
3,787.00
3,949.50
-
NT
-
-
PH
-
10
4,725.00
4,767.50
4,840.00
4,520.00
NT
3,938.00
-
PH
-
-
-
-
11
NT
PH
4,798.00
4,498.00
PH
3,854.50
-
-
-
NT
-
-
12
PH
4,850.50
4,801.00
NT
PH
3,861.50
NT
-
-
PH
-
-
13
4,810.00
4,790.50
4,806.50
PH
3,868.50
3,909.00
PH
-
NT
-
-
NT
14
4,789.50
4,765.00
4,814.50
4,418.50
3,969.00
NT
-
-
PH
-
-
PH
15
4,632.50
NT
NT
4,332.00
3,882.50
PH
-
-
-
-
NT
-
16
4,619.50
PH
PH
4,246.50
3,879.00
4,044.50
-
NT
-
-
PH
-
17
4,577.50
4,736.50
4,749.00
4,262.00
NT
4,059.50
-
PH
-
-
-
-
18
NT
4,742.50
PH
4,180.00
PH
4,076.00
-
-
-
NT
-
-
19
PH
4,783.00
4,688.00
NT
3,889.50
4,089.50
NT
-
-
PH
-
-
20
4,578.50
4,805.00
4,707.00
PH
3,944.50
4,076.50
PH
-
NT
-
-
NT
21
4,536.50
4,868.00
4,721.50
4,094.00
3,907.50
NT
-
-
PH
-
-
PH
22
4,565.50
NT
NT
4,113.00
3,850.00
PH
-
-
-
-
NT
-
23
4,517.00
PH
PH
4,142.50
3,860.00
4,079.00
-
NT
-
-
PH
-
24
4,527.50
4,781.00
4,669.50
4,157.50
NT
4,000.00
-
PH
-
-
-
-
25
NT
4,792.50
4,634.50
4,172.50
PH
3,963.00
-
-
-
NT
-
-
26
PH
4,757.00
4,624.50
NT
3,817.00
3,956.50
NT
-
-
PH
-
-
27
4,566.00
4,687.50
4,677.00
PH
3,841.00
PH
PH
-
NT
-
-
NT
28
4,560.00
NT
4,705.00
4,075.00
3,880.50
NT
-
-
PH
-
-
PH
29
PH
NT
4,018.00
3,952.00
PH
-
-
-
-
NT
-
30
PH
PH
3,974.50
3,854.50
3,912.50
-
NT
-
-
PH
-
31
4,600.00
PH
NT
-
PH
-"""

# Filter out blank lines and control messages
lines = [line.strip() for line in data_text.splitlines() if line.strip() not in ("重试", "错误原因", "")]
# Extract header
months = lines[1:13]
lines = lines[13:]

# Build data rows
records = []
while lines:
    day = lines[0]
    values = lines[1:13]
    if not values:
        break
    records.append([day] + values)
    lines = lines[13:]

# Create DataFrame
columns = ["Day"] + months
_df = pd.DataFrame(records, columns=columns)

# Replace markers with NaN and convert to numbers
_df.replace({"PH": np.nan, "NT": np.nan, "-": np.nan, "3,935.00**": "3935.00"}, inplace=True)
for m in months:
    _df[m] = _df[m].str.replace(",", "", regex=False)
    _df[m] = _df[m].astype(float)

_df.set_index("Day", inplace=True)

# Plot each month's data line
_df.plot(figsize=(10, 6))
plt.title("Daily Data by Month")
plt.ylabel("Value")
plt.tight_layout()
plt.show()
