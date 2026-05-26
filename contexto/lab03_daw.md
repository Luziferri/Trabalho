Instituto Politécnico de Setúbal

Escola Superior de Ciências Empresariais

Desenvolvimento de Aplicações Web

Lab 03 - Estilização e Design Responsivo com CSS

Ano Letivo: 2025/2026

1 Objetivos

Neste terceiro laboratório iremos ﬁnalizar o desenvolvimento da Página Pessoal através da
aplicação de CSS (Cascading Style Sheets).
Teremos como objetivos principais:

• Compreender a separação entre estrutura (HTML) e apresentação (CSS)

• Aplicar estilos: cores, fontes, tamanhos, espaçamentos, bordas

• Criar layouts proﬁssionais usando posicionamento CSS

• Implementar menus horizontais com técnicas modernas

• Tornar o site responsivo com Media Queries

• Usar pseudo-elementos e pseudo-classes

• Aplicar gradientes, transformações e animações

• Validar CSS com W3C Validator

2 Introdução

Nos laboratórios anteriores, criámos a estrutura (HTML) e semântica do site. Agora, vamos
adicionar a apresentação (CSS) e torná-lo visualmente atraente, proﬁssional e responsivo.

Nota Importante

Neste laboratório, a escolha dos estilos a aplicar ﬁca ao critério do aluno, sendo parte
integrante da avaliação.

1

Desenvolvimento de Aplicações Web

Lab 03 - Estilização e Design Responsivo com CSS

3 Pré-requisitos

• Lab 01 e Lab 02 completos

• Conhecimentos básicos de seletores CSS

• Ficheiros de ícones (opcional, fornecidos no Moodle)

4 Procedimento

Nota Importante

Aviso Importante: Ao copiar código deste documento para o seu editor, tenha cuidado
com aspas, hífenes e outros símbolos tipográﬁcos. Recomenda-se reescrever o código
manualmente ou colar em editor de texto simples antes de levar para VS Code.

4.1 Tarefa 1: Criar Ficheiro CSS Principal

1. Na pasta PaginaPessoal/styles/, crie um ﬁcheiro chamado style.css

2. No <head> de todas as páginas HTML, adicione a ligação ao CSS:

<link rel = " stylesheet " href = " styles/style . css " >

Código 1: Lincar ﬁcheiro CSS

4.2 Tarefa 2: Aplicar Estilos Base

Este é o primeiro passo para estilizar a página. Aqui deﬁnimos:

• Reset CSS: Remove margens e padding padrão dos navegadores

• Estilos globais: Fonte, cor, fundo da página

• Estilos de títulos e links: Base visual para elementos comuns

No ﬁcheiro style.css, comece com estilos globais:

Nota Importante

Nota sobre Códigos Hexadecimais e Unidades:
Quando copiar código CSS do enunciado, tenha cuidado com:

