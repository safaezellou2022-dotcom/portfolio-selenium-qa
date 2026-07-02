from selenium import webdriver
import time

# 1. Initialisation du navigateur Chrome
driver = webdriver.Chrome()

try:
    # 2. Visite du nouveau site (L'équivalent de cy.visit)
    driver.get("https://saucedemo.com")
    driver.maximize_window()
    
    # Petite pause d'une minute  pour observer visuellement le navigateur
    time.sleep(60)
    
    # 3. Assertion du Jour 1 : Vérifier le titre de la page de connexion
    assert "Swag Labs" in driver.title
    print("Félicitations ! Le script s'est exécuté avec succès.")
    print("Le navigateur a ouvert SauceDemo et le titre de la page est correct.")

finally:
    # 4. Fermeture propre du navigateur (Indispensable avec Selenium)
    driver.quit()
