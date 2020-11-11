#===========================
# Imports
#===========================

import tkinter as tk
from tkinter import ttk,  Menu, colorchooser as cc, Spinbox as sb, scrolledtext as st, messagebox as mb, filedialog as fd

from datetime import date, datetime

class Events:
    # ------------------------------------------
    # Initializer
    #------------------------------------------
    def __init__(self):
        self.list_events = []

    def get_events(self, filename):
        with open('events.txt') as file:
            for line in file:
                line = line.rstrip('\n')
                current_event = line.split(',')

                event_date = datetime.strptime(current_event[1], r'%d/%m/%y').date()
                current_event[1] = event_date

                self.list_events.append(current_event)
            return self.list_events

    def days_between_dates(self, date1, date2):
        time_between = str(date1 - date2)
        number_of_days = time_between.split(' ') # :'27', 'days', '0:00:00'
        return number_of_days[0]

# #===========================
# # Main App
# #===========================

class App(tk.Tk):
    """Main Application."""

    #------------------------------------------
    # Initializer
    #------------------------------------------
    def __init__(self):
        super().__init__()
        self.init_config()
        self.init_vars()
        self.init_widgets()

    #------------------------------------------
    # Instance Attributes
    #------------------------------------------
    def init_vars(self):
        self.events_list = Events()
        self.events = self.events_list.get_events('events.txt')
        self.today = date.today()
        self.vertical_space = 100

    #-------------------------------------------
    # Window Settings
    #-------------------------------------------
    def init_config(self):
        self.resizable(False, False)
        self.geometry('500x500+0+0')
        self.title('Countdown Calendar Version 1.0')
        self.iconbitmap('python.ico')
        self.style = ttk.Style(self)
        self.style.theme_use('clam')

    #-------------------------------------------
    # Widgets / Components
    #-------------------------------------------
    def init_widgets(self):
        frame = self.create_frame(self,
            side=tk.TOP, fill=tk.BOTH, expand=True)

        self.canvas = self.create_canvas(frame, '#000',
            side=tk.TOP, fill=tk.BOTH, expand=True)

        self.canvas.create_text(50, 50,
            anchor=tk.W, fill='orange', font='Arial 20 bold', text='Countdown Calendar')

        self.events.sort(key=lambda x: x[1])
        for event in self.events:
            event_name = event[0]
            days_until = self.events_list.days_between_dates(event[1], self.today)

            display = f'It is {days_until} days until {event_name}'

            if (int(days_until) <= 7):
                text_color = 'red'
            else:
                text_color = 'lightblue'

            self.canvas.create_text(50, self.vertical_space,
                anchor=tk.W, fill=text_color, font='Arial 15 bold', text=display)

            self.vertical_space += 30

    # INSTANCE ---------------------------------
    def create_canvas(self, parent, color, **kwargs):
        canvas = tk.Canvas(parent, bg=color)
        canvas.pack(**kwargs)
        return canvas

    def create_frame(self, parent, **kwargs):
        frame = ttk.Frame(parent)
        frame.pack(**kwargs)
        return frame

# #===========================
# # Start GUI
# #===========================

def main():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()