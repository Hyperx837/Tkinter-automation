import tkinter as tk
import webbrowser
import getpass



def add_to_startup():
    file_path = os.path.dirname(os.path.realpath(__file__))

    bat_path = 'C:/Users/%s/AppData/Roaming/Microsoft/ \
                Windows/Start Menu/Programs/Startup/open.bat' % USER_NAME

    with open(bat_path, "w") as bat_file:
        bat_file.write(r'start "" %s' % file_path)

root = tk.Tk()
USER_NAME = getpass.getuser()

add_to_startup()


root.geometry('500x500')
root.title('Automate 3 Tasks')

urls = ['https://github.com/Anu2006',
        'https://youtube.com',
        'https://twitter.com/home']

msgs = ['github', 'youtube', 'twitter']
positions = [(i, 200) for i in (120, 160, 200)]

def open_url(url):
    return lambda: webbrowser.open_new(url)


frame = tk.Frame(root, bg='#7e3ba8')
frame.place(relx = 0.1, rely= 0.1, relwidth = 0.8,
            relheight = 0.8)

label = tk.Label(root, text='welcome', relief='solid',
                 width=20, font=('arial', 19, 'bold'))
label.place(x=90, y=53)

for url, text, pos in zip(urls, msgs, positions):
    tk.Button(root, text=f'go to {text}', width=12, bg='#655fe7',
                        command=open_url(url)).place(x=pos[1], y=pos[0])

root.mainloop()
