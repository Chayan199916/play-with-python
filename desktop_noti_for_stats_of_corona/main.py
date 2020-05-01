import win10toast

def notify_me(title, message):
    toaster = win10toast.ToastNotifier()
    toaster.show_toast(title, message, duration = 10)

if __name__ == "__main__":
    notify_me("Chayan", "Let's stop the spread of this virus together")