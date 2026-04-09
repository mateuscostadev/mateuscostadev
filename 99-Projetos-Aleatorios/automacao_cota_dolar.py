# exercicio pegar a cotação do dolar e tirar um print

from playwright.sync_api import sync_playwright
import time
import random

#-----------COMPORTAMENTO HOMANO------------

def delay_humano(minimo=0.2, maximo=0.8):
    atraso = random.uniform(minimo, maximo)
    print(f"Soneca de {atraso:.2f} segundos...")
    time.sleep(atraso)

def clicar_como_humano(elemento):
    elemento.hover()
    delay_humano()
    elemento.click(delay=random.randint(80, 150))

#-----------SEGURANÇA PRA NÃO SER BLOQUEADO NAS NAVEGAÇÕES IVI-BOT ------------

def cotacao_dolar():
    with sync_playwright() as pw:
        Navegador = pw.chromium.launch(headless=False, channel="chrome",
        args=["--disable-blink-features=AutomationControlled"])

        contexto = Navegador.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
            locale="pt-BR",
            java_script_enabled=True,
            viewport={"width": 1366, "height": 768}
        )
        contexto.add_init_script('''
        Object.defineProperty(navigator, 'webdriver', {
        get: () => undefined });
        ''')

        #-----------COMEÇAR A AUTOMAÇÃO DO PROJETO------------
        
        pagina = contexto.new_page()
        pagina.goto("https://www.google.com/?hl=pt_BR")
        pagina.wait_for_load_state("networkidle")
        delay_humano()

        #selecionando o campo de busca
        campo = pagina.locator("textarea[title='Pesquisar']")
        #digitando no campo de busca
        campo.press_sequentially("dolar hoje", delay=random.randint(100, 150))
        #apertando enter
        campo.press("Enter")
        #esperando a pagina carregar completamente
        pagina.wait_for_load_state("networkidle")
        delay_humano()
        #esperando até que esse campo apareça na tela
        pagina.wait_for_selector("span.DFlfde.SwHCTb")
        #pegando a cotaçao e armezenando em uma variável
        elemento_cotacao = pagina.locator("span[data-precision='2']").first
        #batendo um screenshot da cotacao em imagem
        elemento_cotacao.screenshot(path="foto_cotacao.png")
        #trazendo esse screenshot para um arquivo no python 
        valor_cotacao = elemento_cotacao.inner_text()

        #print(valor_cotacao)
        
        delay_humano()

        Navegador.close()

if __name__ == '__main__':
    cotacao_dolar()