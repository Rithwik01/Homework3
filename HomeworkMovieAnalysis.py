import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


f = pd.read_csv("/Users/rithwikkamalesh/Downloads/cinemaTicket_Ref.csv")

plt.plot(f["total_sales"])
plt.show()
plt.hist(f["ticket_price"])
plt.show()

# According to these graphs, when prices are high, the sales tend to be low, when prices are low sales tend to he high.


plt.plot(f["total_sales"])
plt.show()
plt.hist(f["ticket_price"])
plt.show()


#Question 2

plt.plot(f["total_sales"])
plt.plot(f["show_time"])



plt.plot(f["total_sales"])
plt.plot(f["date"])

#Question 3


#Question 4: Yes you can tell if a theatre is under-performing after seeing data that matches for other ones you can determine if a theatre is not doing well.