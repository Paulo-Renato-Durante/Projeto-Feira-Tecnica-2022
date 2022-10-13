from selenium import webdriver
import time


def pesquisa(placa):

    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')



    driver = webdriver.Firefox(options = options)
    driver.get("https://www.despachantedok.com.br/?gclid=CjwKCAjwvsqZBhAlEiwAqAHElfFSvg__61DWUwu_08lRn4Jt4kEZxELS3PgNHHWKnJz9ibM9Y6mo1BoCYOkQAvD_BwE")
    identificador = driver.find_element("name", "identificador")
    identificador.send_keys(placa)
    email = driver.find_element("name", "email")
    email.send_keys('paulorenatodurante@gmail.com')

    time.sleep(6)

    botao = driver.find_element('xpath', '/html/body/main/section[1]/div/div/div/div/div/div[1]/form/div[2]/button')
    botao.click()
    time.sleep(25)
    try:
        detalhesDebito = list()
        detalhesValor = list()

        nome = driver.find_element('xpath', '//*[@id="checkoutDok"]/div/main/section/div/aside/div/div/div[1]/p').text
        localidade = driver.find_element('xpath','//*[@id="checkoutDok"]/div/main/section/div/aside/div/div/div[2]/p').text
        botao = driver.find_element('xpath','//*[@id="checkoutDok"]/div/main/section/div/div/section/div[2]/div[1]/div[1]/a')
        botao.click()

        detalhesDebito.append(driver.find_element('xpath','//*[@id="checkoutDok"]/div/main/section/div/div/section/div[3]/div[2]/div/div/div/div/p').text)
        detalhesValor.append(driver.find_element('xpath','//*[@id="checkoutDok"]/div/main/section/div/div/section/div[3]/div[2]/div/div/div/div/div/p').text)


        try:
            botao = driver.find_element('xpath','//*[@id="checkoutDok"]/div/main/section/div/div/section/div[4]/div[1]/div[1]/a')
            botao.click()
            detalhesDebito.append(driver.find_element('xpath', '//*[@id="checkoutDok"]/div/main/section/div/div/section/div[4]/div[2]/div/div/div/div/p').text)
            detalhesValor.append(driver.find_element('xpath','//*[@id="checkoutDok"]/div/main/section/div/div/section/div[4]/div[2]/div/div/div/div/div/p').text)

        except:
            pass
        dicionario = {
            'detalhesDebitos':detalhesDebito,
            'valores':detalhesValor,
            'nome': nome,
            'localidade':localidade
        }
        return dicionario
    except:

        return 'documento em ordem'
    finally:
        driver.quit()
