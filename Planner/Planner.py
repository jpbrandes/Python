import json
import os
import re
from tkinter import messagebox, ttk
import tkinter as tk

ARQUIVO_DB = "contatos.json"


class GerenciadorContatos:
    """Classe responsável por gerenciar a persistência de dados em JSON (CRUD)."""

    def __init__(self):
        self.contatos = {}
        self.carregar_dados()

    def carregar_dados(self):
        if os.path.exists(ARQUIVO_DB):
            try:
                with open(ARQUIVO_DB, "r", encoding="utf-8") as f:
                    self.contatos = json.load(f)
            except json.JSONDecodeError:
                self.contatos = {}
        else:
            self.contatos = {}

    def salvar_dados(self):
        with open(ARQUIVO_DB, "w", encoding="utf-8") as f:
            json.dump(self.contatos, f, indent=4, ensure_ascii=False)

    def criar(self, email, nome, telefone):
        if email in self.contatos:
            return False, "Este e-mail já está cadastrado."
        if not telefone.isdigit():
            return False, "Telefone inválido: contém letras."
        self.contatos[email] = {"nome": nome, "telefone": telefone}
        self.salvar_dados()
        return True, "Contato cadastrado com sucesso."

    def ler_todos(self):
        return self.contatos

    def atualizar(self, email_original, novo_email, nome, telefone):
        # Se o email mudou, precisa verificar se o novo já existe
        if email_original != novo_email and novo_email in self.contatos:
            return False, "O novo e-mail já está sendo usado por outro contato."

        # Se mudou o e-mail, remove o antigo do dicionário
        if email_original != novo_email:
            del self.contatos[email_original]

        self.contatos[novo_email] = {"nome": nome, "telefone": telefone}
        self.salvar_dados()
        return True, "Contato atualizado com sucesso."

    def deletar(self, email):
        if email in self.contatos:
            del self.contatos[email]
            self.salvar_dados()
            return True, "Contato removido com sucesso."
        return False, "Contato não encontrado."


