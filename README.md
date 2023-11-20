# Visão Geral

Aquole é um produto consistente em um reservatório de água integrado a um sistema de monitoramento de volume e incidência de resíduos. Este reservatório contém um sistema de filtragem e captação de água das calhas de residências em períodos de chuva.

O reservatório possui um acelerômetro dentro de uma boia e sensores de luminosidade que realizam o monitoramento da quantidade de água de de resíduos existentes em seu interior.

Todo o monitoramento pode ser feito através de uma aplicação móvel ou navegador em tempo real, apresentando também resultados da quantidade de água economizada ao utilizá-lo.

# Casos de Uso

## Funcionalidade: FG01 - Monitoramento do Reservatório

- Como usuário interessado no estado do reservatório
- Eu quero monitorar em tempo real o volume de água e a presença de resíduos no reservatório
- Para garantir o uso eficiente do sistema e a tomada de decisões informadas sobre seu funcionamento.

### Cenário: FG01-C01 - Visualização do Estado Atual

Dado que o usuário está logado na aplicação móvel ou navegador

Quando o usuário acessa a página de monitoramento do reservatório

Então o sistema exibe em tempo real o volume atual de água e a presença de resíduos no reservatório.

### Cenário: FG01-C02 - Alerta de Volume Alto

Dado que o volume de água no reservatório está acima de um nível pré-definido

Quando o usuário acessa a página de monitoramento

Então o sistema emite um alerta indicando a necessidade de esvaziamento do reservatório.

### Cenário: FG01-C03 - Alerta de Alta Quantidade de Resíduos

Dado que a quantidade de resíduos no reservatório ultrapassa um limite pré-definido


Quando o usuário acessa a página de monitoramento


Então o sistema emite um alerta indicando a alta quantidade de resíduos detectada.

## Funcionalidade: FG02 - Captura de Água da Chuva

- Como usuário consciente sobre o uso sustentável da água
- Eu quero que o sistema capture água da chuva por meio das calhas residenciais
- Para maximizar a eficiência do reservatório e contribuir para a sustentabilidade hídrica.

### Cenário: FG02-C01 - Ativação Automática da Captura de Água

Dado que o sistema está instalado e configurado corretamente


Quando é detectida chuva pelas calhas residenciais


Então o sistema ativa automaticamente a captura de água da chuva para o reservatório.

### Cenário: FG02-C02 - Desativação Manual da Captura de Água

Dado que o usuário deseja desativar temporariamente a captura de água da chuva


Quando o usuário acessa a aplicação móvel ou navegador


Então o sistema permite a desativação manual da captura de água.

## Funcionalidade: FG03 - Apresentação de Resultados de Economia

- Como usuário interessado em sustentabilidade e economia de água


- Eu quero ver os resultados da quantidade de água economizada pelo sistema


- Para acompanhar o impacto ambiental positivo e a eficácia do sistema.


### Cenário: FG03-C01 - Visualização dos Resultados de Economia

Dado que o usuário acessa a página de resultados na aplicação móvel ou navegador

Quando o usuário seleciona o período desejado

Então o sistema exibe a quantidade total de água economizada pelo sistema durante o período escolhido.


## Funcionalidade: FG04 - Seleção de Reservatório

- Como usuário com vários reservatórios em diferentes locais
- Eu quero poder selecionar qual reservatório desejo monitorar
- Para personalizar a visualização e o controle com base na localização específica.


### Cenário: FG04-C01 - Seleção de Reservatório Padrão

Dado que o usuário possui vários reservatórios configurados no sistema

Quando o usuário acessa a aplicação móvel ou navegador

Então o sistema exibe uma lista dos reservatórios disponíveis e permite a seleção de um reservatório padrão para monitoramento.

### Cenário: FG04-C02 - Troca de Reservatório Ativa


Dado que o usuário já selecionou um reservatório padrão

Quando o usuário decide trocar para um reservatório diferente

Então o sistema atualiza dinamicamente a visualização e os dados para refletir o reservatório recém-selecionado.
