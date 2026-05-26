Instituto Politécnico de Setúbal

Escola Superior de Ciências Empresariais

Desenvolvimento de Aplicações Web

Lab 02 - Elementos HTML5 Semânticos, Tabelas e Multimédia

Ano Letivo: 2025/2026

1 Objetivos

Neste segundo laboratório iremos continuar com o desenvolvimento da nossa Página Pessoal,
adicionando estrutura mais proﬁssional e conteúdo expandido.

• Utilizar elementos HTML5 semânticos: <header>, <nav>, <article>, <section>, <aside>, <footer

>

• Criar tabelas estruturadas com <table>, <tr>, <td>, <th>, <thead>, <tbody>

• Usar atributos avançados de tabelas: colspan, rowspan

• Incorporar elementos multimédia: <video>, <audio>, <iframe>

• Usar elementos de formatação semântica: <strong>, <em>, <mark>

• Compreender a diferença entre elementos semânticos e elementos de apresentação

2 Introdução

No laboratório anterior, criámos a estrutura base do nosso site com HTML elementar. Agora,
iremos:

1. Melhorar a semântica do HTML usando elementos HTML5 modernos

2. Adicionar tabelas para apresentar informação estruturada

3. Incorporar multimédia (vídeo, áudio, iframes)

4. Continuar a expandir o conteúdo das páginas

1

Desenvolvimento de Aplicações Web

Lab 02 - Elementos HTML5 Semânticos, Tabelas e Multimédia

Nota Importante

Neste laboratório, apenas devem ser utilizados os conceitos HTML. Não devem usar CSS
inline nem JavaScript. A formatação visual virá no Lab 03.

3 Elementos HTML5 Semânticos

Os elementos semânticos HTML5 descrevem o signiﬁcado do conteúdo, não apenas a sua
apresentação. Isto melhora a acessibilidade, SEO e manutenibilidade.

3.1 Principais Elementos

Elemento
<header>
<nav>
<main>
<article>
<section>
<aside>
<footer>
<figure>
<figcaption>

Uso
Cabeçalho da página ou secção (logo, título, navegação)
Bloco de navegação (menu principal)
Conteúdo principal da página (único por página)
Conteúdo independente (post, notícia, comentário)
Agrupamento temático de conteúdo
Conteúdo relacionado mas secundário (sidebar)
Rodapé da página ou secção (copyright, links)
Conteúdo ilustrativo (imagem, diagrama)
Legenda de uma <figure>

Nota Importante

Neste laboratório, apenas devem ser utilizados os conceitos HTML. Não devem usar CSS
inline nem JavaScript. A formatação visual virá no Lab 03.

4 Procedimento

Nota Importante

Aviso Importante: Ao copiar código deste documento para o seu editor, tenha cuidado
com aspas, hífenes e outros símbolos tipográﬁcos. Recomenda-se reescrever o código
manualmente ou colar em editor de texto simples antes de levar para VS Code.

4.1 Tarefa 1: Reestruturar index.html com Semântica

Abra o ﬁcheiro index.html e reestruture-o usando elementos semânticos:
<!DOCTYPE html>
<html lang = " pt " >
<head>

<meta charset = " UTF-8 " >
<meta name = " viewport " content = " width = device-width, initial-scale =1.0

" >

<title>P á gina Pessoal - [ Seu Nome ] </title>

</head>

2

Desenvolvimento de Aplicações Web

Lab 02 - Elementos HTML5 Semânticos, Tabelas e Multimédia

<body>

<!-- Cabe ç alho da p á gina -->
<header>

<h1> [ Seu Nome ] </h1>
<p><em>Estudante de Gest ã o de Sistemas de Informa ç ã o</em></p>

</header>

<!-- Menu de navega ç ã o -->
<nav>

<h2>Menu</h2>
<ul>

<li><a href = " pessoal . html " >Dados Pessoais</a></li>
<li><a href = " familia . html " >Fam í lia</a></li>
<li><a href = " formacao . html " >Forma ç ã o</a></li>
<li><a href = " curriculum . html " > Curr icu l um< /a></li>
<li><a href = " hobbies . html " >Hobbies</a></li>

</ul>

</nav>