• Códigos de cores: Os códigos hexadecimais devem ﬁcar completos e sem espaços
(ex: #3498db = cardinal + 6 caracteres). Se o copy-paste não funcionou, reescreva
manualmente.

• Unidades: As unidades (como px, em, deg, %, etc) devem estar coladas ao valor, sem
espaços. Correto: padding: 10px, rotate(45deg). Incorreto: padding: 10 px, rotate
(45 deg).

2

Desenvolvimento de Aplicações Web

Lab 03 - Estilização e Design Responsivo com CSS

/* Reset b á sico */
* {

margin: 0;
padding: 0;
box-sizing: border-box ;

}

/* Estilos do body */
body {

font-family: Arial, Helvetica, sans-serif ;
font-size: 16 px ;
line-height: 1.6;
color: #333;
background-color: # f4f4f4 ;
padding: 20 px ;

}

/* T í tulos */
h1 { font-size: 2.5 em ; color: #2 c3e50 ; }
h2 { font-size: 2 em ; color: #34495 e ; }

/* Links */
a {

color: #3498 db ;
text-decoration: none ;

}

a:hover {

text-decoration: underline ;
color: #2980 b9 ;

}

Código 2: Estilos base globais

4.3 Tarefa 3: Estilizar Header e Footer

O header e footer são elementos-chave que enquadram o site. Aqui aplica-se:

• Cores de fundo: Criar contraste com cores mais escuras

• Espaçamento: Padding para conteudo não ﬁcar colado às bordas

• Text-align: Centrar texto para efeito proﬁssional

• Border-radius: Cantos arredondados para aspecto moderno

header {

background-color: #2 c3e50 ;
color: white ;
padding: 20 px ;
text-align: center ;
border-radius: 5 px ;
margin-bottom: 20 px ;

}

3

Desenvolvimento de Aplicações Web

Lab 03 - Estilização e Design Responsivo com CSS

header h1 {

color: white ;
margin: 0;

}

footer {

background-color: #34495 e ;
color: white ;
text-align: center ;
padding: 15 px ;
border-radius: 5 px ;
margin-top: 30 px ;

}

footer a {

color: # ecf0f1 ;

}

footer a:hover {

color: #3498 db ;

}

Código 3: Estilos para header e footer

4.4 Tarefa 4: Criar Menu Horizontal

Transformar o menu de lista vertical num menu horizontal proﬁssional. Os aspetos-chave são:

• list-style: none: Remove os bullets da lista

• display: inline-block: Coloca itens lado a lado na horizontal

• transition: Cria animação suave ao passar o rato

• :hover: Deﬁne cor diferente quando rato passa sobre o menu

nav {

background-color: # ecf0f1 ;
padding: 0;
margin-bottom: 20 px ;
border-radius: 5 px ;

}

nav ul {

list-style: none ;
padding: 0;
margin: 0;
text-align: center ;

}

nav ul li {

display: inline-block ;
margin: 0;

}

nav ul li a {

4

Desenvolvimento de Aplicações Web

Lab 03 - Estilização e Design Responsivo com CSS

display: inline-block ;
padding: 15 px 20 px ;
background-color: #3498 db ;
color: white ;
font-weight: bold ;
transition: background-color 0.3 s ;

}

nav ul li a:hover {

background-color: #2980 b9 ;
text-decoration: none ;

}

Código 4: Menu horizontal

4.5 Tarefa 5: Estilizar Tabelas

Tabelas bem formatadas melhoram a legibilidade dos dados. Aqui aplicamos:

• border-collapse: Remove espaçamento entre células

• thead: Header com cor de fundo para destaque

• nth-child(even): Alterna cores nas linhas

• :hover: Destaca a linha quando o rato passa

Se o seu site tem tabelas (do Lab 02), adicione estilos:

table {

width: 100%;
border-collapse: collapse ;
margin: 20 px 0;
background-color: white ;
box-shadow: 0 2 px 4 px rgba (0 ,0,0,0 .1) ;

}

thead {

background-color: #3498 db ;
color: white ;

}

th, td {

padding: 12 px ;
text-align: left ;
border: 1 px solid # ddd ;

}

tbody tr:nth-child ( even ) {

background-color: # f9f9f9 ;

}

tbody tr:hover {

background-color: # e8f4f8 ;

}

Código 5: Estilos para tabelas

5

Desenvolvimento de Aplicações Web

Lab 03 - Estilização e Design Responsivo com CSS

4.6 Tarefa 6: Adicionar Gradientes

Os gradientes dão um aspecto visual moderno e soﬁsticado. Nesta tarefa:

• linear-gradient(): Máquina de cores suaves e transições

• rgba(): Permite cores com transparência

• Angulos: Controlar direcção do gradiente (135deg, to right, etc)

• Paleta de cores: Escolher cores que harmonizam e criam efeito visual atraente

Para um aspecto visual mais moderno:

Nota Importante

Atenção com Funções CSS: Nas propriedades com funções (como linear-gradient, rgba
, rotate()), é fundamental que os parênteses apareçam imediatamente a seguir ao nome
da função, sem espaços. Exemplo correto: linear-gradient(135deg, ...) e NOT linear
-gradient (135deg, ...). Veriﬁcar cuidadosamente o copy-paste!

header {

background: linear-gradient (135 deg, #667 eea 0% , #764 ba2 100%) ;

}

nav ul li a {

background: linear-gradient ( to right, #3498 db, #2980 b9 ) ;

}

/* Destaque com gradiente */
. destaque {

background: linear-gradient ( to right,

rgba (52 , 152 , 219 , 0) ,
rgba (52 , 152 , 219 , 0.3) ,
rgba (52 , 152 , 219 , 0) ) ;

padding: 20 px ;
border-radius: 5 px ;

}

Código 6: Gradientes CSS

4.7 Tarefa 7: Usar Pseudo-classes e Pseudo-elementos

Para que os estilos de botão funcionem, é necessário adicionar a classe botao aos links do seu
HTML. Por exemplo, no menu de navegação, altere de:

<a href = " index . html " >Home</a>

para:

<a href = " index . html " class = " botao " >Home</a>

Repita isto para todos os links que pretende que tenham o efeito de botão. De seguida,

adicione os seguintes estilos CSS:

6

Desenvolvimento de Aplicações Web

Lab 03 - Estilização e Design Responsivo com CSS

/* Bot õ es com efeito hover */
a . botao {

display: inline-block ;
padding: 10 px 20 px ;
margin: 5 px ;
border-radius: 5 px ;
transition: transform 0.2 s ;

}

a . botao:hover {

transform: scale (1.1) ;

}

/* Adicionar s í mbolo antes de t í tulos */
h2::before {

content: " > " ;
color: #3498 db ;
font-weight: bold ;

}

/* Primeira letra em destaque */
p::first-letter {

font-size: 1.2 em ;
font-weight: bold ;

}

Código 7: Pseudo-classes e pseudo-elementos

4.8 Tarefa 8: Design Responsivo com Media Queries

As Media Queries permitem adaptar o layout a diferentes tamanhos de ecrã. Aqui:

• @media queries: Deﬁnem regras CSS que só se aplicam a certos tamanhos de ecrã

• max-width: Deﬁne até que largura se aplicam as regras

• Mobile vs Desktop: Diferentes layouts para diferentes dispositivos

• Menu em coluna: Em mobile, o menu ﬁca vertical em vez de horizontal

Tornar o site adaptável a dispositivos móveis. Uma forma simples de testar a responsividade
é redimensionar a janela do seu navegador, observando como o layout se adapta conforme a
largura muda. Isto permite validar que os breakpoints estão a funcionar corretamente:

/* Ecr ã s pequenos ( tablets e smartphones ) */
@media screen and ( max-width: 768 px ) {

body {

padding: 10 px ;
font-size: 14 px ;

}

h1 { font-size: 1.8 em ; }
h2 { font-size: 1.5 em ; }

/* Menu em coluna em dispositivos m ó veis */
nav ul li {

7

Desenvolvimento de Aplicações Web

Lab 03 - Estilização e Design Responsivo com CSS

display: block ;
width: 100%;

}

nav ul li a {

width: 100%;
text-align: left ;

}

}

/* Smartphones muito pequenos */
@media screen and ( max-width: 480 px ) {

h1 { font-size: 1.5 em ; }
h2 { font-size: 1.2 em ; }

nav ul li a {

padding: 10 px ;
font-size: 0.9 em ;

}

}

Código 8: Media Queries para responsividade

4.9 Tarefa 9: Animações e Transformações

Animações CSS adicionam interatividade e dinamismo sem JavaScript:

• @keyframes: Deﬁne os passos da animação (from/to ou percentagens)

• animation: Aplica a animação a um elemento

• transform: Modiﬁca tamanho, rotação e posição

• transition: Suaviza mudanças de estilo ao passar do rato

Nota Importante

Nota sobre Compatibilidade: Alguns navegadores mais antigos podem não suportar al-
gumas propriedades CSS 3 como transform, animation ou flex. Para melhor compati-
bilidade, preﬁxos como -webkit-, -moz- podem ser necessários (ex: -webkit-transform).
Testes em vários navegadores são recomendados.

@keyframes deslizamento {

from {

transform: translateX ( -100px ) ;
opacity: 0;

transform: translateX (0) ;
opacity: 1;

}
to {

}

}

header {

animation: deslizamento 0.5 s ease-in ;

8

Desenvolvimento de Aplicações Web

Lab 03 - Estilização e Design Responsivo com CSS

}

/* Efeito de escala no hover */
img:hover {

transform: scale (1.05) ;
transition: transform 0.3 s ;

}

Código 9: Animações CSS

4.10 Tarefa 10: Container Principal

O container centraliza e enquadra todo o conteúdo da página. Benefícios:

• max-width: Limita a largura para melhor legibilidade

• margin: 0 auto: Centraliza o container no ecrã

• box-shadow: Adiciona "profundidade"visual

• background-color: Separa visualmente o conteúdo principal do fundo

Para um layout mais proﬁssional, necessita de envolver o conteúdo principal da sua página

numa div com a classe container. No seu HTML, estruture da seguinte forma:

<body>

<header> ... </header>
<nav> ... </nav>
<div class = " container " >

<main>

<article>

<h2>T í tulo do Artigo</h2>
<p>Conte ú do do artigo ... </p>

</article>

</main>

</div>
<footer> ... </footer>

</body>

De seguida, adicione os seguintes estilos CSS:

. container {

max-width: 1200 px ;
margin: 0 auto ;
padding: 20 px ;
background-color: white ;
box-shadow: 0 0 20 px rgba (0 ,0,0,0 .3) ;

}

main {

min-height: 400 px ;

}

article {

padding: 20 px ;
margin: 20 px 0;
border-left: 4 px solid #3498 db ;

9

Desenvolvimento de Aplicações Web

Lab 03 - Estilização e Design Responsivo com CSS

}

Código 10: Container principal

4.11 Tarefa 11: Testar Responsividade

1. Abra o navegador e pressione F12 (DevTools)

2. Clique no ícone de dispositivo móvel (no canto superior esquerdo)

3. Teste em diferentes resoluções:

• iPhone 12: 390 x 844px

• iPad: 768 x 1024px

• Desktop: 1920 x 1080px

4. Redimensione a janela e observe o comportamento do menu

4.12 Tarefa 12: Validar CSS

1. Aceda a https://jigsaw.w3.org/css-validator/

2. Selecione Validate by File Upload

3. Faça upload do ﬁcheiro style.css

4. Corrija eventuais erros reportados

5 Conceitos-Chave

5.1 Seletores CSS

Descrição
Seleciona todos os elementos dessa tag
Seleciona elementos com essa classe
Seleciona elemento com esse ID (único)

Seletor
elemento
.classe
#id
ancestor descendant Seleciona descendentes
:hover
::before

Pseudo-classe: quando o rato passa
Pseudo-elemento: antes do conteúdo

5.2 Box Model

Todo o elemento HTML é uma “caixa” com:

• Content: conteúdo do elemento

• Padding: espaço dentro da borda

• Border: borda à volta do elemento

• Margin: espaço fora da borda

10

Desenvolvimento de Aplicações Web

Lab 03 - Estilização e Design Responsivo com CSS

5.3 Responsividade

Breakpoints comuns:

• Mobile: até 480px

• Tablet: 481px - 768px

• Desktop: 769px ou mais

6 Resultado Esperado

No ﬁnal desta tarefa, deve ter:

□ Site completamente estilizado com CSS proﬁssional

□ Menu horizontal funcional e visualmente atraente

□ Tabelas bem formatadas (se aplicável)

□ Site responsivo (funciona em mobile, tablet, desktop)

□ Uso de gradientes, animações ou transformações

□ CSS válido (sem erros no W3C Validator)

□ Código organizado e comentado

7 Questões para Reﬂexão

1. Por que é importante separar HTML (estrutura) de CSS (apresentação)?

2. Qual a vantagem de usar Media Queries em vez de criar versões separadas do site?

3. Qual a diferença entre display: none e visibility: hidden?

4. Como as pseudo-classes e pseudo-elementos melhoram a experiência do utilizador?

8 Próximos Passos

No decorrer da disciplina, iremos expandir nosso conhecimento de desenvolvimento web:

• Próximos Laboratórios: Interatividade com JavaScript

– Comportamento dinâmico e manipulação de elementos
– Validação de dados e interações com o utilizador
– Efeitos e animações avançadas
– Exploração de novos projectos e contextos

11

Desenvolvimento de Aplicações Web

Lab 03 - Estilização e Design Responsivo com CSS

9 Referências

• MDN CSS: https://developer.mozilla.org/en-US/docs/Web/CSS

• CSS-Tricks: https://css-tricks.com/

• Can I Use: https://caniuse.com/

• CSS Validator: https://jigsaw.w3.org/css-validator/

• Flexbox Guide: https://css-tricks.com/snippets/css/a-guide-to-flexbox/

• MDN - Media Queries: https://developer.mozilla.org/en-US/docs/Web/CSS/Media_

Queries

12

