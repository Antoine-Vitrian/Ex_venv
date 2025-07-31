import os
import requests

# 1. Obtenha a chave da API a partir das variáveis de ambiente.
#    É uma prática mais segura do que deixá-la no código.
#    (Usei a chave do seu exemplo como um valor padrão caso a variável não exista)
api_key = os.environ.get("EXCHANGERATE_API_KEY", "9a554695c49965e063f2a44f")

# 2. Defina a moeda base que você quer consultar.
moeda_base = "USD"

# 3. Construa a URL de forma dinâmica.
url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{moeda_base}"

print(f"Buscando taxas de câmbio para {moeda_base}...")

# 4. Faça a requisição para a API.
response = requests.get(url)

# 5. Converta a resposta (que vem em formato JSON) para um dicionário Python.
dados = response.json()

# 6. Verifique se a API retornou um resultado de sucesso.
if dados.get("result") == "success":
    # 7. Acesse o dicionário com as taxas de conversão.
    taxas = dados.get("conversion_rates")

    moeda = input("Escolha a moeda:")
    if moeda in taxas:
        # 8. Exiba as taxas de algumas moedas de interesse.
        print("\n--- Taxas de Conversão ---")
        print(f"1 {moeda_base} = {taxas.get(moeda)} {moeda}")
    else:
        print("Moeda não encontrada")

else:
    print("erro")

