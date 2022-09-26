const btnsEliminacion = document.querySelectorAll('.btnEliminacion');

(function ()  {

    notificacionSwal(document.title, "Cursos listados con éxito", "success",);

    formularioCurso.addEventListener('submit', function(e){
        let nombre = String(txtCurso.value).trim();
        if (nombre.length === 0) {
            alert("Debes llenar el campo Nombre de Curso");
            e.preventDefault();
        }
    });

    btnsEliminacion.forEach(btn => {
        btn.addEventListener("click", function(e){
            let confirmation=confirm("¿Deseas eliminar el Curso?");
            if (!confirmation) {
                e.preventDefault();
            }
        });
    });
})();