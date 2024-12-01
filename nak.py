from tkinter import *
from tkinter import ttk
def conversion_window():

    #Window Screen
    root= Tk()
    root.title('Meter Converter')
    root.geometry('600x400')
    # root.rowconfigure([0,1,2,3], weight=1)
    # root.columnconfigure([0,1], weight=1)
    

    #Entry
    entry_label = Label(root, text='Measurement (in meters): ')
    entry_label.pack(pady=10)
    entry = Entry(root, width=15)
    entry.pack()

    #ComboBox Coversion To
    conversion = ['km', 'hm', 'dcm', 'm', 'dm', 'cm', 'mm']
    conversion_list = ttk.Combobox(root, values=conversion, width=5)
    conversion_list.pack()
    conversion_list.set('m') 
        
     #Conversion Function
    def convert_meter():
        conversions= {
            'km' : 1000,
            'hm' : 100,
            'dcm' : 10,
            'm' : 1,
            'dm' : 0.1,
            'cm' : 0.01,
            'mm' : 0.001}
        try:
            user_input = float(entry.get())
            units = conversion_list.get()
            if units in conversions:
                result = user_input / conversions[units]
                result_label.config(text=f'Result: {result:.2f} {units.capitalize()}')
            else: result_label.config(text='Invalid Input!')
        except ValueError:
            result_label.config(text='Please enter a numeric value!')
    #Result
    result_label = Label(root, text='', fg= 'white', anchor='center')
    result_label.pack()
    
    #Convert Button
    convert_btn = Button(root, text='Convert', command=convert_meter)
    convert_btn.pack()
    
    root.mainloop()
def main()-> None:
    conversion_window()
if __name__ == '__main__':
    main()