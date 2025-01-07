import os
import sys
from tqdm import tqdm
import re

def clear_screen():
    os.system('clear')

def display_red_ascii_art():
    clear_screen()
    
    ascii_art = r"""
  /$$$$$$                                         
 /$$__  $$                                        
| $$  \__/ /$$   /$$ /$$$$$$$  /$$   /$$ /$$   /$$
|  $$$$$$ | $$  | $$| $$__  $$| $$  | $$|  $$ /$$/
 \____  $$| $$  | $$| $$  \ $$| $$  | $$ \  $$$$/ 
 /$$  \ $$| $$  | $$| $$  | $$| $$  | $$  >$$  $$ 
|  $$$$$$/|  $$$$$$$| $$  | $$|  $$$$$$$ /$$/\  $$
 \______/  \____  $$|__/  |__/ \____  $$|__/  \__/
           /$$  | $$           /$$  | $$          
          |  $$$$$$/          |  $$$$$$/          
           \______/            \______/           
    """
    
    red_color = "\033[91m"
    reset_color = "\033[0m"
    
    sys.stdout.write(red_color + ascii_art + reset_color)
    sys.stdout.flush()

def display_header():
    gold_color = "\033[38;5;220m"
    telegram_color = "\033[38;5;33m"
    reset_color = "\033[0m"
    
    display_red_ascii_art()
    print("\n\nURL:LOG:PASS EXTRATOR")
    print(f"{gold_color}Owner: X{reset_color}")
    print(f"{telegram_color}Telegram: @larpador{reset_color}\n")

def clean_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

def search_keyword_in_files(keyword, folder_path):
    save_results = input("\nDeseja salvar os resultados? (Y/N): ").strip().upper()

    seen_lines = set()
    results = []

    try:
        file_list = [f for f in os.listdir(folder_path) if f.endswith(".txt")]
        total_files = len(file_list)

        if save_results == 'Y':
            cleaned_keyword = clean_filename(keyword)
            file_name = f"synyx_{cleaned_keyword}.txt"
            try:
                with open(file_name, 'w') as output_file:
                    for filename in tqdm(file_list, unit="arquivo", dynamic_ncols=True):
                        file_path = os.path.join(folder_path, filename)
                        
                        try:
                            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                                for line in file:
                                    stripped_line = line.strip()
                                    if keyword in stripped_line and stripped_line not in seen_lines:
                                        seen_lines.add(stripped_line)
                                        tqdm.write(f"{stripped_line}")
                                        output_file.write(stripped_line + "\n")
                        except Exception as e:
                            tqdm.write(f"Erro ao ler o arquivo {filename}: {e}")
            except Exception as e:
                tqdm.write(f"Erro ao abrir: {e}")
            tqdm.write(f"\nResultados salvos em {file_name}")
        else:
            for filename in tqdm(file_list, unit="arquivo", dynamic_ncols=True):
                file_path = os.path.join(folder_path, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                        for line in file:
                            stripped_line = line.strip()
                            if keyword in stripped_line and stripped_line not in seen_lines:
                                seen_lines.add(stripped_line)
                                tqdm.write(f"{stripped_line}")
                except Exception as e:
                    tqdm.write(f"Erro ao ler o arquivo {filename}: {e}")

    except Exception as e:
        tqdm.write(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    display_header()  
    
    folder_path = input("Caminho da pasta com os .txt: ").strip()
    if not os.path.exists(folder_path):
        print(f"Erro: O caminho '{folder_path}' não existe.")
        sys.exit(1)

    keyword = input("\nDigite a url: ")
    search_keyword_in_files(keyword, folder_path)
