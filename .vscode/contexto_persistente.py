from playwright.sync_api import sync_playwright

caminho_do_perfil = r"C:\Users\mateu\OneDrive\Desktop\estudo automacao\perfil_do_google"

def acessar_login():

    with sync_playwright() as pw:
        # O comando abaixo já gerencia tudo: ele LÊ se tiver dados e GRAVA se você mudar algo
        contexto = pw.chromium.launch_persistent_context(
            user_data_dir=caminho_do_perfil,
            headless=False,
            channel="chrome", # Opcional, mas ajuda muito no Google
            args=["--disable-blink-features=AutomationControlled"]
        )
        
        pagina = contexto.new_page()
        pagina.goto("https://www.google.com/?hl=pt_BR")
        
        # O pause() serve só para o robô não fechar enquanto você digita
        pagina.pause() 
        
        # Ao fechar aqui, TUDO o que você fez já está gravado na pasta perfil_chrome
        contexto.close()

if __name__ == "__main__":
    acessar_login()
