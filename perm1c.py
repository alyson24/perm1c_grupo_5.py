web = {'https://ucsp.edu.pe/cs111/index.html': """<html>
<body>
<h1>Algoritmo CS111</h1>
<p>
Aqui encontraremos más información al respecto:
<ul>
<li> <a href="https://ucsp.edu.pe/cs111/pseudocodigo.html">Pseudocódigo</a>
<li> <a href="https://ucsp.edu.pe/cs111/implementacion.html">Implementación del algoritmo</a>
<li> <a href="https://ucsp.edu.pe/cs111/python.html">Documentación de Python</a>
</ul>

Podemos revisar comentarios adicional al respecto: 
<a href="https://ucsp.edu.pe/cs111/guido.html">Guido van Rossum</a> 
y <a href="https://ucsp.edu.pe/cs111/peter.html">Peter Norvig</a>.
</body>
</html>
""",
   'https://ucsp.edu.pe/cs111/peter.html': """<html>
<body>
<h1>Peter Norvig</h1>
<p>
Peter Norvig es un científico estadounidense, investigador en ciencias de la computación. Actualmente 
es director de investigación de la empresa Google. Ha publicado unos cincuenta artículos científicos 
sobre informática, en particular en el campo de la inteligencia artificial, el procesamiento automático 
del lenguaje natural , la recuperación de información y el diseño de software.

Con muchos años de expiencia en el lenguaje <a href="https://ucsp.edu.pe/cs111/python.html">Python</a>, 
creado por <a href="https://ucsp.edu.pe/cs111/guido.html">Guido van Rossum</a>.

</body>
</html>

""",
   'https://ucsp.edu.pe/cs111/guido.html': """<html>
<body>
<h1>Guido van Rossum</h1>
<p>
El es el creador de 
<a href="https://ucsp.edu.pe/cs111/python.html">Python</a>

</body>
</html>


""",
   'https://ucsp.edu.pe/cs111/python.html': """<html>
<body>
<h1>
Lenguaje de Programación Python
</h1>
<p>

<ol>
<li> Python 2.
<li> Python 3.
</ol>

</body>
</html>

""",
   'https://ucsp.edu.pe/cs111/implementacion.html': """<html>
<body>
<h1>
La Implementación del algoritmo
</h1>
<p>

<ol>
<li> En el siguiente link <a href="https://ucsp.edu.pe/cs111/guido.html">Guido van Rossum</a>.
<li> Cree las variables de manera correcta, siguiendo los estandares.
</ol>

</body>
</html>

""",
   'https://ucsp.edu.pe/cs111/pseudocodigo.html': """<html>
<body>
<h1>
Pseudocódigo
</h1>
<p>

<ol>
<li> 'https://ucsp.edu.pe/cs111/implementacion.html'.
<li> 'https://ucsp.edu.pe/cs111/pseudocodigo.html'.
<li> 'https://ucsp.edu.pe/cs111/pseudocodigo.html'.
<li> 'https://ucsp.edu.pe/cs111/pseudocodigo.html'.
<li> 'https://ucsp.edu.pe/cs111/pseudocodigo.html'.
<li> 'https://ucsp.edu.pe/cs111/pseudocodigo.html'.
<li> 'https://ucsp.edu.pe/cs111/pseudocodigo.html'.
<li> 'https://ucsp.edu.pe/cs111/pseudocodigo.html'.
<li> 'https://ucsp.edu.pe/cs111/pseudocodigo.html'.
</ol>

</body>
</html>

"""}

#
# Ingrese su código debajo de esta linea
# ############################################################
def imprimir_rank(rank):
   for i in rank:
      print(f"{rank.index(i)+1}. {i[1]} con un valor de {i[0]}")

salientes = {}                      
entrantes = {}
links_unicos = tuple(web.keys())

inicio = 'https:'                   
final = '.html'                     

for pagina, texto in web.items():

   conjunto_url = set() 
   while True:

      pos = texto.find(inicio)            
      pos2 = texto.find(final) + len(final) 

      if texto.find(inicio) == -1:
         break

      conjunto_url.add(texto[pos:pos2])     
      texto = texto[pos2+1:]                
   salientes[pagina] = conjunto_url

for link in links_unicos:

    lista_entrantes = []    

    for pagina, lista_salientes in salientes.items():

        if link in lista_salientes:                  
            lista_entrantes.append(pagina) 

    entrantes[link] = lista_entrantes

ranking_entrantes = []
ranking_salientes = []
ranking_importancia = []

for link in links_unicos:

   e = len(entrantes[link])
   s = len(salientes[link])
   rank = e/(s+1)

   ranking_entrantes.append((e,link))        
   ranking_salientes.append((s,link))
   ranking_importancia.append((rank,link))


ranking_entrantes.sort(reverse=True)
ranking_salientes.sort(reverse=True)
ranking_importancia.sort(reverse=True) 

print("Ranking según links salientes:\n")
imprimir_rank(ranking_salientes)
print("\nRanking según links entrantes:\n")
imprimir_rank(ranking_entrantes)
print("\nRanking según links importancia:\n")
imprimir_rank(ranking_importancia)
