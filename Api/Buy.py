import os
from dotenv import load_dotenv
import bitget.v2.mix.order_api as maxOrderApi
from bitget.exceptions import BitgetAPIException
from Bot import total

# Chargement des variables d'environnement
load_dotenv()

API_KEY = os.getenv("API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
PASSPHRASE = os.getenv("PASSPHRASE")

# Initialisation de l'API
order_api = maxOrderApi.OrderApi(API_KEY, SECRET_KEY, PASSPHRASE)

# Fonction pratique pour passer un ordre avec quantité paramétrable
def placer_ordre(symbol: str, quantite: float, prix: float, side="open_long", type_ordre="limit"):
    params = {
        "symbol": symbol,
        "marginCoin": "USDT",
        "side": side,  # open_long ou open_short
        "orderType": type_ordre,
        "price": str(prix),
        "size": str(quantite), # quantité dynamique définie ici
        "timeInForceValue": "normal",
        "marginMode": "isolated",
        "productType": "spot"
    }
    try:
        reponse = order_api.placeOrder(params)
        print("Réponse de l'API :", reponse)
        return reponse
    except BitgetAPIException as e:
        print("Erreur rencontrée :", e.message)
        return None

# Exemple concret d'utilisation :
if __name__ == "__main__":
    symbole = "BTCUSDT"
    quantite = 0.0002 
    prix_achat = 40000
    
    # Passer l'ordre en appelant la fonction
    placer_ordre(symbole, total(), prix_achat)
