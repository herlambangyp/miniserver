import socket
import questionary
from assets.script.config import loadSettings

SETTINGS = loadSettings()
def cekIp(port=8000):
    try:
        mainSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        mainSocket.connect(("8.8.8.8", 80))
        ip = mainSocket.getsockname()[0]
        mainSocket.close()
        return questionary.print(f"http://{ip}:{port}", style="fg:ansigreen bold underline", end="")
    
    except Exception:
        return questionary.print("ERROR: Gagal ekspose ke jaringan lokal. Apakah jaringan lokal mati?", style="fg:ansired bold")


def pesanCLI(dir='', port=8000, link="url"):
    questionary.print("> ",end="")
    questionary.print("By Herlambang YP", style="bold fg:ansicyan")
    questionary.print("Source-code: ",end="")
    questionary.print("https://github.com/herlambangyp/python/tree/main/miniServer", style="underline")
    questionary.print(f"(Ctrl + Klik Link)", style="bold")

    questionary.print(f"\n> Miniserver dijalankan di:")
    questionary.print(f"  {dir}", style="bold")

    questionary.print("\n> Server lokal aktif di:")
    questionary.print("  ",end="")                
    questionary.print(f"{link}", style="fg:ansigreen bold underline", end="")
    questionary.print(f" (Ctrl + Klik Link)", style="bold")

    questionary.print("\n> Link akses utk perangkat lain (di jaringan yg sama):")
    questionary.print("  ",end="")        
    cekIp(port)                
    questionary.print(" (Ctrl + Klik Link)", style="bold")
    questionary.print("  *Izinkan firewall agar bisa diakses perangkat lain" )
    questionary.print("  *Jika tetap tidak tampil di perangkat lain:" )
    questionary.print("    - Lakukan ping ke perangkat yg dituju melalui CMD" )
    questionary.print("    - Misalnya: ", end="" )
    questionary.print("ping ", style="fg:ansiyellow", end="")
    questionary.print("192.168.11.134 ", style="bold", end="")
    questionary.print("(ip perangkat lain yg dituju)")
    questionary.print("    - Jika ping berhasil, buka lagi website di perangkat yg dituju." )
    questionary.print("    - Tidak perlu melakukanya untuk semua perangkat" )
    questionary.print("    - 1 Perangkat terhubung, seharusnya bisa memicu pembaruan seluruh koneksi" )

    questionary.print("\n> ",end="")
    questionary.print("Info:", style="fg:ansicyan")
    questionary.print("  Tekan ",end="")
    questionary.print("Ctrl + C atau tutup terminal ini", style="bold fg:ansired", end="")
    questionary.print(" untuk mematikan server.")

    questionary.print("\n  Pengaturan Server:")
    questionary.print("  ",end="")                
    questionary.print(f"{link}/settings", style="fg:ansiyellow bold underline", end="")
    questionary.print(f" (Ctrl + Klik Link)", style="bold")

    questionary.print("\n  SERVER INI DIBUAT SANGAT SPESIFIK UNTUK ENVIRONMENT FRONT END LOKAL", style="bold")
    questionary.print("  Tanpa koneksi database, tanpa PHP, tanpa NodeJS (server-side).")
    questionary.print("  Arsitektur dibuat sangat spesifik meniru Github-Pages")
    questionary.print("  TIDAK untuk port forwarding (hosting server) ke publik! Baca source-code terkait hal ini", style="bold")

    questionary.print("\n> ",end="")
    questionary.print("Lalu lintas server:", style="fg:ansiyellow")
    if SETTINGS["access_log"]:
        questionary.print('\nIP yang request - - [Waktu request] "method dan yang di request" kode respon server\n')
    else:
        questionary.print('  Lalu lintas server dimatikan di pengaturan server', style='bold')
        
def pesanCLIEN(dir='', port=8000, link="url"):
    questionary.print("> ",end="")
    questionary.print("By Herlambang YP", style="bold fg:ansicyan")
    questionary.print("Source-code: ",end="")
    questionary.print("https://github.com/herlambangyp/python/tree/main/miniServer", style="underline")
    questionary.print(f"(Ctrl + Klik Link)", style="bold")

    questionary.print(f"\n> Miniserver working at:")
    questionary.print(f"  {dir}", style="bold")

    questionary.print("\n> local server running on:")
    questionary.print("  ",end="")                
    questionary.print(f"{link}", style="fg:ansigreen bold underline", end="")
    questionary.print(f" (Ctrl + Click Link)", style="bold")

    questionary.print("\n> Link for other device to access (same network):")
    questionary.print("  ",end="")        
    cekIp(port)                

    questionary.print(" (Ctrl + Click Link)", style="bold")
    questionary.print("  *Allow firewall access to connect from other devices.")
    questionary.print("  *If the server is still inaccessible from other devices:")
    questionary.print("    - Ping the target device using CMD.")
    questionary.print("    - For example: ", end="")
    questionary.print("ping ", style="fg:ansiyellow", end="")
    questionary.print("192.168.11.134 ", style="bold", end="")
    questionary.print("(target device's IP address)")
    questionary.print("    - If the ping succeeds, try opening the website again.")
    questionary.print("    - You only need to do this once, not for every device.")
    questionary.print("    - One successful connection should be enough to restore access for all devices.")

    questionary.print("\n> ",end="")
    questionary.print("Info:", style="fg:ansicyan")
    questionary.print("  Click ",end="")
    questionary.print("Ctrl + C or close this terminal", style="bold fg:ansired", end="")
    questionary.print(" to shutdown this server")

    questionary.print("\n  Server Settings:")
    questionary.print("  ",end="")                
    questionary.print(f"{link}/settings", style="fg:ansiyellow bold underline", end="")
    questionary.print(f" (Ctrl + Click Link)", style="bold")

    questionary.print("\n  THIS SERVER WAS BUILD SPECIFICALY FOR LOCAL FRONT-END ENVIRONMENT", style="bold")
    questionary.print("  Without database connection, no PHP, no NodeJS (server-side).")
    questionary.print("  The architecture specificaly build just like how github-pages works")
    questionary.print("  NOT RECOMENDED FOR port forwarding (hosting server) to public! Please read source-code for further information", style="bold")

    questionary.print("\n> ",end="")
    questionary.print("Server Traffic:", style="fg:ansiyellow")
    if SETTINGS["access_log"]:
        questionary.print(f'\nRequester IP - - [request time] "method and whats the request" server respond code\n')
    else:
        questionary.print('  Server traffic dissabled in server settings', style='bold')
        

