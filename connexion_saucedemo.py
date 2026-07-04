from selenium import webdriver
# Cet import permet de définir la stratégie de ciblage (By.ID, By.CSS_SELECTOR, etc.)
from selenium.webdriver.common.by import By
import time

# 1. Initialisation du navigateur Chrome
driver = webdriver.Chrome()

try:
    # 2. Visite de la page de connexion de SauceDemo
    driver.get("https://saucedemo.com")
    driver.maximize_window()
    
    # 3. Saisie de l'identifiant (Username)
    # SauceDemo fournit un attribut id="user-name" sur ce champ
    champ_username = driver.find_element(By.ID, "user-name")
    champ_username.send_keys("standard_user")
    print("Identifiant saisi avec succès.")
    
    # 4. Saisie du mot de passe (Password)
    #  on utilise un sélecteur CSS pour diversifier la méthode
    champ_password = driver.find_element(By.CSS_SELECTOR, "#password")
    champ_password.send_keys("secret_sauce")
    print("Mot de passe saisi avec succès.")
    time.sleep(12)
    # 5. Clic sur le bouton de connexion (Login)
    # On cible l'élément par son attribut Name : name="login-button"
    bouton_login = driver.find_element(By.NAME, "login-button")
    bouton_login.click() 
    print("Clic sur le bouton Login effectué.")
    
    #  pause pour contempler le Dashboard après connexion
    time.sleep(60)
    
    # 6. Assertion du Jour 2 : Vérifier que la connexion a réussi
    # Si la connexion réussit, l'URL change et contient "/inventory.html"
    assert "inventory.html" in driver.current_url
    print("Victoire ! Connexion réussie et validée au vert.")

finally:
    # 7. Fermeture propre du navigateur
    driver.quit()
