from colorama import Fore, Style

def format_text(file_path):
    with open(file_path, 'r',encoding='utf-8') as file:
        lines = file.readlines()

    with open(file_path, 'w',encoding='utf-8') as file:
        for line in lines:
            title = line.strip()
            if  title.endswith('.'):
                file.write('\n')
                file.write(title)
                file.write('\n')
            elif title.startswith('*') and title.endswith('*'):
                colored_title = f"{Fore.GREEN}{Style.BRIGHT}{title}{Style.RESET_ALL}\n"
                file.write('\n')
                file.write(colored_title)
                colored_Stars = f"{Fore.CYAN}{Style.BRIGHT}{'*'*45}{Style.RESET_ALL}\n"
                file.write(colored_Stars)
                file.write('\n')
            else:
                file.write(title)
                


format_text('doc.txt')
