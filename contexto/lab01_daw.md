Instituto Politécnico de Setúbal

Escola Superior de Ciências Empresariais

Desenvolvimento de Aplicações Web

Lab 01 - Estrutura HTML da Página Pessoal

Ano Letivo: 2025/2026

1

Introdução ao Problema

Nos primeiros trabalhos desta disciplina (2025/2026) iremos criar uma Página Pessoal (Per-
sonal Web Page).

Este primeiro projeto permite-nos desenvolver uma presença online proﬁssional que reﬂita
as nossas competências, formação, experiências e interesses. A página pode servir como port-
fólio, curriculum vitae online, ou espaço para partilhar projetos pessoais.

Criar uma página pessoal é uma forma prática de consolidar conhecimentos em desenvolvi-
mento web. Para contexto adicional sobre este tipo de projetos: https://en.wikipedia.org/
wiki/Personal_web_page.

Nota Importante

O trabalho desenvolvido ao longo do semestre contribui para a avaliação ﬁnal.
Surpreenda-nos!

2 Objetivos

Neste laboratório iremos criar a estrutura base da nossa Página Pessoal.

• Compreender a estrutura de um documento HTML5

• Criar páginas HTML interligadas

• Utilizar elementos HTML essenciais: <meta>, <br>, <hr>, <p>, <h*>, <ul>, <ol>, <li>, <img>,

<a>

• Organizar ﬁcheiros e pastas de forma estruturada

1

Desenvolvimento de Aplicações Web

Lab 01 - Estrutura HTML da Página Pessoal

• Criar navegação entre páginas

• Validar HTML com W3C Validator

3 Conteúdo da Página Pessoal

A página principal (index.html) deve conter:

• Nome e fotograﬁa (ou avatar)

• Breve descrição pessoal (2-3 parágrafos)

• Menu de navegação com links para as secções:

3.1 Secções Obrigatórias

1. Dados Pessoais (pessoal.html): Nome, data de nascimento, contactos.

2. Formação (formacao.html):

Instituições de ensino, graus obtidos, períodos (incluindo

links para os sites das instituições).

3. Curriculum Proﬁssional (curriculum.html): Experiência proﬁssional (empresas, funções,

períodos) ou competências técnicas e áreas de interesse.

4. Hobbies (hobbies.html): Interesses pessoais com breves descrições, com links para re-

cursos relacionados.

5. Outras secções relevantes para a apresentação pessoal (seja criativo!).

4 Pré-requisitos

