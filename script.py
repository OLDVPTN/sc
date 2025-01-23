import sys

def show_apps():
    # Daftar aplikasi dan package names yang sering dipakai cewek (ilusi saja)
    apps = [
        {"name": "Instagram", "package": "com.instagram.android"},
        {"name": "Facebook", "package": "com.facebook.katana"},
        {"name": "Getcontact", "package": "app.source.getcontact"},
        {"name": "TikTok", "package": "com.ss.android.ugc.trill"},
        {"name": "Pinterest", "package": "com.pinterest"},
        {"name": "Spotify", "package": "com.spotify.music"},
        {"name": "Shopee", "package": "com.shopee.app"},
        {"name": "DANA", "package": "id.dana"},
        {"name": "TeraBox", "package": "com.dubox.drive"},
        {"name": "WhatsApp", "package": "com.whatsapp"},
        {"name": "YouTube", "package": "com.google.android.youtube"},
        {"name": "Netflix", "package": "com.netflix.mediaclient"},
        {"name": "Telegram", "package": "org.telegram.messenger"},
        {"name": "LINE", "package": "jp.naver.line.android"},
        {"name": "X", "package": "com.twitter.android"},
        {"name": "Discord", "package": "com.discord"},
        {"name": "Google Maps", "package": "com.google.android.apps.maps"},
        {"name": "MyTelkomsel", "package": "com.telkomsel.telkomselcm"},
        {"name": "Gojek", "package": "com.gojek.app"},
        {"name": "Messenger", "package": "com.facebook.orca"},
        {"name": "Grab", "package": "com.grabtaxi.passenger"},
        {"name": "BCA mobile", "package": "com.bca"},
        {"name": "Duolingo", "package": "com.duolingo"},
        {"name": "Mobile Legends", "package": "com.mobile.legends"},
        {"name": "Cuaca", "package": "com.vivo.weather"},
        {"name": "Cuaca", "package": "com.kcstream.kucing"}
    ]

    print("Aplikasi terinstall:")
    for i, app in enumerate(apps, 1):
        print(f"{i}. {app['name']} ({app['package']})")

    return apps

def select_app(apps, index):
    try:
        selected_app = apps[index - 1]
        print(f"Terpilih: {selected_app['name']} ({selected_app['package']})")
    except IndexError:
        print("Invalid selection. Please choose a valid number.")

def main():
    print("Menunggu target...")
    print("Target membuka aplikasi...")
    print("Terhubung dengan target!")

    apps = []

    while True:
        command = input("Enter command: ").strip()

        if command.lower() == "listapk 1":
            apps = show_apps()
        elif command.lower().startswith("pkgname"):
        elif command.lower() == "getfile -d /storage/emulated/DCIM":
            print("Sukses!\nCamera: 340 item\ncaptured_media: 0 item\nFacebook: 72 item\nScreenshots: 680 item")
            if apps:
                try:
                    _, index = command.split()
                    index = int(index)
                    select_app(apps, index)
                except ValueError:
                    print("Invalid command format. Use 'pkgname <number>'.")
                except IndexError:
                    print("Invalid selection. Please choose a valid number from the list.")
            else:
                print("No apps loaded. Use 'listapk' first.")
        elif command.lower() == "exit":
            print("Goodbye!")
            break
        else:
            print("Unknown command. Try 'listapk', 'pkgname <number>', or 'exit'.")

if __name__ == "__main__":
    main()
