

# data_log_now = datetime.today().strftime('%d/%m/%Y')

def write_log(text):
    with open("log", "a", encoding="UTF-8") as file:
        file.write(text+"\n")