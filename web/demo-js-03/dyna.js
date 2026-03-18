document.addEventListener('DOMContentLoaded', function () {
    const image = document.getElementById('cible');
    const btnAgrandir = document.getElementById('btnAgrandir');
    const btnRetrecir = document.getElementById('btnRetrecir');
    const increment = 50; /* en pixel */

    function ajouterLargeur(delta) {
        let largeur = parseInt(image.style.width) || parseInt(image.clientWidth);
        largeur += delta;
        image.style.width = largeur + 'px';
    }

    btnAgrandir.addEventListener('click', () => {
        ajouterLargeur(increment);
    });

    btnRetrecir.addEventListener('click', () => {
        ajouterLargeur(-increment);
    });
});
