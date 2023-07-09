from sys import argv


if len(argv) < 2:
    print("Should have at least 1 arguments")
    exit()

script_args = {
    "--load-urls": "load_urls.main",
    "--enter-data": "enter_data.main",
    "--find-emails": "find_emails.main",
    "--send-email": "send_emails.main"
}

arg = argv[1]
if arg not in script_args:
    print("Argument must be one of the following: ")
    print(script_args.keys())
    exit()

script_to_execute = script_args[arg]

try:
    module = __import__(script_to_execute, fromlist=["main"])
    module.main()
except ModuleNotFoundError:
    print("Can't find module")
