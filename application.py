import tkinter as tk
from tkinter import ttk

import weather

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        
        self.w = weather.Weather()

    def create_widgets(self):

        # search label control
        self.search_label = ttk.Label(self, text='City:').grid(row=1,column=1)

        # search text box control
        self.search_box = ttk.Entry(self)
        self.search_box.grid(row=1,column=2)  

        # quit button control
        #self.quit = ttk.Button(self, text="QUIT", command=self.master.destroy)
        #self.quit.grid(row=1, column=3)

        # search button control
        self.search = ttk.Button(self)
        self.search["text"] = "Search"
        self.search["command"] = self.location_by_name
        self.search.grid(row=1, column=3)

        # combobox for search options
        self.search_result_text = tk.StringVar()
        self.search_results_box = ttk.Combobox(self, textvariable=self.search_result_text)
        self.search_results_box.grid(row=2, column=2)

        # current weather button control
        self.current_weather_button = ttk.Button(self, text='Current', command=self.get_current_weather)

        self.current_temp_label = ttk.Label(self, text='Current:')
        self.current_temp_min_label = ttk.Label(self, text='Min:')
        self.current_temp_max_label = ttk.Label(self, text='Max:')

        self.current_temp = ttk.Label(self)
        self.current_temp_min = ttk.Label(self)
        self.current_temp_max = ttk.Label(self)

    def location_by_name(self):

        cities = self.w.list_city_by_name(self.search_box.get())

        self.search_results_box['values'] = tuple(cities)
        self.search_results_box.current(0)

        self.current_weather_button.grid(row=2, column=3)

    def get_current_weather(self):

        user_choice = self.search_result_text.get()

        for item in self.w.cities.keys():
            if self.w.cities[item] == user_choice:
                self.w.city_id = item

        current_weather = self.w.current_weather_id()

        self.current_temp_label = ttk.Label(self, text='Current:').grid(row=3, column=1)
        self.current_temp_min_label = ttk.Label(self, text='Min:').grid(row=3, column=2)
        self.current_temp_max_label = ttk.Label(self, text='Max:').grid(row=3, column=3)

        self.current_temp = ttk.Label(self, text=current_weather['temp']).grid(row=4, column=1)
        self.current_temp_min = ttk.Label(self, text=current_weather['min']).grid(row=4, column=2)
        self.current_temp_max = ttk.Label(self, text=current_weather['max']).grid(row=4, column=3)
        