class AppContatos(tk.Tk):
    """Classe que gerencia a interface gráfica (Tkinter)."""

    def __init__(self):
        super().__init__()
        self.db = GerenciadorContatos()
        self.email_selecionado = None

        # Configurações da Janela Principal
        self.title("Cadastro de Contatos - CRUD JSON")
        self.geometry("700x450")
        self.resizable(False, False)

        # Estilo ttk
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.criar_widgets()
        self.atualizar_tabela()

    def criar_widgets(self):
        # --- Formunário de Entrada ---
        frame_form = ttk.LabelFrame(self, text=" Dados do Contato ", padding=15)
        frame_form.pack(fill="x", padx=15, pady=10)

        ttk.Label(frame_form, text="Nome:").grid(
            row=0, column=0, sticky="w", padx=5, pady=5
        )
        self.txt_nome = ttk.Entry(frame_form, width=30)
        self.txt_nome.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_form, text="Telefone:").grid(
            row=0, column=2, sticky="w", padx=5, pady=5
        )
        self.txt_telefone = ttk.Entry(frame_form, width=20)
        self.txt_telefone.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(frame_form, text="E-mail:").grid(
            row=1, column=0, sticky="w", padx=5, pady=5
        )
        self.txt_email = ttk.Entry(frame_form, width=30)
        self.txt_email.grid(row=1, column=1, padx=5, pady=5)

        # --- Frame de Botões ---
        frame_botoes = ttk.Frame(frame_form)
        frame_botoes.grid(
            row=1, column=2, columnspan=2, pady=5, sticky="e", padx=5
        )

        self.btn_salvar = ttk.Button(
            frame_botoes, text="Salvar", command=self.acao_salvar
        )
        self.btn_salvar.pack(side="left", padx=2)

        self.btn_limpar = ttk.Button(
            frame_botoes, text="Limpar", command=self.limpar_campos
        )
        self.btn_limpar.pack(side="left", padx=2)

        self.btn_deletar = ttk.Button(
            frame_botoes,
            text="Excluir",
            command=self.acao_deletar,
            state="disabled",
        )
        self.btn_deletar.pack(side="left", padx=2)

        # --- Visualização de Dados (Tabela Treeview) ---
        frame_tabela = ttk.Frame(self, padding=15)
        frame_tabela.pack(fill="both", expand=True)

        colunas = ("nome", "telefone", "email")
        self.tabela = ttk.Treeview(
            frame_tabela, columns=colunas, show="headings"
        )

        self.tabela.heading("nome", text="Nome")
        self.tabela.heading("telefone", text="Telefone")
        self.tabela.heading("email", text="E-mail")

        self.tabela.column("nome", width=250)
        self.tabela.column("telefone", width=150)
        self.tabela.column("email", width=250)

        # Barra de Rolagem da Tabela
        scrollbar = ttk.Scrollbar(
            frame_tabela, orient="vertical", command=self.tabela.yview
        )
        self.tabela.configure(yscrollcommand=scrollbar.set)

        self.tabela.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Evento de clique na tabela
        self.tabela.bind("<<TreeviewSelect>>", self.ao_selecionar_contato)

    # --- Operações e Lógica do App ---

    def validar_email(self, email):
        padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(padrao, email) is not None

    def limpar_campos(self):
        self.txt_nome.delete(0, tk.END)
        self.txt_telefone.delete(0, tk.END)
        self.txt_email.delete(0, tk.END)
        self.email_selecionado = None
        self.btn_deletar.configure(state="disabled")
        self.tabela.selection_remove(self.tabela.selection())

    def atualizar_tabela(self):
        # Limpa as linhas atuais
        for linha in self.tabela.get_children():
            self.tabela.delete(linha)

        # Carrega dados do JSON e preenche a interface
        contatos = self.db.ler_todos()
        for email, dados in contatos.items():
            self.tabela.insert(
                "", tk.END, values=(dados["nome"], dados["telefone"], email)
            )

    def ao_selecionar_contato(self, event):
        selecao = self.tabela.selection()
        if not selecao:
            return

        item = self.tabela.item(selecao[0])
        valores = item["values"]

        # Preenche os campos de texto com a linha selecionada
        self.limpar_campos()
        self.txt_nome.insert(0, valores[0])
        self.txt_telefone.insert(0, valores[1])
        self.txt_email.insert(0, valores[2])

        # Guarda a chave primária (e-mail) para controle de Updates/Deletes
        self.email_selecionado = valores[2]
        self.btn_deletar.configure(state="normal")

    def acao_salvar(self):
        nome = self.txt_nome.get().strip()
        telefone = self.txt_telefone.get().strip()
        email = self.txt_email.get().strip()

        # Validações básicas
        if not nome or not telefone or not email:
            messagebox.showerror(
                "Erro de Validação", "Todos os campos devem ser preenchidos."
            )
            return

        if not self.validar_email(email):
            messagebox.showerror("Erro de Validação", "E-mail inválido.")
            return

        if self.email_selecionado:
            # Modo Edição (UPDATE)
            sucesso, msg = self.db.atualizar(
                self.email_selecionado, email, nome, telefone
            )
        else:
            # Modo Criação (CREATE)
            sucesso, msg = self.db.criar(email, nome, telefone)

        if sucesso:
            messagebox.showinfo("Sucesso", msg)
            self.limpar_campos()
            self.atualizar_tabela()
        else:
            messagebox.showerror("Erro", msg)

    def acao_deletar(self):
        if not self.email_selecionado:
            return

        confirmar = messagebox.askyesno(
            "Confirmar Exclusão",
            f"Tem certeza que deseja excluir o contato {self.email_selecionado}?",
        )
        if confirmar:
            sucesso, msg = self.db.deletar(self.email_selecionado)
            if sucesso:
                messagebox.showinfo("Sucesso", msg)
                self.limpar_campos()
                self.atualizar_tabela()
            else:
                messagebox.showerror("Erro", msg)


if __name__ == "__main__":
    app = AppContatos()
    app.mainloop()
