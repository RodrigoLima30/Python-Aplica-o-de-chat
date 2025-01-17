# Tela Inicial: Hashzap
    # Título
    # Botão Inicial chat
        # Quando clicar no botão:
        # Abrir um popup/modal/alerta
            # Título: Bem vindo ao hashzap
            # Caixa de Texto: Escrever seu nome no chat
            # Botão: Entrar no chat
                # Quando clicar no botão:
                # Fechar o popup
                # Sumir com o título
                # Sumir com o botão iniciar chat
                    # Carregar o chat
                    # Carregar o campo de enviar mensagem: "Digite sua mensagem"
                    # Botão Enviar
                        # Quando clicar no botão enviar:
                        # Enviar mensagem
                        # Limpar a caixa de mensagem

# Usaremos a bib Flet - consegue ao mesmo tempo construir site, aplicativo e programa de computador

# Flat
# importar o flet
import flet as ft

# criar uma função principal para rodar o seu aplicativo

def main(pagina):
    # colocar o que essa função vai fazer
    # título
    titulo = ft.Text("HashZap");

    # websoket - tunel de comunicação entre 2 usuários

    def enviar_mensagem_tunel(mensagem):
        # executar tudo que eu quero que aconteça para todos os usuarios que receberem a mensagem
        texto = ft.Text(mensagem);
        chat.controls.append(texto);
        pagina.update();
    
    pagina.pubsup.subscribe(enviar_mensagem_tunel);


    def enviar_mensagem(evento):
        nome_usuario = caixa_nome.value;
        texto_campo_mensagem = campo_enviar_mensagem.value;
        mensagem = f"{nome_usuario}: {texto_campo_mensagem}"
        pagina.pubsub.send_all(mensagem);
        # limpar a caixa de enviar mensagem
        campo_enviar_mensagem.value = "";
        pagina.update()
    
    campo_enviar_mensagem = ft.TextField(label="Digite aqui sua mensagem", on_submit=enviar_mensagem);
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem);
    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar]);

    chat = ft.Column();

    def entrar_chat(evento):
        # Fechar o popup
        popup.open = False;
        # sumior com o titulo
        pagina.remove(titulo);
        # Sumir com o botão iniciar chat
        pagina.remove(botao);
        # Carregar o chat
        pagina.add(chat);
        # Carregar o campo de enviar mensagem: "Digite sua mensagem" e botao enviar
        pagina.add(linha_enviar);

        # adicionar no chat a mensagem: "fulano entrou no chat"
        nome_usuario = caixa_nome.value
        mensagem = f"{nome_usuario} entrou no chat";
        pagina.pubsub.sand_all(mensagem);
        pagina.uptade();

    # criar o popup
    titulo_popup = ft.Text("Bem vindo ao HashZap");
    caixa_nome = ft.TextField(label="Digite o seu nome");
    botao_popup = ft.ElevatedButton("Entrar no Chat", on_click=entrar_chat);

    popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome, actions=[botao_popup]);

    # botão inicial
    def abrir_popup(evento): # sempre que uma função está atribuída no evento de click no botão, ela tem q receber
    # obrigatoriamente como parametro uma variavel evento que é onde ele vai armazenar 
    # as informções do click no botão
        pagina.dialog = popup;
        popup.open = True;
        pagina.update(); # sempre que eu executar algo preciso usar depois o update
        print("Clicou no botão");

    botao = ft.ElevatedButton("Iniciar Chat", on_click = abrir_popup);

    # colocar os elementos na página
    pagina.add(titulo);
    pagina.add(botao);

# executar essa função com o flet
ft.app(main, view=ft.WEB_BROWSER);