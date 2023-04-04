import pandas as pd

import matplotlib.pyplot as plt


tata_motors=pd.read_csv("C:/Users/svukk/PycharmProjects/TheoryEL/TATAMOTORS.csv")
tata_steel=pd.read_csv("C:/Users/svukk/PycharmProjects/TheoryEL/TATASTEEL.csv")
tcs=pd.read_csv("C:/Users/svukk/PycharmProjects/TheoryEL/TCS.csv")


tata_motors["Date"]=pd.to_datetime(tata_motors["Date"])
tata_steel["Date"]=pd.to_datetime(tata_steel["Date"])
tcs["Date"]=pd.to_datetime(tcs["Date"])

tata_motors=tata_motors.drop(['Trades','Deliverable Volume','%Deliverble'], axis=1)
tata_steel=tata_steel.drop(['Trades','Deliverable Volume','%Deliverble'], axis=1)
tcs=tcs.drop(['Trades','Deliverable Volume','%Deliverble'], axis=1)


tata_motors['Month']=tata_motors["Date"].dt.month
tata_motors['Year']=tata_motors["Date"].dt.year
tata_motors['Day']=tata_motors["Date"].dt.day

tata_steel['Month']=tata_steel["Date"].dt.month
tata_steel['Year']=tata_steel["Date"].dt.year
tata_steel['Day']=tata_steel["Date"].dt.day

tcs['Day']=tcs['Date'].dt.day
tcs['Year']=tcs['Date'].dt.year
tcs['Month']=tcs['Date'].dt.month



plt.figure(figsize=(20,7))
plt.plot(tata_motors['Date'],tata_motors['Open'],color='blue',label='Tata Motors')
plt.plot(tata_steel['Date'],tata_steel['Open'],color='grey',label='Tata Steel')
plt.plot(tcs['Date'],tcs['Open'],color='orange',label='TCS')
plt.title("Relation between Tata Motors, Tata Steel and TCS Price")
plt.xlabel("Year")
plt.ylabel("Price")
plt.legend(title="")
#plt.show()


plt.figure(figsize=(20,7))
plt.plot(tata_motors['Date'],tata_motors['Volume'],color='blue',label='Tata Motors')
plt.plot(tata_steel['Date'],tata_steel['Volume'],color='grey',label='Tata Steel')
plt.plot(tcs['Date'],tcs['Volume'],color='orange',label='TCS')
plt.title("Relation between Tata Motors, Tata Steel and TCS Volume")
plt.xlabel("Year")
plt.ylabel("Volume")
plt.legend(title="")
#plt.show()



fig = plt.figure()
tcs['MA50'] = tcs['Open'].rolling(50).mean()
tcs['MA200'] = tcs['Open'].rolling(200).mean()
tcs['Open'].plot(figsize = (15,7))
tcs['MA50'].plot()
tcs['MA200'].plot()
plt.legend()
plt.grid()
plt.show()


fig = plt.figure()
tcs['returns'] = (tcs['Close']/tcs['Close'].shift(1)) -1
tata_motors['returns'] = (tata_motors['Close']/tata_motors['Close'].shift(1))-1
tata_steel['returns'] = (tata_steel['Close']/tata_steel['Close'].shift(1)) - 1
tcs['returns'].hist(bins = 100, label = 'TCS', alpha = 0.5, figsize = (15,7))
tata_motors['returns'].hist(bins = 100, label = 'tata_motors', alpha = 0.5)
tata_steel['returns'].hist(bins = 100, label = 'tata_steel', alpha = 0.5)
plt.legend()
plt.show()

