import requests
from tkinter import *

countries_url = "https://covid19.mathdro.id/api/countries"
res1 =requests.get(countries_url)
countries= res1.json()
countries_list = []
list_code = []
we=countries['countries']
for i in we:
    countries_list.append(i['name'])
    if i.get('iso3') is None:
        pass
    else:
        list_code.append(i.get('iso3'))

print(countries_list)

url = "https://covid19.mathdro.id/api/countries/IND/confirmed"
res = requests.get(url)
output = res.json()
lists=[]
for states in output:
    if states['provinceState'] is None:
        lists.append("No states are there")
        break

    lists.append(states['provinceState'])

def Covid():


    TEXT = city1_listbox.get()
    url2 = "https://covid19.mathdro.id/api/countries/{}/confirmed".format(TEXT)
    res2 = requests.get(url2)
    output = res2.json()
    if output[0]['provinceState'] is None:
        cases_in_state = output[0]['confirmed']
        Active_cases_in_state = output[0]['active']
        Recovered_in_state = output[0]['recovered']
        deaths_in_state = output[0]['deaths']
        nameOfState = output[0]['countryRegion']
        cases_in_India_label.configure(text="Confirmed cases " + ": " +str(cases_in_state))
        active_label.configure(text="Active cases : " + str(Active_cases_in_state))
        deaths_label.configure(text="Recovered      : " + str(Recovered_in_state))
        recovered_label.configure(text="Deaths   : " + str(deaths_in_state))
        Name_label.configure(text="Country   : " + str(nameOfState))

    else:
        state = city_name_list.index(city_listbox.get())
        nameOfState = output[state]['provinceState']
        cases_in_state = output[state]['confirmed']
        Active_cases_in_state = output[state]['active']
        Recovered_in_state = output[state]['recovered']
        deaths_in_state = output[state]['deaths']

        Name_label.configure(text="State    : " + str(nameOfState))
        cases_in_India_label.configure(text="Confirmed cases in " + str(output[state]['provinceState']) + ": " + str(cases_in_state))
        active_label.configure(text="Active cases : " + str(Active_cases_in_state))
        deaths_label.configure(text="Recovered     : " + str(Recovered_in_state))
        recovered_label.configure(text="Deaths     : " + str(deaths_in_state))



def change(event):
    TEXT=city1_listbox.get()
    url2="https://covid19.mathdro.id/api/countries/{}/confirmed".format(TEXT)
    res2 = requests.get(url2)
    output2=res2.json()
    lists.clear()

    for states in output2:
        if states['provinceState'] is None:
            lists.append("No states are there")
            break
        lists.append(states['provinceState'])
        print(lists)
    option = OptionMenu(window, city_listbox, *lists)
    option.grid(row=3, column=5, padx=150, pady=10)



window =Tk()
window.title("Covid-19 Current situation")
window.geometry("450x420+400+200")
window.configure(bg='red')


countries_code_list = list_code
city1_listbox = StringVar(window)
city1_listbox.set("Select Countries")
option1 = OptionMenu(window,city1_listbox,*list_code)
option1.grid(row=1,column =5,padx = 150,pady =10 ,columnspan=3)

city_name_list =lists
city_listbox = StringVar(window)
city_listbox.set("Select the City")


b2 = Button(window,text ="ok", width =15)
b2.grid(row= 2, column =5, padx = 150)
b2.bind('<Button-1>', change)

b1 = Button(window, text ="Submit", width =15, command =Covid)
b1.grid(row= 5, column =5, padx = 150, pady=10)
b1.configure(bg='lightblue')

cases_in_India_label = Label(window,font=("times", 15, "bold"))
cases_in_India_label.grid(row=10, column=5)

recovered_label = Label(window,font=("times", 15, "bold"))
recovered_label.grid(row=13, column=5)

active_label = Label(window, font=("times", 15, "bold"))
active_label.grid(row=14, column=5)

deaths_label = Label(window,font=("times", 15, "bold"))
deaths_label.grid(row=16, column=5)

Name_label = Label(window,font=("times", 15, "bold"))
Name_label.grid(row=18, column=5)

window.mainloop()
