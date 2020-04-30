import tkinter as tk
import webbrowser

root = tk.Tk()
root.geometry('500x500')

root.title('Automate 3 Tasks')

urls = ['https://github.com/Anu2006',
        'https://youtube.com',
        'https://twitter.com/home']

msgs = ['github', 'youtube', 'twitter']
positions = (120, 160, 200)

def open_url(url):
    return lambda: webbrowser.open_new(url)


frame = tk.Frame(root, bg='#7e3ba8')
frame.place(relx = 0.1, rely= 0.1, relwidth = 0.8,
            relheight = 0.8)

label = tk.Label(root, text='welcome', relief='solid',
                 width=20, font=('arial', 19, 'bold'))
label.place(x=90, y=53)

for url, text, y in zip(urls, msgs, positions):
    tk.Button(root, text=f'go to {text}', width=12, bg='#655fe7',
                        command=open_url(url)).place(x=200, y=y)

root.mainloop()
