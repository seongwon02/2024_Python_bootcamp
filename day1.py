from tkinter import *
from tkinter.filedialog import *

# 숙제
def new_file():
    text_area.delete("1.0", "end")

def save_file():
    files = [('All Files', '*.*'),  
             ('Python Files', '*.py'), 
             ('Text Document', '*.txt')] 
    f = asksaveasfile(filetypes = files, defaultextension = files) 

def maker():
    info = Tk()
    info.title = "infomation"
    info.geometry("500x100+100+100")
    info.resizable(False, False)
    label = Label(info, text="만든이: 김성원")
    label.pack()
    info.mainloop()
    
window = Tk(className='메모장')  #가장 상위레벨의 윈도우 창 생성
window.title = "Notepad"

window.iconbitmap("img/notepad-icon_34386.ico")

# png 파일 가져오기
# photo = PhotoImage()
# window.iconphoto(False, photo)


# 메뉴 만들기
menuMaker = Menu(window)

first_menu = Menu(menuMaker, tearoff=0)

first_menu.add_command(label='새 파일', command=new_file)
first_menu.add_command(label='저장', command=save_file)
first_menu.add_separator()  # 구분선 추가
first_menu.add_command(label="종료", command=window.destroy)

menuMaker.add_cascade(label='파일', menu = first_menu)
# 메뉴 구성
window.config(menu = menuMaker)

second_menu = Menu(menuMaker, tearoff=0)
second_menu.add_command(label='만든 이', command=maker)
menuMaker.add_cascade(label='정보', menu = second_menu)




# 텍스트 창 생성
text_area = Text(window)

# 공백 설정
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# 텍스트 화면을 동서남북으로 붙이기
text_area.grid(sticky=N+E+S+W)

window.geometry("400x400+800+300")
window.resizable(True, True)

window.mainloop()  # 윈도우 종료까지 실행

