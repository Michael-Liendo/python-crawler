from sys import argv

if len(argv) < 2:
    print("Debe proporcionar un argumento válido.")
    exit()

script_args = {
    "--enter-data": "enter_data.main",
    "--find-emails": "find_emails.main",
    "--load-urls": "load_urls.main"
}

arg = argv[1]
if arg not in script_args:
    print("El argumento proporcionado no es válido.")
    exit()

script_to_execute = script_args[arg]

try:
    module = __import__(script_to_execute, fromlist=["main"])
    module.main()
except ModuleNotFoundError:
    print("El archivo especificado no existe o no puede ser importado.")
