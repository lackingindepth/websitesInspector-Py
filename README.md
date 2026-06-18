# Web Inspector - python
## Objetivos
O Web Inspector é uma ferramenta de linha de comando desenvolvida em Python para inspecionar configurações HTTP e TLS de um website. A aplicação coleta informações como headers de segurança, cookies, certificado TLS, registros DNS, redirecionamentos, status HTTP e tempo de resposta, permitindo avaliar rapidamente a configuração de segurança de um servidor web.
## Funcionalidades

 HTTP Status Code

 Redirect Chain

 HTTP Security Headers

 Cookies Inspection

 TLS Certificate Inspection

 DNS Records

 Response Time

 Server Information

 
## Tecnologias Utilizadas
O projeto foi feito completamente em python, utilizando bibliotecas padrão mas também:
requests para realizar as requisições HTTP e coleta headers, cookies, redirecionamentos e status code.
as libs ssl e socket para estabelecer conexão sem utilizar o HTTPS e pegar informações de TLS;
dnspython para obter informações sobre o DNS.

## Como utilizar
1. Clonar o repositório
```
git clone https://github.com/lackingindepth/websitesInspector-Py.git
cd ~pasta onde foi clonado~
```

2. Criar ambiente virtual
```
Windows
python -m venv venv
venv\Scripts\activate
```
```
Linux
python3 -m venv venv
source venv/bin/activate
```
4. Instalar dependências
```
pip install -r requirements.txt
```

6. Executar o projeto
```
python main.py
```

## Aprendizados
Além de aprimorar os conhecimentos com requisições e respostas http, enquanto tentava entender o que o header retornava, compreendi a importancia de sua segurança. Compreendi o funcionamento do handshake TLS, da negociação de chaves e do papel das Autoridades Certificadoras (CAs) na emissão de certificados digitais.
Acabei também percendo um pouco de como vulnerabilidades funcionam, e de como quem ataca interpreta o problema, o que eu acho de bastante utilidade quando estiver arquitetando
um sistema - isso é, pensar em usuários maldosos e aplicar boas práticas para evitar que quaisquer problemas apareçam.

## Futuras implementações
Futuras versões poderão incluir torná-lo de fato um analisador, com score, que utilize de métricas baseada nessas mesmas informações, para saber se um site é mais ou menos seguro.
Para isso, além de estabelecer critérios, também irá aumentar o número de variáveis resposáveis por fazer essa indicação. Adicionando analise de TLD suspeitos,
há quanto dias o domínio existe, entre outros.

## Nota
O Web Inspector não identifica automaticamente se um site é malicioso. Ele inspeciona configurações técnicas do servidor e apresenta informações que podem auxiliar em análises de segurança. A interpretação dos resultados depende do contexto e não substitui ferramentas de reputação ou scanners de vulnerabilidades. Foi feito com o objetivo de aprendizado.
