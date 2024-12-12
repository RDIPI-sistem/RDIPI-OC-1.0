import tkinter as tk
import time

def запуск_приложения():
    # Создание окна
    окно = tk.Tk()
    окно.title("Мое оконное приложение")
    окно.geometry("400x300")

    # Создание виджетов
    label = tk.Label(окно, text="Добро пожаловать в мое оконное приложение!")
    label.pack()

    button = tk.Button(окно, text="Кнопка", command=lambda: print("Кнопка нажата!"))
    button.pack()

    # Запуск приложения
    окно.mainloop()

def main():
    print(" RDIPI. All rights reserved")
    print("Version: 1.0")
    print("Viruses: not found")
    print("Starting OS system. Please wait...")
    time.sleep(9)  # задержка на 9 секунд
    print("OS system started. You can use the following commands:")
    print("  help - displays a list of commands")
    print("  exit - exits the OS system")
    print("  uninstall - uninstalls the OS system")
    print("  restart - restarts the OS system")
    print("  shutdown - shuts down the OS system")
    print("  update - updates the OS system")
    print("  info - displays information about the OS system")
    print("  apps - displays a list of installed applications")
    print("  install - installs a new application")
    print("  uninstall_app - uninstalls an application")
    while True:
        console = input('Enter a command: ')
        if console.lower() == 'help':
            print("List of commands:")
            print("  help - displays a list of commands")
            print("  exit - exits the OS system")
            print("  uninstall - uninstalls the OS system")
            print("  restart - restarts the OS system")
            print("  shutdown - shuts down the OS system")
            print("  update - updates the OS system")
            print("  info - displays information about the OS system")
            print("  apps - displays a list of installed applications")
            print("  install - installs a new application")
            print("  uninstall_app - uninstalls an application")
        elif console.lower() == 'exit':
            print("Exiting the OS system...")
            break
        elif console.lower() == 'uninstall':
            print("Are you sure you want to uninstall the OS system? (yes/no)")
            confirm = input('Enter your answer: ')
            if confirm.lower() == 'yes':
                print("Uninstalling the OS system...")
                time.sleep(5)
                print("OS system uninstalled.")
                break
            else:
                print("Uninstallation cancelled.")
        elif console.lower() == 'restart':
            print("Restarting the OS system...")
            time.sleep(5)
            print("OS system restarted.")
        elif console.lower() == 'shutdown':
            print("Shutting down the OS system...")
            time.sleep(5)
            print("OS system shut down.")
            break
        elif console.lower() == 'update':
            print("Updating the OS system...")
            time.sleep(5)
            print("OS system updated.")
        elif console.lower() == 'info':
            print("Information about the OS system:")
            print("  Version: 1.0")
            print("  Release date: 2022-01-01")
            print("  Developer: RDIPI")
        elif console.lower() == 'apps':
            print("List of installed applications:")
            print("  Application 1")
            print("  Application 2")
            print("  Application 3")
        elif console.lower() == 'install':
            print("Enter the name of the application to install:")
            app_name = input('Enter the application name: ')
            print("Installing the application...")
            time.sleep(5)
            print("Application installed.")
        elif console.lower() == 'uninstall_app':
            print("Enter the name of the application to uninstall:")
            app_name = input('Enter the application name: ')
            print("Uninstalling the application...")
            time.sleep(5)
            print("Application uninstalled.")
        else:
            print("Unknown command. Type 'help' to display a list of commands.")

if __name__ == "__main__":
    main()
