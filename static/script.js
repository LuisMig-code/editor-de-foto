function editarFoto() {
    var loader = document.getElementById("loader");
    loader.style.display = "block";

    setTimeout(function() {
        loader.style.display = "none";
        document.getElementById("downloadButton").setAttribute("href", "caminho_para_a_foto_editada");
    }, 3000); // Simulação de uma edição demorada, você pode ajustar o tempo conforme necessário
}