<!-- Conte ú do principal -->
<main>

<article>

<h2>Sobre Mim</h2>

<figure>

<img src = " images/foto . jpg " alt = " Fotografia de [ Seu Nome ]

" >

<f ig cap ti on> Fo tog ra f ia tirada em [ Local/Ano ]

</figcaption>

</figure>

<p>Breve descri ç ã o sobre si (2 -3 par á grafos ) ... </p>
<p>Mais informa ç ã o ... </p>

</article>

<aside>

<h3>Destaque</h3>
<p>Alguma informa ç ã o adicional ou cita ç ã o interessante . </p>

</aside>

</main>

<!-- Rodap é -->
<footer>

<p> & copy ; 2026 [ Seu Nome ]. Todos os direitos reservados . </p>
<p>Contacto: <a href = " m ai lt o: em ai l@ ex em plo . com " >email@exemplo .

com</a></p>

</footer>

</body>
</html>

Código 1: Estrutura com elementos semânticos

3

Desenvolvimento de Aplicações Web

Lab 02 - Elementos HTML5 Semânticos, Tabelas e Multimédia

Nota Importante

Repare no uso de &copy; para o símbolo ©. Esta é uma entidade HTML que representa
caracteres especiais.

4.2 Tarefa 2: Aplicar Semântica às Restantes Páginas

Aplique a mesma estrutura semântica a pessoal.html, formacao.html, etc.:

• <header> com título da página

• <nav> com link de volta

• <main> com o conteúdo principal dentro de <article>

• <footer> com informação de copyright

4.3 Tarefa 3: Criar Tabela de Notas em formacao.html

Na página formacao.html, adicione uma secção com notas académicas:
<section>

<h2>Notas Acad é micas - ESCE</h2>

<h3>1 º Ano</h3>
<table border = " 1 " >

<thead>

<tr>

<th>Semestre</th>
<th>Unidade Curricular</th>
<th>Nota</th>

</tr>

</thead>
<tbody>

<tr>

<td rowspan = " 5 " >1 º Semestre</td>
<td>Fundamentos de Programa ç ã o</td>
<td>15</td>

</tr>
<tr>

<td>Matem á tica Discreta</td>
<td>14</td>

</tr>
<tr>

<td>Sistemas de Informa ç ã o</td>
<td>16</td>

</tr>
<tr>

<td>Compet ê ncias Co mun ica c ion a is< / td>
<td>17</td>

</tr>
<tr>

<td>Introdu ç ã o ‘a Gest ã o</td>
<td>15</td>

</tr>

4

Desenvolvimento de Aplicações Web

Lab 02 - Elementos HTML5 Semânticos, Tabelas e Multimédia

<!-- 2 º Semestre -->
<tr>

<td rowspan = " 4 " >2 º Semestre</td>
<td>Programa ç ã o Orientada a Objetos</td>
<td>16</td>

</tr>
<tr>

<td>Bases de Dados</td>
<td>17</td>

</tr>
<tr>

<td>Desenvolvimen to de Aplica ç õ es Web</td>
<td>Em curso</td>

</tr>
<tr>

<td>Estat í stica Aplicada</td>
<td>Em curso</td>

</tr>

</tbody>
<tfoot>

<tr>

<td colspan = " 2 " ><strong>M é d ia:< /stro ng></td>
< t d > < s t r o n g > 1 5 , 5 < / s t r o n g > < / t d >

</tr>

</tfoot>

</table>

</section>

Código 2: Tabela com rowspan para semestres

Elementos principais de tabelas:

• <table> — Contentor da tabela

• <thead> — Cabeçalho da tabela

• <tbody> — Corpo da tabela (dados)

• <tfoot> — Rodapé da tabela (totais, médias)

• <tr> — Table Row (linha)

• <th> — Table Header cell (célula cabeçalho)

• <td> — Table Data cell (célula de dados)

• rowspan — Célula ocupa múltiplas linhas (vertical)

• colspan — Célula ocupa múltiplas colunas (horizontal)

4.4 Tarefa 4: Adicionar Vídeo de Apresentação

Numa nova página apresentacao.html ou secção em index.html, incorpore um vídeo:
<section>