• Visual Studio Code instalado (https://code.visualstudio.com/)

• Um browser moderno (Chrome, Firefox, Edge, ou Safari)

• Fotograﬁa pessoal ou avatar (formato JPG/PNG)

• Informação biográﬁca básica para preencher as secções

• Conhecimento básico de navegação em sistemas de ﬁcheiros

5 Conceção e Desenho do Site

Antes de começarmos a implementar, planeemos a estrutura e aparência do site.

Precisamos de considerar princípios de design que garantem usabilidade e legibilidade. Re-

cursos sobre web design:

• https://designshack.net/articles/layouts/10-rock-solid-website-layout-examples/

• https://www.creativebloq.com/web-design/steps-perfect-website-layout-812625

• https://developer.mozilla.org/en-US/docs/Learn/HTML

2

Desenvolvimento de Aplicações Web

Lab 01 - Estrutura HTML da Página Pessoal

5.1 Wireframes (Esboços Estruturais)

Sugere-se começar por wireframes — esboços que representam a estrutura e componentes
das páginas:

• https://en.wikipedia.org/wiki/Website_wireframe

• https://designmodo.com/wireframing-prototyping-mockuping/

Ferramentas sugeridas: Figma (https://www.figma.com/), Excalidraw (https://excalidraw.

com/), ou (porque não?) papel e lápis.

Ferramentas online gratuitas facilitam a criação rápida de wireframes sem necessidade de

instalar software.

6 Procedimento

Nota Importante

Aviso Importante: Ao copiar código deste documento para o seu editor, tenha cuidado
com aspas, hífenes e outros símbolos tipográﬁcos. Documentos PDF ou Word podem
converter aspas retas (") em aspas curvas (“”), hífenes em travessões, etc. Recomenda-
se reescrever o código manualmente ou colar em editor de texto simples (Notepad) antes
de levar para VS Code.

6.1 Tarefa 1: Criar Estrutura de Pastas e Ficheiros

1. Crie uma pasta PaginaPessoal

2. Dentro dela, crie as subpastas:

• images — imagens e fotograﬁas
• styles — ﬁcheiros CSS (laboratórios futuros)
• scripts — ﬁcheiros JavaScript (se necessário)

3. Abra Visual Studio Code

4. Selecione “File” → “Open Folder...” → PaginaPessoal

Nota Importante

Esta organização separa conteúdo (HTML), apresentação (CSS), comportamento (JS) e
recursos (images).

3

Desenvolvimento de Aplicações Web

Lab 01 - Estrutura HTML da Página Pessoal

Nota Importante

Convenção de Nomes: Todos os nomes de ﬁcheiros e pastas devem ter:

• Apenas letras minúsculas (a-z)

• Números (0-9)

• Hífenes () ou underscores (_)

• Sem acentos (à, é, ç, etc)

• Sem espaços

• Sem caracteres especiais (#, @, %, etc)

Exemplos corretos: index.html, meu-perfil.html, formacao.html, foto-perfil.jpg
Exemplos incorretos: Meu Perfil.html, ação.html, Foto-Perfil.jpg
Esta prática evita problemas em servidores, especialmente Linux/Mac que diferenciam
maiúsculas de minúsculas.

6.2 Tarefa 2: Criar Página Principal (index.html)

1. No VS Code, crie um novo ﬁcheiro (File → New File)

2. Guarde como index.html na raiz de PaginaPessoal

3. Insira a estrutura HTML5:

<!DOCTYPE html>
<html lang = " pt " >
<head>

<meta charset = " UTF-8 " >
<meta name = " viewport " content = " width = device-width, initial-scale =1.0

" >

<meta name = " description " content = " P á gina Pessoal de [ Seu Nome ] " >
<meta name = " keywords " content = " portfolio, curriculum, pessoal " >
<meta name = " author " content = " [ Seu Nome ] " >
<title>P á gina Pessoal - [ Seu Nome ] </title>

</head>
<body>

<h1> [ Seu Nome ] </h1>
<img src = " images/foto . jpg " alt = " Fotografia de [ Seu Nome ] " >

<p>Breve descri ç ã o pessoal (2 -3 par á grafos ) . </p>
<p>Mais informa ç ã o pessoal ... </p>

<hr>

<h2>Menu de Navega ç ã o</h2>
<ul>

<li><a href = " pessoal . html " >Dados P essoais</a></li>
<li><a href = " formacao . html " >Forma ç ã o</a></li>
<li><a href = " curriculum . html " >C urr i cul u m</ a> </ li >
<li><a href = " hobbies . html " >Hobbies</a></li>

</ul>

4

Desenvolvimento de Aplicações Web

Lab 01 - Estrutura HTML da Página Pessoal

</body>
</html>

Nota Importante

Código 1: Estrutura básica de index.html

Substitua [Seu Nome] pelo seu nome real! Personalize todo o conteúdo.

6.3 Tarefa 3: Adicionar Fotograﬁa

1. Escolha uma fotograﬁa ou avatar

2. Copie para a pasta images

3. Renomeie para foto.jpg ou foto.png

4. Veriﬁque o caminho no HTML: src="images/foto.jpg"

5. Teste: abra index.html no browser (botão direito → Open with)

6.4 Tarefa 4: Criar Página “Dados Pessoais”

1. Crie pessoal.html

2. Use estrutura HTML5 semelhante a index.html

3. Inclua:

• Nome completo
• Data de nascimento e idade
• Contactos (email opcional)
• Localização (cidade/país)

4. Adicione link de retorno: <a href="index.html">Voltar</a>

<!DOCTYPE html>
<html lang = " pt " >
<head>

<meta charset = " UTF-8 " >
<title>Dados Pessoais - [ Seu Nome ] </title>

</head>
<body>

<h1>Dados Pessoais</h1>

< p > < s tr o n g > N o m e : < /s t r o n g > [ Nome Completo ] </p>
<p><strong>Data de Nasciment o :</ s tro n g> [ DD/MM/AAAA ] ( XX anos ) </p>
< p > < s t r o n g > C o n t a c t o : < / s t r o n g > [ email@exemplo . com ] </p>
<p><strong>Localiza ç ã o:</strong> [ Cidade, Pa í s ] </p>

<hr>
<p><a href = " index . html " >Voltar</a></p>

</body>
</html>

Código 2: Estrutura de pessoal.html

5

Desenvolvimento de Aplicações Web

Lab 01 - Estrutura HTML da Página Pessoal

6.5 Tarefa 5: Criar Página “Formação”

1. Crie formacao.html

2. Liste instituições de ensino

3. Para cada uma:

• Nome da instituição

• Grau obtido ou em curso

• Período (ex.: 2020-2023)

• Link para o site da instituição

• Logo da instituição (opcional)

<h1>Forma ç ã o Acad é mica</h1>

<h2>Licenciatura em Gest ã o de Sistemas de Informa ç ã o</h2>
< p>< s trong>Institui ç ã o:</strong> <a href = " https://www . esce . ips . pt "

target = " _blank " >ESCE - IPS</a></p>

<p><strong>Per í odo:</strong> 2024 - presente</p>
<p><strong>Descri ç ã o:</strong> Curso focado em sistemas de informa ç ã o,

bases de dados, desenvolvimento web e gest ã o de projetos . </p>

<hr>

<h2>Ensino Secund á rio</h2>
<p><strong>Institui ç ã o:</strong> [ Nome da Escola Secund á ria ] </p>
<p><strong>Per í odo:</strong> 2020 - 2023 </p>
<p><strong> Á rea:</strong> Ci ê ncias e Tecnologias</p>

<hr>
<p><a href = " index . html " >Voltar</a></p>

Código 3: Exemplo de formacao.html

6.6 Tarefa 6: Criar Página “Curriculum”

1. Crie curriculum.html

2. Com experiência proﬁssional:

• Empresa/instituição

• Função

• Período

• Descrição das responsabilidades

• Link para o site da empresa

3. Sem experiência: liste competências técnicas, áreas de interesse ou projetos académicos

6

Desenvolvimento de Aplicações Web

Lab 01 - Estrutura HTML da Página Pessoal

<h1>Curriculum Profissional</h1>

<h2> Á reas de Interesse</h2>
<ul>

< li> Desenvolvimento Web ( HTML, CSS, JavaScript ) </li>
<li>Bases de Dados ( SQL, PostgreSQL ) </li>
<li>Sistemas de Informa ç ã o</li>
<li>An á lise de Dados</li>

</ul>

<h2>Compet ê ncias T é cnicas</h2>
<ul>

<li>Microsoft Office ( Word, Excel, PowerPoint ) </li>
<li>Programa ç ã o em Python ( b á sico ) </li>
<li>HTML e CSS ( em aprendizagem ) </li>

</ul>

<hr>
<p><a href = " index . html " >Voltar</a></p>

Código 4: Exemplo curriculum.html (sem experiência)

6.7 Tarefa 7: Criar Página “Hobbies”

1. Crie hobbies.html

2. Liste hobbies e interesses

3. Para cada um:

• Nome do hobby

• Descrição breve

• Links relacionados (associações, comunidades)

<h1>Hobbies e Interesses</h1>

<h2>Fotografia</h2>
<p>Pratico fotorafia amadora h á 5 anos . Gosto especialmente de

fotografar elementos da natureza . </p>

<p>Links ú teis:</p>
<ul>

<li><a href = " https://www . instagram . com " target = " _blank "

>Instagram</a></li>

<li><a href = " https://www . flickr . com " target = " _blank " >Flickr</a></li>

</ul>

<hr>

<h2>Desporto: Nata ç ã o</h2>
<p>Nado regularmente h á 5 anos . Gosto especialmente de nata ç ã o

sincronizada e competi ç õ es . </p>

<p><a href = " https://www . fnp . pt " target = " _blank " >Federa ç ã o Nacional de

Nata ç ã o</a></p>

7

Desenvolvimento de Aplicações Web

Lab 01 - Estrutura HTML da Página Pessoal

<hr>
<p><a href = " index . html " >Voltar</a></p>

Código 5: Estrutura de hobbies.html

6.8 Tarefa 8: Testar Navegação

1. Abra index.html no browser

2. Teste todos os links do menu

3. Veriﬁque se as páginas abrem corretamente

4. Teste os links de retorno

5. Conﬁrme que as imagens aparecem

Nota Importante

Problemas comuns: nome do ﬁcheiro incorreto, ﬁcheiro na pasta errada, capitalização
inconsistente.

6.9 Tarefa 9: Validar HTML

1. Aceda a https://validator.w3.org/

2. Selecione “Validate by File Upload”

3. Faça upload de index.html

4. Analise os resultados:

• Sem erros: ótimo!

• Com erros: leia as mensagens e corrija

5. Repita para todas as páginas

6.10 Tarefa 10: Usar Ferramentas de Desenvolvedor

1. Abra index.html no browser

2. Pressione F12 (ou Ctrl+Shift+I)

3. Explore:

• Elements: estrutura HTML renderizada
• Console: mensagens de erro (deve estar vazio)

4. Experimente:

• Botão direito num elemento → “Inspect”

• Observe a hierarquia do HTML

8

Desenvolvimento de Aplicações Web

Lab 01 - Estrutura HTML da Página Pessoal

7 Conceitos-Chave

7.1 Estrutura HTML5

• <!DOCTYPE html> — Declaração HTML5

• <html lang="pt"> — Elemento raiz com idioma

• <head> — Metadados (título, charset, descrição)

• <body> — Conteúdo visível

7.2 Elementos Semânticos

• <h1> a <h6> — Títulos hierárquicos

• <p> — Parágrafos

• <ul>, <ol>, <li> — Listas e itens

• <a href="..."> — Links

• <img src="..." alt="..."> — Imagens (alt obrigatório)

• <hr> — Separador horizontal

• <br> — Quebra de linha

7.3 Atributos Importantes

• lang="pt" — Idioma português

• charset="UTF-8" — Codiﬁcação (suporta acentos)

• href="..." — Caminho do link

• src="..." — Caminho da imagem

• alt="..." — Texto alternativo

• target="_blank" — Abre em nova aba

7.4 Caminhos

• Relativo: images/foto.jpg — relativo ao ﬁcheiro HTML

• Absoluto: https://example.com/foto.jpg — URL completo

9

Desenvolvimento de Aplicações Web

Lab 01 - Estrutura HTML da Página Pessoal

8 Resultado Esperado

No ﬁnal desta tarefa, deve ter:

□ Uma pasta PaginaPessoal com estrutura organizada (images, styles, scripts)
□ Ficheiro index.html com página principal e menu de navegação
□ Ficheiros pessoal.html, formacao.html, curriculum.html, hobbies.html
□ Navegação funcional entre todas as páginas

□ Pelo menos 1 fotograﬁa/imagem incorporada

□ HTML válido (sem erros no W3C Validator)

□ Código legível e bem indentado

9 Questões para Reﬂexão

1. Porque é que HTML é uma “linguagem de marcação” e não de “programação”?

2. Qual a diferença entre usar um título e formatar texto com tamanho grande?

3. Porque organizar ﬁcheiros em pastas é importante?

4. O que acontece sem texto alternativo numa imagem?

5. Porque validar HTML, mesmo quando “funciona”?

10 Próximos Passos

No decorrer da disciplina, iremos expandir a Página Pessoal com:

• Etapa 2: Estrutura semântica e elementos avançados

– Organização mais eﬁciente da página com elementos semelhantes
– Adição de tabelas para apresentar informação estruturada
– Média: vídeo, áudio
– Expansão do conteúdo das secções

• Etapa 3: Apresentação visual e design

– Estilização da página
– Cores, fontes, espaçamentos
– Layouts avançados
– Design adaptado para diferentes dispositivos

10

Desenvolvimento de Aplicações Web

Lab 01 - Estrutura HTML da Página Pessoal

11 Referências

• MDN Web Docs - HTML: https://developer.mozilla.org/en-US/docs/Web/HTML

• HTML Living Standard: https://html.spec.whatwg.org/

• W3C Validator: https://validator.w3.org/

• VS Code Docs: https://code.visualstudio.com/docs

• Web.dev (Google): https://web.dev/learn/html

11

