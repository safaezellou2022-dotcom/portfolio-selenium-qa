from selenium import webdriver
from selenium.webdriver.common.by import By
#  LES IMPORTS CLÉS POUR L'ASYNCHRONISME :
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Initialisation du navigateur Chrome
driver = webdriver.Chrome()

try:
    # 2. Visite et Connexion rapide (Acquis du Jour 2)
    driver.get("https://saucedemo.com")
    driver.maximize_window()
    
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.NAME, "login-button").click()
    
    # 3. ÉTAPE ASYNCHRONE : Ouvrir le menu latéral (Burger Menu)
    # On clique sur le bouton du menu
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    print("Clic sur le menu burger effectué.")
    
    # 4. L'EXPLICIT WAIT 
    # Le menu latéral s'ouvre avec une animation CSS lente. Si on clique tout de suite sur "Logout", le test plante.
    # On dit à Selenium : "Attends jusqu'à 10 secondes que le lien Logout soit visible et cliquable"
    lien_logout = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    )
    
    # 5. Action après attente dynamique
    lien_logout.click()
    print("Clic sur le lien de déconnexion effectué.")
    
    # 6. Assertion : Vérifier qu'on est bien revenu sur la page de connexion
    # On attend dynamiquement que le bouton Login soit de nouveau visible pour confirmer la déconnexion
    #WebDriverWait(driver, 10).until(
     #   EC.visibility_of_element_located((By.NAME, "login-button"))
    #)
    assert "saucedemo.com" in driver.current_url and "inventory.html" not in driver.current_url
    print("Victoire ! Déconnexion réussie et validée de manière asynchrone au vert !")

finally:
    # 7. Fermeture propre du navigateur
    driver.quit()
