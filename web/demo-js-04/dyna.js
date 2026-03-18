const btnAjouter = document.getElementById('btnAjouter');
const destination = document.getElementById('clapier');
const scrImage = [
    "thenorthbaybay-rabbit-7359240_640.jpg",
    "nennieinszweidrei-rabbits-9307357_640.jpg",
    "jaclou-dl-rabbit-4367628_640.jpg"
];
let compteur = 0;

btnAjouter.addEventListener('click', () => {
    const newImg = document.createElement('img');
    compteur = (compteur + 1) % scrImage.length;
    newImg.src = scrImage[compteur];
    newImg.style.cursor = "pointer"; /* Changement de la forme du curseur */
    newImg.title = "Supprimer"; /* Texte affiché au survol de l'image */

    newImg.addEventListener('click', () => {
        newImg.remove(); /* L'image se supprime elle-même */
    });

    destination.appendChild(newImg);
});