<h2>V í deo de Apresenta ç ã o</h2>

<!-- Op ç ã o 1 : V í deo local -->

5

Desenvolvimento de Aplicações Web

Lab 02 - Elementos HTML5 Semânticos, Tabelas e Multimédia

<video width = " 640 " height = " 480 " controls>

<source src = " videos/apresen taca o . mp4 " type = " video/mp4 " >
<source src = " videos/apresen taca o . webm " type = " video/webm " >
O seu browser n ã o suporta o elemento video .

</video>

<!-- Op ç ã o 2 : V í deo do YouTube ( iframe ) -->
<h3>Ou veja no YouTube:</h3>
<iframe width = " 560 " height = " 315 "

src = " https://www . youtube . com /emb ed/VIDE O_ID "
title = " V í deo de apresenta ç ã o "
frameborder = " 0 "
allow = " accelerometer ; autoplay ; encrypted-media "
allowfullscreen>

</iframe>

</section>

Nota Importante

Código 3: Incorporar multimédia (vídeo e iframe)

Se não tiver vídeo próprio, pode incorporar um vídeo do YouTube que goste ou que seja
relevante (ex.: sobre a sua área de estudo ou interesses).

4.5 Tarefa 5: Adicionar Áudio (Opcional)

Se tiver um ﬁcheiro de áudio (música favorita, podcast, etc.), adicione:

<section>

<h2>M ú sica Favorita</h2>
<audio controls>

<source src = " audio/musica . mp3 " type = " audio/mpeg " >
<source src = " audio/musica . ogg " type = " audio/ogg " >
O seu browser n ã o suporta o elemento audio .

</audio>
< p > < s t r o n g > A r t i s t a : < / s t r o n g > [ Nome do Artista ] </p>
<p><strong> Á lbum:</strong> [ Nome do Á lbum ] </p>

</section>

Código 4: Incorporar audio

4.6 Tarefa 6: Usar Elementos de Formatação Semântica

Adicione ênfase e importância ao texto usando elementossemânticos apropriados:

<p>Esta cadeira de <s tr o ng >D es e n v ol v i m en to de Aplica ç õ es Web</strong>
é <em>fundamental</em> para a minha forma ç ã o . </p>

<p>O prazo de entrega é <mark>25 de mar ç o</mark> . </p>

<p>A f ó rmula qu í mica da á gua é H<sub>2</sub>O . </p>

<p>E = mc<sup>2</sup> é a famosa equa ç ã o de Einstein . </p>

<p>Texto <del>riscado</ del> e texto < ins>inserido</ins> . </p>

6

Desenvolvimento de Aplicações Web

Lab 02 - Elementos HTML5 Semânticos, Tabelas e Multimédia

<p>Abreviatura: <abbr title = " HyperText Markup Language " >HTML</abbr></p>

Código 5: Formatação semântica

Elementos semânticos vs. visuais:

• <strong> vs. <b>: <strong> indica importância, <b> apenas negrito

• <em> vs. <i>: <em> indica ênfase, <i> apenas itálico

Use sempre elementos semânticos! O visual (negrito, itálico) virá a partir Lab 03 com CSS.

4.7 Tarefa 7: Criar Página com Mapa (iframe)

Crie uma nova página localizacao.html com informação sobre localização:
<!DOCTYPE html>
<html lang = " pt " >
<head>

<meta charset = " UTF-8 " >
<title>Localiza ç ã o - ESCE</title>

</head>
<body>

<header>

<h1>Localiza ç ã o da ESCE</h1>

</header>

<main>

<article>

<h2>Campus do IPS</h2>
< p > < s t r o n g > M o r a d a : < / s t r o n g > Campus do IPS, Estefanilha, 2910

-761 Set ú bal</p>

<iframe src = " https://www . google . com/maps/embed ? pb =

!1m 18!1m1 2!1m3 ! 1d311 5 .123456 ! "

width = " 600 "

height = " 450 "
style = " border:0 ; "
allowfullscreen = " "
loading = " lazy " >

</iframe>

<p><a href = " index . html " >← Voltar ‘a P á gina Principal</a></p>

</article>

</main>

<footer>

