import tkinter as tk
from tkinter import ttk, scrolledtext
import time
import os
import threading
from datetime import datetime

    # --- Configuração do Logging ---
LOG_DIRECTORY = r"C:\Logs\monitoramento_alertas"

def setup_logging():
    try:
        os.makedirs(LOG_DIRECTORY, exist_ok=True)
    except OSError as e:
    # Lida com possíveis erros de permissão ou outros problemas
        print(f"Erro ao criar o diretório de log: {e}")
        return False
    return True

class DeploymentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Implantação de Aplicação")
        self.root.geometry("700x550")
        
        # --- Estilo ---
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TButton", padding=6, relief="flat", background="#0078D7", foreground="white")
        style.map("TButton", background=[('active', '#005a9e')])
        style.configure("TFrame", background="#f0f0f0")
        style.configure("TLabel", background="#f0f0f0")
        style.configure("Header.TLabel", font=("Helvetica", 14, "bold"))

    # --- Frame Principal ---
        main_frame = ttk.Frame(root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

    # --- Seção de Inputs ---
        input_frame = ttk.Frame(main_frame, padding="10")
        input_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(input_frame, text="Nome da Aplicação:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.app_name_entry = ttk.Entry(input_frame, width=40)
        self.app_name_entry.grid(row=0, column=1, sticky=tk.EW, padx=5, pady=5)
        self.app_name_entry.insert(0, "Minha Aplicação Web")

        ttk.Label(input_frame, text="URL do Repositório:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.repo_url_entry = ttk.Entry(input_frame, width=40)
        self.repo_url_entry.grid(row=1, column=1, sticky=tk.EW, padx=5, pady=5)
        self.repo_url_entry.insert(0, "https://github.com/simulado/app.git")

        ttk.Label(input_frame, text="Nome do Serviço:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.service_name_entry = ttk.Entry(input_frame, width=40)
        self.service_name_entry.grid(row=2, column=1, sticky=tk.EW, padx=5, pady=5)
        self.service_name_entry.insert(0, "simulated_service")
        
        input_frame.columnconfigure(1, weight=1)

    # --- Botão de Implantação ---
        self.deploy_button = ttk.Button(main_frame, text="Iniciar Implantação", command=self.start_deployment_thread)
        self.deploy_button.pack(pady=10, fill=tk.X)

    # --- Seção de Logs ---
        log_frame = ttk.Frame(main_frame)
        log_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        ttk.Label(log_frame, text="Logs da Implantação:", style="Header.TLabel").pack(anchor="w", pady=(0, 5))
        
        self.log_area = scrolledtext.ScrolledText(log_frame, wrap=tk.WORD, height=15, font=("Courier New", 9))
        self.log_area.pack(fill=tk.BOTH, expand=True)
        self.log_area.config(state='disabled')

        self.log_file_path = None

    def log_step(self, message):
        timestamp = time.strftime('%H:%M:%S')
        log_message = f"[{timestamp}] {message}\n"

    # Atualiza a área de texto da GUI
        self.log_area.config(state='normal')
        self.log_area.insert(tk.END, log_message)
        self.log_area.see(tk.END) # Auto-scroll
        self.log_area.config(state='disabled')
        
    # Salva no arquivo de log
        if self.log_file_path:
            with open(self.log_file_path, 'a', encoding='utf-8') as f:
                f.write(log_message)
        
        self.root.update_idletasks() # Garante que a GUI seja atualizada
        time.sleep(1) # Simula algum tempo de processamento

    def deploy_application(self, app_name, repo_url, service_name):
        timestamp_file = datetime.now().strftime("%d%m%Y_%H%M%S")
        self.log_file_path = os.path.join(LOG_DIRECTORY, f"{app_name}_{timestamp_file}.log")

        self.log_step(f"--- Iniciando Implantação para: {app_name} ---")
        self.log_step(f"URL do Repositório: {repo_url}")
        self.log_step(f"Serviço Associado: {service_name}")
        self.log_step(f"Logs sendo salvos em: {self.log_file_path}")

        try:
     # 1. Parar o Serviço
            self.log_step(f"1. Parando o serviço '{service_name}'...")
            self.log_step(f"   Serviço '{service_name}' parado com sucesso (simulado).")

    # 2. Puxar a Versão Mais Recente do Código
            self.log_step("2. Puxando a versão mais recente do código...")
            current_version = "v1.0.0"
            new_version = "v1.1.0"
            self.log_step(f"   Código puxado com sucesso. Versão anterior: {current_version}, Nova versão: {new_version} (simulado).")

    # 3. Instalar Dependências
            self.log_step("3. Instalando dependências...")
            dependencies = ["biblioteca_a", "biblioteca_b", "modulo_x"]
            self.log_step(f"   Dependências instaladas: {', '.join(dependencies)} (simulado).")

    # 4. Rodar Migrações de Banco de Dados
            self.log_step("4. Executando migrações de banco de dados (se aplicável)...")
            self.log_step("   Migrações executadas com sucesso (simulado).")

    # 5. Reiniciar o Serviço
            self.log_step(f"5. Reiniciando o serviço '{service_name}'...")
            self.log_step(f"   Serviço '{service_name}' reiniciado com sucesso (simulado).")

            self.log_step(f"--- Implantação para '{app_name}' Concluída com Sucesso! ---")

        except Exception as e:
            self.log_step(f"!!! ERRO DURANTE A IMPLANTAÇÃO: {e} !!!")
        finally:
            self.deploy_button.config(state='normal')
            self.log_file_path = None # Reseta o caminho do arquivo

    def start_deployment_thread(self):
        if not setup_logging():
            self.log_step("ERRO: Não foi possível configurar o diretório de logs. Abortando.")
            return
            
    # Limpa a área de log para a nova implantação
        self.log_area.config(state='normal')
        self.log_area.delete('1.0', tk.END)
        self.log_area.config(state='disabled')
        
    # Desabilita o botão para evitar múltiplas implantações simultâneas
        self.deploy_button.config(state='disabled')

    # Pega os valores dos campos de entrada
        app_name = self.app_name_entry.get() or "AppSemNome"
        repo_url = self.repo_url_entry.get()
        service_name = self.service_name_entry.get()

    # Cria e inicia a thread
        deployment_thread = threading.Thread(
            target=self.deploy_application,
            args=(app_name, repo_url, service_name),
            daemon=True # Permite que o programa feche mesmo se a thread estiver rodando
        )
        deployment_thread.start()

if __name__ == "__main__":
    root = tk.Tk()
    app = DeploymentApp(root)
    root.mainloop()
