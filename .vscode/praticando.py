from playwright.sync_api import sync_playwright

# FUNÇÃO 1: Apenas para "carregar as baterias" (Login)
def salvar_sessao():
    with sync_playwright() as pw:
        navegador = pw.chromium.launch(headless=False)
        contexto = navegador.new_context()
        pagina = contexto.new_page()
        
        pagina.goto("https://accounts.google.com")
        print("Logue e feche o navegador no 'pause'...")
        pagina.pause()
        
        contexto.storage_state(path="estado_login.json")
        navegador.close()

# FUNÇÃO 2: O trabalho real (Extração de Dados)
def extrair_dados_logado():
    with sync_playwright() as pw:
        navegador = pw.chromium.launch(headless=False)
        
        # AQUI ESTÁ A MÁGICA: Ele já nasce com o login da função anterior
        contexto = navegador.new_context(storage_state="estado_login.json")
        pagina = contexto.new_page()
        
        pagina.goto("https://www.youtube.com")
        
        # Aqui você colocaria sua lógica de Engenheiro de Dados:
        # titulo = pagina.title()
        # print(f"Logado com sucesso no canal: {titulo}")
        
        navegador.close()

# --- EXECUTANDO ---
if __name__ == "__main__":
    # salvar_sessao()  <-- Você roda essa uma vez na vida
    extrair_dados_logado() # <-- Essa você roda 1000 vezes por dia