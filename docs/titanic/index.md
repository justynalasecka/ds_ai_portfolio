# Analiza EDA katastrofy RMS Titanic

Zapraszam do zapoznania się z analizą danych katastrofy "Titanica".  
  
  Spis treści:  
    
  *1. Ogólny przegląd danych  
  2. Analiza brakujących wartości  
  3. Transformacja danych  
  4. Analiza statystyczna
    <ul style="list-style-type: none; padding-left: 20px;">
      <li>4.1. Ogólne cechy danych liczbowych</li>
      <li>4.2. Zależność przeżycia od klasy biletu</li>
      <li>4.3. Zależność przeżycia od płci</li>
      <li>4.4. Zależność przeżycia od płci i klasy biletu</li>
      <li>4.5. Rozkład wieku dla mężczyzn i kobiet</li>
    </ul>
  5. Wnioski*

<a href="titanic.ipynb" class="md-button md-button--primary">Pobierz Notebook</a>

<iframe
  id="content"
  src="titanic.html"
  width="100%"
  style="border:1px solid black;overflow:hidden;"
></iframe>
<script>
function resizeIframeToFitContent(iframe) {
  iframe.style.height = (iframe.contentWindow.document.documentElement.scrollHeight + 50) + "px";
  iframe.contentDocument.body.style["overflow"] = 'hidden';
}
window.addEventListener('load', function() {
  var iframe = document.getElementById('content');
  resizeIframeToFitContent(iframe);
});
window.addEventListener('resize', function() {
  var iframe = document.getElementById('content');
  resizeIframeToFitContent(iframe);
});
</script>