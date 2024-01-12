# GDrive Copia Compartilhados

Script que faz uma cópia dos arquivos que foram compartilhados com você no Google Drive para seu Drive, para que consiga editar os arquivos.

# Instalação

Segue script para instalação:

```
git clone https://github.com/riguima/gdrive-copia-compartilhados
cd gdrive-copia-compartilhados
pip install -r requirements.txt
```

# Autenticação

Acesse o [Console de APIs](https://console.developers.google.com/iam-admin/projects) e crie seu projeto.

Procure por 'API e Serviços' no menu lateral, selecione 'API e Serviços Ativados' e depois clique em 'Ativar APIs e Serviços', pesquise por Google Drive e clique em 'Ativar'.

Selecione 'Credenciais' no menu esquerdo, clique em 'Criar credenciais', selecione 'ID do cliente OAuth'.

Agora, o nome do produto e a tela de consentimento precisam ser definidos -> clique em 'Configurar tela de consentimento' e siga as instruções. Depois de terminar:

Selecione 'Tipo de aplicativo' para ser aplicativo da Web.

Insira um nome apropriado.

Insira http://localhost:8080 para 'Origens JavaScript autorizadas'.

Insira http://localhost:8080/ para 'URIs de redirecionamento autorizados'.

Clique em 'Salvar'.

Clique em 'Baixar JSON' no lado direito do Client ID para baixar client_secret_<ID>.json.

O arquivo baixado contém todas as informações de autenticação da sua aplicação. Renomeie o arquivo para “client_secrets.json” e copie para a pasta `gdrive-copia-compartilhados`.

Depois disso vai em `Tela de permissão OAuth` na parte de `Credenciais` e publique seu aplicativo.

Renomeie o arquivo `base-settings.yaml` para `settings.yaml` e edite o arquivo inserindo seu `CLIENT_ID` e `CLIENT_SECRET` not locais indicados no arquivo.

Rode o script com `python main.py`.
