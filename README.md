# Entrega1-Figueroa
<h3>Estructura del proyecto:</h3>
<ul>
  <li>Rama principal: blogfig </li>
  <li>Dos apps: core y mainblog</li>
</ul>
<h3>Apps</h3>
<ul>
    <li>Core: Manejar features genericos.(WIP)</li>
    <li>Mainblog: Manejar features particulares.</li>
</ul>


<h4>Funcionamiento</h4>
<p>En la app Mainblog se encuentra el manejo de las funcionalidades para interactuar con la Base de Datos representada en tres modelos: 
  <ul>
    <li>Proyectos</li>
    <li>Editores</li>
    <li>Autores</li>
  </ul>
Cada uno de los modelos presenta su template correspondiente vinculado al Front, en los que se disponibiliza un boton a pie de pagina a los fines de poder incorporar informacion a su respectiva base. Adicionalmente, la vista de proyectos incorpora un form para poder hacer consultas basadas en el nombre del proyecto.
</p>
<h5> Prueba desde el Nav </h5>
<p>A nivel del Front, el navegador del panel superior se encuentra configurado en los valores referidos a los tres modelos que se encuentran desarrollados actualmente con las redirecciones correspondientes. 
Adicionalmente, en el <strong>urls.py</strong> dentro de la app Core, se encuentra la referencia a las URL's correspondientes, tomando en consideracion que es en esta App donde se manejan las interacciones con las <strong>views.py</strong> de las distintas App's</p>
