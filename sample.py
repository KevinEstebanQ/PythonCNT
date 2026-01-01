import json
import random
from datetime import timedelta, datetime
import faker
import wx
import pandas as pd
import matplotlib.pyplot as plt

faker = faker.Faker()

def get_name_gender():

    if random.random() > 0.5:
        name, Gender = faker.name_male(), "M"
    else:
        name, Gender = faker.name_female(), "F"
    parts = name.split()
    FirstName = parts[0]
    LastName = parts[-1]
    return FirstName, LastName, Gender

def CreateSensorData():
    SensorDict = {}
    start_date = datetime(2015, 1,1, 0, 0)
    
    for i in range(1000):
        TS = start_date + timedelta(hours=i*6)
        date_string = TS.strftime("%Y-%m-%d")
        time_string = TS.strftime("%H:%M:%S")
        
        outside_temp = random.uniform(70, 95)
        outside_humidity = random.uniform(50,95)
        
        room_temp = outside_temp - random.uniform(0,10)
        room_humidity = outside_humidity - random.uniform(0,10)
        
        DataNumber = "SensorData#"+str(i+1)
        SensorDict.update({DataNumber:{"Date": date_string,
                                       "time": time_string,
                                        "Outsidetemperature": round(outside_temp,2),
                                        "OutsideHumidity": round(outside_humidity, 2),
                                        "RoomTemperature": round(room_temp, 2),
                                        "RoomHumidity": round(room_humidity, 2)}})
    return SensorDict




def CreateUsers(users): 



    for _ in range(1000):
        FirsName, LastName, Gender = get_name_gender() 
        user = {"FirstName": FirsName,
                "LastName": LastName,
                "age":faker.random_int(min=18,max=90),
                "gender":Gender,
                "Username":faker.user_name(),
                "address": faker.address(),
                "email": faker.email(),
                "Sensor":CreateSensorData()
               }
        users.append(user)
    return users

class IotAPP(wx.Frame):
    def __init__(self, *args, **kw):
        super(IotAPP, self).__init__(*args, **kw)

        self.users = []
        self.df = pd.DataFrame()

        self.InitUI()

    def InitUI(self):
        self.panel = wx.Panel(self)

        menubar = wx.MenuBar()

        fileMenu = wx.Menu()
        genItem  = fileMenu.Append(wx.ID_ANY, 'Generate IOT')
        JsonItem  = fileMenu.Append(wx.ID_ANY, 'Generate JSON')
        CSVItem  = fileMenu.Append(wx.ID_ANY, 'Generate CSV')
        menubar.Append(fileMenu, '&file')

        statsMenu = wx.Menu()
        descItem = statsMenu.Append(wx.ID_ANY, 'Descriptive')
        plotA = statsMenu.Append(wx.ID_ANY, 'PlotA')
        plotB = statsMenu.Append(wx.ID_ANY, 'PlotB')
        plotC = statsMenu.Append(wx.ID_ANY, 'PlotC')
        menubar.Append(statsMenu, '&Statistics')

        self.Bind(wx.EVT_MENU, self.OnGenerateIoT, genItem)
        self.Bind(wx.EVT_MENU, self.OnSaveJson, JsonItem)
        self.Bind(wx.EVT_MENU, self.OnSaveCSV, CSVItem)
        self.Bind(wx.EVT_MENU, self.OnDescriptive, descItem)
        self.Bind(wx.EVT_MENU, self.OnPlotA, plotA)
        self.Bind(wx.EVT_MENU, self.OnPlotB, plotB)
        self.Bind(wx.EVT_MENU, self.OnPlotC, plotC)


        self.SetMenuBar(menubar)
        self.SetTitle('IoT Data Generator')
        self.Centre()


    def OnGenerateIoT(self, event):
        global users, df
        users = CreateUsers([])
        self.users = users
        flattened = []
        for user in users:
            for sid, sensor in user["Sensor"].items():
                flattened.append({
                    "FirstName": user["FirstName"],
                    "LastName": user["LastName"],
                    "Username": user["Username"],
                    "SensorID": sid,
                    "Date": sensor["Date"],
                    "Time": sensor["time"],
                    "OutsideTemperature": sensor["Outsidetemperature"],
                    "OutsideHumidity": sensor["OutsideHumidity"],
                    "RoomTemperature": sensor["RoomTemperature"],
                    "RoomHumidity": sensor["RoomHumidity"]
                })
        self.df = pd.DataFrame(flattened)
        wx.MessageBox("Generated 1,000 users with sensor data.", "Success")
    
    def OnSaveJson(self, event):
        with wx.FileDialog(self, 'Save JSON', wildcard = "JSON files (*.json)|*.json",
                           style = wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as dialog:
            if dialog.ShowModal() == wx.ID_CANCEL:
                return
            path = dialog.GetPath()
            with open(path, 'w') as f:
                json.dump(self.users, f, indent = 2)
    
    def OnSaveCSV(self, event):
        with wx.FileDialog(self, "Save CSV", wildcard="CSV files (*.csv)|*.csv",
                           style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as dialog:
            if dialog.ShowModal() == wx.ID_CANCEL:
                return
            path = dialog.GetPath()
            self.df.to_csv(path, index=False)
    
    def OnDescriptive(self, event):
        if self.df.empty:
            wx.MessageBox("No data generated yet.", "Error")
            return
        desc = self.df.describe().to_string()
        wx.MessageBox(desc, "Descriptive Statistics")
    
    def OnPlotA(self, event):
        self.ShowHistogram(['OutsideTemperature'], 'Outside Temp Histogram')
    
    def ShowHistogram(self, columns, title):
        if self.df.empty: return
        self.df[columns].hist(figsize=(10,6))
        plt.suptitle(title)
        plt.show()
    
    def OnPlotB(self, event):
        if self.df.empty: return
        plt.figure(figsize=(10,5))
        plt.plot(self.df["OutsideTemperature"][:100], label="Outside Temp")
        plt.plot(self.df["RoomTemperature"][:100], label="Room Temp")
        plt.title("Outside vs Room Temperature")
        plt.legend()
        plt.grid(True)
        plt.show()
    
    def OnPlotC(self, event):
     self.ShowHistogram(['OutsideTemperature', 'RoomTemperature', 'OutsideHumidity', 'RoomHumidity'], 'Combined Histogram')

if __name__ == '__main__':
    app = wx.App(False)
    frame = IotAPP(None)
    frame.Show()
    app.MainLoop()