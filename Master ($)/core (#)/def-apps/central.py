import random
import os
import subprocess
from colorama import init, Fore, Back, Style
init()
print(Fore.GREEN + """
/==============================/
|                              |
| TomatOS v0.1                 |
| TomatOS served fresh!        |
|                              |
/==============================/""" + Style.RESET_ALL)

def handle_open_old_old(file_path: str, app: str = None):
  try:
    if os.name == 'nt':  # Windows
      if app:
        os.system(f'start "" "{app}" "{file_path}"')
      else:
        os.startfile(file_path)
    else:
      if app:
        subprocess.run([app, file_path])
      else:
        subprocess.run(['xdg-open', file_path])
      print(Fore.GREEN + f"✅ Abriendo '{file_path}'..." + Fore.RESET)
  except Exception as e:
    print(Fore.RED + f"Error: {e}" + Fore.RESET)

def handle_open_old(file_path: str, app: str):
  try:
    if os.name == 'nt':  # Windows
      subprocess.run(f'"{app}" "{file_path}"', shell=True)
    else:  # Linux/macOS
      subprocess.run([app, file_path])
    print(Fore.GREEN + f"✅ Abriendo '{file_path}' con {app}..." + Fore.RESET)
  except Exception as e:
    print(Fore.RED + f"Error al abrir: {e}" + Fore.RESET)

def handle_open(file_path: str, app: str):
  try:
    if not os.path.isabs(file_path):
      raise ValueError("Use absolute routes! e.g: 'C:/folder/file.txt' or '/home/user/file.txt'")
    
    if not os.path.exists(file_path):
      raise FileNotFoundError(f"The file '{file_path}' does not exist")
        
    if os.name == 'nt':  # Windows
      subprocess.run(f'"{app}" "{file_path}"', shell=True)
    else:  # Linux/macOS
      subprocess.run([app, file_path])
        
    print(Fore.GREEN + f"[v] Opened: '{file_path}' with {app}" + Fore.RESET)
    
  except Exception as e:
    print(Fore.RED + f"Error: {e}" + Fore.RESET)

def handle_exe(program: str):
    try:
        subprocess.Popen(program, shell=True)
        print(Fore.GREEN + f"Executing'{program}'..." + Fore.RESET)
    except Exception as e:
        print(Fore.RED + f"Error: {e}" + Fore.RESET)

while True:
  current_path = "" or "$>#"

  cmds_help = {
    "del": "Deletes a file / directory",
    "open": "Opens a file (Does not support .exe, .bat or any executable files)",
    "exe": "Executes a program.",
    "conv": "Converts a TomatOS directory into another's OS's directory (Windows, Linux, Mac OS)",
    "facts": "Shows a random fact",
    "chdir": "Changes the current directory",
    "make": "Creates a file / directory",
    "simcrash": "Displays a fake death screen."
  }
  
  cmds_howto = {
    "delete": "use 'del' + directory (include file name and extension if working with files)",
    "create": "use 'make' + direcotry (include file name and extension if working with files)",
}
  
  cmd = input(Fore.GREEN + f"TomatOS>User {current_path}: " + Style.RESET_ALL).lower()
  
  cmds = ["conv", "wconv", "lconv", "iConv", "facts", "make", "open", "conv_m", "mconv",
   "del", "chdir", "howto", "simcrash"]
  
  how_to = ["delete", "change_directory", "delete_directory", "delete_file", ""]
  
  facts = ["OS fact #1: Did you know that the name TomatOS is a Reference to Wheatly calling GLaDOS 'PotatOS' in Portal 2?",
    "OS fact #2: TomatOS is the first OS to be approved by the best italian chefs",
    "Dev fact #1: Did you know that Torvalds got into programming at age 11? It's never too soon to begin!",
    'Tomato fact #1: Did you know that the tomato plant is called "Solanum lycopersicum"?',
    'Tomato fact #2: Did you know that Tomatoes contain potassium, iron and vitamins A, B1, B2, B5 and C? They\'re not just the coolest fruit- they\'re one of the healthiest!',
    "OS fact #3: Did you know that Linux's pet penguin actually has a name? It's Tux!"  
  ] 
  
  others = ["sudo make me a sandwich", "linux is better","tux isbetter","rm -rf /", "i want ice cream" ,"exit"]
  
  others_2 = ["Here's you tomato sandwich (made with extra tomatOS)", 
  "Yeah, but that little penguin can't make you TomatOS sauce and silly jokes, can it? (ERROR: 404_NOTUX)",
  "You can't make sauce with your system because there are no penguins here. Only tomatOS.",
  "I don't think there's tomato ice cream yet :("]
  
  fact_to_show = random.choice(facts)
  
  messages = {5: "That does not count as a Tomato... Nor as a valid input...", 4: "These tomatOS are for the spaghetti tomato sauce only!"}
  
  def conv(path: str, target: str):
    parts = path.split(">")
    if target == "windows":
      core = parts[1] = "Users\\(username)"
      if parts[0] == "$":
        drive = "C:"
      elif parts[0] == "0":
        dirve = "D:"
      elif parts[0] == "1":
        drive = "E:"
      elif parts[0] == "2":
        drive: "F:"
      else:
        drive = "(IDK, why do you have so many drives dude?):"
      print(f"{drive}\\{'\\'.join(parts[1:])}")
    elif target == "linux":
      print(f"/{'/'.join(parts).replace("$", "root").replace("#", "core")}")
    elif target == "macos":
      print(f"")
    else:
      print("That doesn't count as a tomato... Nor does it count as a valid input... Select a supported OS: \nWindows\nLinux\nMac OS")
  
  if cmd == "conv":
    targ_imp = input("Enter OS to translate (windows, Linux, Mac OS)").lower().strip()
    path_input = input("Enter Path to transalte:").lower()
    conv(path_input, targ_imp) 
  elif cmd == "facts":
    print(Fore.CYAN + Back.WHITE + fact_to_show + Style.RESET_ALL)
  elif cmd == others[3]:
    print(Fore.MAGENTA + others_2[2] + Fore.RESET)
  elif cmd == others[1] or cmd == others[2]:
    print(Fore.MAGENTA + others_2[1] + Fore.RESET)
  elif cmd == others[0]:
    print(Fore.MAGENTA + others_2[0] + Fore.RESET)
  elif cmd == others[3]:
    print(Fore.MAGENTA + others_2[2] + Fore.RESET)
  elif cmd == others[4]:
    print(Fore.MAGENTA + others_2[3] + Fore.RESET)
  elif cmd == "exit":
    print("Byeeeeeeeeee!")
    break #150 líneas menos para el lanzamiento oficial 🍅🥳🎉
  elif cmd == "simcrash":
    print("""
  x_x
  Your TomatOS got rotten!
    Your PC has ran into a problem, we're trying to fix it :3.""")
  elif cmd == "gh":
    print(f"""comands: 
    {cmds}""")
  elif cmd.startswith("help"):
    try:
      command = cmd.split(" ")[1]
      print(cmds_help.get(command, "Comnand not found."))
    except IndexError:
      print("Uso: help <comando>. Comandos disponibles:", list(cmds_help.keys()))
  elif cmd.startswith("open"):
    try:
      parts = cmd[len("open"):].strip().split("**", 1)
      if len(parts) != 2:
        raise ValueError("Formato incorrecto")
      file_part = parts[0].strip()
      if not file_part.startswith("*"):
        raise ValueError("Falta '*' antes del archivo")
      file_path = file_part[1:].strip() 
      app = parts[1].strip()
      handle_open(file_path, app)
    except Exception as e:
      print(Fore.RED + f"Error: {e}. Formato correcto: open *archivo **app" + Fore.RESET)
  elif cmd.startswith("exe"):
    program = cmd.split(" ", 1)[1]
    handle_exe(program)