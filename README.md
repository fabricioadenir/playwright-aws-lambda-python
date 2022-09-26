# playwright-aws-lambda-python

- O playwright só funciona com versões especificas do chrome. Por isso criei esse repo para contribuir para quem tiver com a mesma dificuldade.

- A lib pyppeteer que fará o download do chrme mas o default dela é uma versão mais antiga do navegador.
Por isso que definimos a variável de ambiente com a versão aceita pelo playwright PYPPETEER_CHROMIUM_REVISION 

# Rodar local.
```
functions-framework --target print_tela_google
```
# Fazer deploy.
```
gcloud beta functions deploy print_tela_google --runtime python38 --trigger-http --memory=1GB --timeout=540s --allow-unauthenticated
```
