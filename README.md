# Aplicativo de Previsão do Tempo
Este é um aplicativo simples de previsão do tempo construído usando PyQt5 e APIs do WeatherAPI. O aplicativo permite que os usuários obtenham previsões do tempo para uma localização específica com base em latitude e longitude. Ele também inclui uma janela secundária para os usuários inserirem as coordenadas do local desejado.

Para utilizar o aplicativo, simplesmente faça o download do projeto e execute "Previsão do tempo"

### Para utilizar o aplicativo direto do código fonte:

Para usar este aplicativo, você precisará de chaves de API do WeatherAPI. Veja como obtê-las:

Chave de API do WeatherAPI: Você precisa de uma chave de API do WeatherAPI para acessar os dados de previsão do tempo. Você pode se inscrever para obter uma conta gratuita em seu site e obter uma chave de API no painel de controle.

Chave de API do Geo Localização do WeatherAPI: Você também precisa de uma chave para a API de Geo Localização do WeatherAPI, que é usada para recuperar as coordenadas de latitude e longitude para uma determinada cidade e estado. Isso pode ser obtido de maneira semelhante à chave de API de previsão do tempo.

Depois de obter ambas as chaves de API, edite o arquivo .env e insira suas chaves nos respectivos locais.

api_key = "SUA_CHAVE_DE_API_DO_WEATHERAPI", 
weather_key = "SUA_CHAVE_DE_API_DE_GEO_LOCALIZACAO_DO_WEATHERAPI"

### Instalação
Instale os pacotes necessários:

pip install PyQt5 requests python-dotenv
pip install PyQt5
pip install requests

# Uso
### python janela_principal.py

Ao iniciar o aplicativo, você verá a janela principal exibindo a previsão do tempo para o dia atual e localização.

Clique no botão "Buscar localização" para abrir a janela secundária, onde você pode inserir a cidade e o estado para obter as coordenadas de latitude e longitude.

Clique no botão "Buscar" na janela secundária para recuperar as coordenadas de latitude e longitude.

Você pode copiar as coordenadas clicando no botão "Enviar para Área de Previsão".

Cole as coordenadas nos campos de entrada de latitude e longitude da janela principal.

Clique no botão "Previsão" para buscar a previsão do tempo para as coordenadas especificadas.

Use o botão de seta para a direita para navegar pelos dias da previsão e o botão de seta para a esquerda para voltar.

### Contribuição
Sinta-se à vontade para contribuir com este projeto, abrindo problemas, sugerindo melhorias ou enviando pull requests.