<p> & copy ; 2026 [ Seu Nome ] </p>

</footer>

</body>
</html>

Código 6: Página com Google Maps

Como obter código de embed do Google Maps:

1. Aceda a https://maps.google.com

7

Desenvolvimento de Aplicações Web

Lab 02 - Elementos HTML5 Semânticos, Tabelas e Multimédia

2. Pesquise a sua localização de interesse

3. Clique em “Partilhar” → “Incorporar um mapa”

4. Copie o código <iframe>

4.8 Tarefa 8: Validar Todo o HTML

1. Aceda a https://validator.w3.org/

2. Valide todas as páginas que modiﬁcou

3. Corrija quaisquer erros encontrados

4. Preste especial atenção a:

• Tabelas: rowspan e colspan com valores corretos?

• Elementos semânticos: <main>, <article> usados apropriadamente?

• Entidades HTML: &copy;, &nbsp; escritas correctamente?

5 Conceitos-Chave

5.1 Semântica HTML5

Semântica = signiﬁcado. Elementos semânticos descrevem o tipo de conteúdo, não apenas a
sua aparência.

Exemplo: código sem semântica

<div id = " header " >

<div id = " menu " > ... </div>

</div>
<div id = " content " > ... </div>
<div id = " footer " > ... </div>

Exemplo: código com semântica

<header>

<nav> ... </nav>

</header>
<main> ... </main>
<footer> ... </footer>

5.2 Tabelas: Quando Usar?

Use tabelas para:

• Dados tabulares (notas, horários, comparações)

• Informação com linhas e colunas claramente deﬁnidas

Não use tabelas para:

• Layout de página (usar CSS mais adiante no curso)

• Listas simples (usar <ul> ou <ol>)

8

Desenvolvimento de Aplicações Web

Lab 02 - Elementos HTML5 Semânticos, Tabelas e Multimédia

Símbolo
Menor que (<)
Maior que (>)
E comercial
Aspas (")
©
Espaço não-quebrável
€

Entidade
&lt;
&gt;
&amp;
&quot;
&copy;
&nbsp;
&euro;

Descrição
Less than
Greater than
Ampersand
Quotation mark
Copyright
Non-breaking space
Euro

5.3 Entidades HTML Comuns

□ Todas as páginas reestruturadas com elementos HTML5 semânticos

□ Pelo menos uma tabela com rowspan ou colspan

□ Vídeo ou iframe incorporado (YouTube, Vimeo, Google Maps)

□ Uso correcto de <strong>, <em>, <mark>

□ Entidades HTML usadas correctamente (&copy;, &nbsp;)

□ HTML válido (sem erros no W3C Validator)

□ Navegação funcional entre todas as páginas

6 Questões para Reﬂexão

1. Qual a vantagem de usar <nav> em vez de <div id="menu">?

2. Por que tabelas não devem ser usadas para layout de página?

3. Qual a diferença entre rowspan e colspan?

4. Por que usar &copy; em vez de copiar/colar o símbolo ©?

5. O que acontece se um browser não suportar o elemento <video>?

7 Próximos Passos

No decorrer da disciplina, iremos expandir nosso conhecimento de desenvolvimento web:

• Etapa 3: Estilização com CSS

– Cores, fontes, espaçamentos
– Layouts avançados com Flexbox e Grid
– Design adaptado para diferentes dispositivos

• Etapa 4: Interatividade com JavaScript (novos contextos)

– A partir daí, sairá do contexto da página pessoal e explorará novos projectos
– Comportamento dinâmico e manipulação de elementos
– Validação de dados e interações com o utilizador
– Efeitos e animações avançadas

9

Desenvolvimento de Aplicações Web

Lab 02 - Elementos HTML5 Semânticos, Tabelas e Multimédia

8 Referências

• MDN - HTML Semantics: https://developer.mozilla.org/en-US/docs/Glossary/Semantics

• MDN - HTML Tables: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/

table

• MDN - HTML Media Elements: https://developer.mozilla.org/en-US/docs/Web/HTML/

Element/video

• MDN - HTML Entities: https://developer.mozilla.org/en-US/docs/Glossary/Entity

• W3C Validator: https://validator.w3.org/

10

