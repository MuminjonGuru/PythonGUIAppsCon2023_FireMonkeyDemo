from delphifmx import *
from uMain import FormMain

def main():
    Application.Initialize()
    Application.Title = 'NASA_API_Demo'
    Application.MainForm = FormMain(Application)
    Application.MainForm.Show()
    Application.Run()
    Application.MainForm.Destroy()

if __name__ == '__main__':
    main()
