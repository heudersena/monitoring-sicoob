# https://youtu.be/3hqPaonE7wM
#  pyinstaller --onefile -w main.py

import PySimpleGUI as sg
import src.read as read
import src.database as database
from datetime import datetime
import src.log as log
sg.theme("SandyBeach")



colonyList = []

# iniciar dados
DB = read.readDB()
Query = read.readQuery();

layout = [
    [sg.Text('Servidor: ',size=(6,0)), sg.Input(size=(15,0), key="server_name")],
    [sg.Text('Usuário: ',size=(6,0)), sg.Input(size=(15,0), key="user_name")],
    [sg.Text("PROCEDURE/QUERY")],
    [sg.Radio('PROCEDURE', "PROCEDURE/QUERY",key="PROCEDURE"), sg.Radio('QUERY', "PROCEDURE/QUERY",key="QUERY")],
    [sg.Text("Execute a QUERY",size=(15,0))],
    [sg.Combo(Query,size=(30,10), key="query")],
    [sg.Text("Escolha a base de dados",size=(15,0))],
    [sg.Combo(DB,size=(30,10), key="db")],
    [sg.Text("Executar em todas base de dados?")],
    [sg.Radio('SIM', "aceita",key="positivo"), sg.Radio('NAO', "aceita",key="negativo")],
    [sg.B("ENVIAR DADOS", mouseover_colors="red")],
    [sg.Listbox(values=colonyList,size=(500,10),key="ListBoxValues", background_color="white")]
]

window = sg.Window("MONITORAÇÃO", size=(500,510)).layout(layout)



while True:
      event, values = window.read()    
 
      if values["query"] == '' :    
        sg.popup_error('O CAMPO DE QUERY ESTÁ VAZIO!', auto_close=0.1)  
      else:
        if values['negativo'] == True:
            if values["db"] != '':
                response = database.connection(values["server_name"],values["db"]).execute(values['query'])
                colonyList.clear()
                for row in response:
                    n = []
                    n.append(row)
                    n.append(datetime.today())
                    log.write_log(" ".join(str(n)))
                    
                    colonyList.append(row.name)
                    window.find_element('ListBoxValues').update(colonyList)
                response.close()
            else:
                sg.popup_error('O CAMPO DB ESTÁ VAZIO!', auto_close=0.1) 
        else:
            colonyList.clear()

            for DBName in DB:
                response = database.connection(values["server_name"],DBName).execute(values['query'])
                for row in response:
                        colonyList.append({row.id, row.name})
                        window.find_element('ListBoxValues').update(colonyList)
                                              
                        n = []
                        n.append(row)
                        n.append(datetime.today())
                        log.write_log(" ".join(str(n)))

                        inputNewName = "WASP7852"+datetime.today().strftime('%d/%m/%Y')
                        execRow = database.connection(values["server_name"],DBName).execute("UPDATE peplo SET name=?",str(inputNewName) )
                        execRow.commit()   

                response.close()
            print("bay")

        if event == sg.WIN_CLOSED:
            break

window.close()